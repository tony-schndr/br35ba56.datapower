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
    
    def process_request(self, path, method, body):
        if body not None:
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


class DPManageConfigRequestHandler(DPRequestHandler):

    def __init__(self, connection):
        super(DPManageConfigRequestHandler, self).__init__(connection)
        self.check_mode = check_mode
        self.diff_mode = diff_mode
    
    def build_request(self, **kwargs):
        

class DPActionQueueRequestHandler(DPRequestHandler):
    def __init__(self, connection):
        super(DPFileStoreRequestHandler, self).__init__(connection)


class DPFileStoreRequestHandler(DPRequestHandler):
    def __init__(self, connection):
        super(DPFileStoreRequestHandler, self).__init__(connection)
