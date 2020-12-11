from __future__ import absolute_import, division, print_function

__metaclass__ = type

#from urllib.parse import quote
import time
from ansible.module_utils._text import to_text
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_text
from ansible_collections.community.datapower.plugins.module_utils import (
    requests
)


class DPRequestHandler:
    
    def __init__(self, connection):
        self.connection = connection

    def make_request(self, path, method, body):
        if body is not None:
            _scrub(body, '_links')
            _scrub(body, 'href')
            _scrub(body, 'state')
        try:
            response = self.connection(
                path=path,
                method=method,
                body=body
            )
        except ConnectionError:
            raise
        return response

    def process_request(self, **kwargs):
        pass


class DPManageConfigRequestHandler(DPRequestHandler):
    METADATA_URI = '/mgmt/metadata/{0}/{1}'
    def __init__(self, req, connection, check_mode, diff_mode):
        super(DPManageConfigRequestHandler, self).__init__(connection)
        self.req = req
        self.check_mode = check_mode
        self.diff_mode = diff_mode
    
    def process_request(self):
        pass

    def process_change_status(self):
        pass

    def get_schema(self, domain, class_name, name):


    def get_current_state(self, req):
        resp = self.make_request(req.path, 'GET', None)
        
        
        
        


class DPActionQueueRequestHandler(DPRequestHandler):
    def __init__(self, connection):
        super(DPFileStoreRequestHandler, self).__init__(connection)


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

