from __future__ import absolute_import, division, print_function

__metaclass__ = type

import time
import json
from xml.sax.saxutils import unescape

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
        # Remove any links that are not valid datapower config
        if body is not None:
            _scrub(body, '_links')
            _scrub(body, 'href')
            _scrub(body, 'state')
        return self.connection.send_request(path, method, body)

    def process_request(self, path, method, body=None):

        try:
            resp = self._make_request(path, method, body)
        except ConnectionError:
            raise
        resp_str = json.dumps(resp)
        # DataPower will sometimes return xml encoded strings, unescape
        # ie. &amp is found in strings in AccessProfile and ConfigDeploymentPolicy objects.
        data = json.loads(unescape(resp_str)) 
        return data


class DPManageConfigRequestHandler(DPRequestHandler):
    
    def __init__(self, connection):
        super(DPManageConfigRequestHandler, self).__init__(connection)

    def config_info(self, domain='default', class_name=None):
        if class_name is None:
            path = MGMT_CONFIG_URI
        else:
            path = MGMT_CONFIG_METADATA_URI.format(domain, class_name)
        metadata = self._make_request(path, 'GET', body=None)
        if metadata['_links']['self']['href'] == MGMT_CONFIG_URI:
            metadata = list(metadata['_links'].keys())
            metadata.sort()
            metadata.remove('self')
            return metadata

        props = metadata['object']['properties']['property']
        types = self.get_types(props)

        return {'metadata': metadata, 'types': types}


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
