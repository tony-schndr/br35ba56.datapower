from __future__ import absolute_import, division, print_function

__metaclass__ = type

import time
from ansible.module_utils.connection import Connection, ConnectionError
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPManageConfigRequest,
    MGMT_CONFIG_METADATA_URI,
    MGMT_CONFIG_URI
)
ACTION_QUEUE_TIMEOUT = 300

class DPRequestHandler:
    
    def __init__(self, connection):
        self.connection = connection

    def _make_request(self, path, method, body):
        if body is not None:
            _scrub(body, '_links')
            _scrub(body, 'href')
            _scrub(body, 'state')
        try:
            response = self.connection.send_request(body,path,method)
        except ConnectionError:
            raise
        return response

    def process_request(self, path, method='GET', body=None):
        resp = self._make_request(path, method, body)
        return resp


class DPManageConfigRequestHandler(DPRequestHandler):
    
    def __init__(self, connection):
        super(DPManageConfigRequestHandler, self).__init__(connection)

    def get_schema(self, domain, class_name):
        path = MGMT_CONFIG_METADATA_URI.format(domain, class_name)

    def config_info(self, domain='default', class_name=None):
        if class_name is None:
            path = MGMT_CONFIG_URI
        else:
            path = MGMT_CONFIG_METADATA_URI.format(domain, class_name)
        resp = self._make_request(path, 'GET', body=None)
        if resp['_links']['self']['href'] == MGMT_CONFIG_URI:
            resp = list(resp['_links'].keys())
            resp.sort()
        return resp 

class DPGetConfigRequestHandler(DPRequestHandler):
    
    def __init__(self, connection):
        super(DPGetConfigRequestHandler, self).__init__(connection)

class ActionQueueTimeoutError(Exception):
    pass

class DPActionQueueRequestHandler(DPRequestHandler):
    def __init__(self, connection):
        super(DPActionQueueRequestHandler, self).__init__(connection)

    def process_request(self, path, method, body=None):
        resp = self._make_request(path, method, body)
        if self.is_completed(resp):
            return resp
        else:
            path = resp['_links']['location']['href']
            start_time = time.time()
            while not self.is_completed(resp):
                if (time.time() - start_time) > ACTION_QUEUE_TIMEOUT:
                    raise ActionQueueTimeoutError('Could not retrieve status within defined time out' + path)
                time.sleep(2)
                resp = self._make_request(path, 'GET', None)     
        return resp

    def is_completed(self, resp):
        for k, v in resp.items():
            if v == 'Operation completed.' or v == 'completed':
                return True
        else:
            return False

class DPFileStoreRequestHandler(DPRequestHandler):
    def __init__(self, connection):
        super(DPFileStoreRequestHandler, self).__init__(connection)
        

def _scrub(obj, bad_key):
    """
    Removes specified key from the dictionary in place.
    :param obj: dict, dictionary from DataPowers get object config rest call
    :param bad_key: str, key to remove from the dictionary
    """
    if isinstance(obj, dict):
        for key in list(obj.keys()):
            if key == bad_key:
                del obj[key]
            else:
                _scrub(obj[key], bad_key)
    elif isinstance(obj, list):
        for i in reversed(range(len(obj))):
            if obj[i] == bad_key:
                del obj[i]
            else:
                _scrub(obj[i], bad_key)
    else:
        # neither a dict nor a list, do nothing
        pass

def clean_dp_dict(dict_):
    _scrub(dict_, '_links')
    _scrub(dict_, 'href')
    _scrub(dict_, 'state')
