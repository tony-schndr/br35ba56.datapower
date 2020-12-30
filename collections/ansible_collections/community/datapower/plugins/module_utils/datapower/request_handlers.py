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
     
        return self.connection.send_request(body,path,method)

    def process_request(self, path, method='GET', body=None):
        try:
            resp = self._make_request(path, method, body)
        except ConnectionError:
            raise
        return resp


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
            return metadata

        props = metadata['object']['properties']['property']
        types = self.get_types(props)

        return {'metadata': metadata, 'types': types}

    def get_types(self, props):
        types = []
        for prop in props:
            href = prop['type']['href']
            if not self.has_type(types, href):
                type_ = self._make_request(prop['type']['href'], 'GET', None)
                types.append(type_)
        
        hrefs = []
        type_stack = list(types)
        # Need to continue looping until all types are processed off this stack and added types list
        # this is account for types that return nested properties, if we find a type that returned 
        # properties add the hrefs to be processed later  
        while len(type_stack) > 0: 
            type_ = type_stack.pop()
            if 'properties' in type_.keys():
                for prop in type_['properties']['property']:
                    hrefs.append(prop['type']['href'])  

            while len(hrefs) > 0:
                href = hrefs.pop()
                if not self.has_type(types, href):
                    type_ = self._make_request(href, 'GET', None)
                    type_stack.append(type_)
        return types

    @staticmethod
    def has_type(types, href):
        for type_ in types:
            if href == type_['_links']['self']['href']:
                return True
        else:
            return False

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
