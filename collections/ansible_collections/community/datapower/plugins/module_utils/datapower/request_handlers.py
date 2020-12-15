from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.connection import Connection, ConnectionError


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

    def process_request(self, req):
        resp = self._make_request(req.path, req.method, req.body)
        return resp

METADATA_URI = '/mgmt/metadata/{0}/{1}'

class DPManageConfigRequestHandler(DPRequestHandler):
    
    def __init__(self, connection):
        super(DPManageConfigRequestHandler, self).__init__(connection)

    def get_schema(self, domain, class_name, name):
        path = METADATA_URI.format(domain, class_name, name)
        resp = self._make_request(path, 'GET', body=None)
        return resp

    def get_current_state(self, req):
        resp = self._make_request(req.path, 'GET', None)
        clean_dp_dict(resp)
        return resp


class DPGetConfigRequestHandler(DPRequestHandler):
    
    def __init__(self, connection):
        super(DPGetConfigRequestHandler, self).__init__(connection)

    def get_config(self, dp_req):
        resp = self._make_request(dp_req.path, 'GET', body=None)
        return resp


class DPActionQueueRequestHandler(DPRequestHandler):
    def __init__(self, connection):
        super(DPActionQueueRequestHandler, self).__init__(connection)

    def process_request(self, path, method, body=None):
        resp = self._make_request(path, method, body)
        return resp

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
