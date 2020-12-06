from __future__ import absolute_import, division, print_function

__metaclass__ = type

#from urllib.parse import quote
import time
from ansible.module_utils._text import to_text
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_text
from ansible_collections.community.datapower.plugins.module_utils import (
    config
)

MGMT_CONFIG_BASE_WITH_OBJECT_CLASS_URI = '/mgmt/config/{0}/{1}' 
MGMT_CONFIG_WITH_NAME_URI = '/mgmt/config/{0}/{1}/{2}'
MGMT_CONFIG_WITH_FIELD_URI = '/mgmt/config/{0}/{1}/{2}/{3}'
ACTION_QUEUE_URI = '/mgmt/actionqueue/{0}'
FILESTORE_URI_PUT = '/mgmt/filestore/{0}/{1}/{2}'
FILESTORE_URI_POST = '/mgmt/filestore/{0}/{1}'

# Define the keys that get returned to the modules.  
# REQUEST_DETAILS_KEY is helps for debugging.
RESPONSE_KEY = 'response'
REQUEST_DETAILS_KEY = 'request'
VALID_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

def _make_request(connection, method, path,  body=None):
    return connection.send_request(body, path, method)

   
def clean_dp_dict(dict_):
    _scrub(dict_, '_links')
    _scrub(dict_, 'href')
    _scrub(dict_, 'state')


class DPRequest:

    def __init__(self, path=None, method=None, body=None):
        self.path = path
        self.method = method
        self.body = body
    
    def set_body(self, body):
        self.body = body
    
    def set_path(self, path):
        self.path = path

    def set_method(self, method):
        if method in VALID_METHODS:
            self.method = method
        else:
            raise ConnectionError('Method not supported, choose from \
                                    GET, POST, PUT, DELETE')

class DPManageConfigRequest(DPRequest):


    def set_path(self):
        if not self.get_class_name():
            raise AttributeError('class_name field is required.')
        if hasattr(self, 'obj_field') and self.obj_field:
            self.path = MGMT_CONFIG_WITH_FIELD_URI.format(self.domain, self.class_name, self.get_object_name(), self.obj_field)
        elif hasattr(self, 'name') and self.obj_field == None:
            self.path = MGMT_CONFIG_WITH_NAME_URI.format(self.domain, self.class_name, self.get_object_name())
        else:
            self.path = MGMT_CONFIG_BASE_WITH_OBJECT_CLASS_URI.format(self.domain, self.class_name)


class DPUpdateConfig(DPManageConfigRequest):
    def __init__(self, module):
        super(DPUpdateConfig, self).__init__(module)
  
URI_OPTIONS = [
    'recursive' : {
        view : True
    }
    'state' : {
        'state': 1
    },
    'depth' 
]

class DPGetConfigRequest(DPManageConfigRequest):
    def __init__(self, **kwargs):
        super(DPGetGetConfigRequest, self).__init__(**kwargs)
        if not is_valid_class(self.class_name):
            raise ValueError('Invalid class_name.')

        self.set_uri_options(kwargs.get('options'))
        self.set_path()
        self.method = 'GET'

    def set_path(self, **kwargs):
        super(DPGet, self).set_path()
        opt_str = self._get_options()
        self.path = self.path + '?' + opt_str

    def set_depth_option(self, depth):
        if depth > 0 and depth <= 7:
            self.options.append({'depth': depth})
        else:
            raise AttributeError('depth must be 1-7.')
        
    def set_uri_options(self, **kwargs):
        for k,v in kwargs.items():
            if k in URL_OPTIONS

    def _get_options(self):
        url_params = {}
        if not hasattr(self, 'state') and not hasattr(self,'recursive'):
            return ''
        if self.state:
            url_params['state'] = '1'
        if self.recursive:
            url_params['view'] = 'recursive'
            if self.depth:
                url_params['depth'] = self.depth
            else:
                url_params['depth'] = '3'
        return urlencode(url_params, doseq=0)


class DPDeleteConfig(DPManageConfigRequest):
    
    def __init__(self, module):
        super(DPDelete, self).__init__(module)
        self.set_path()
        self.set_method('DELETE')


class DPAction(DPRequest):
    def __init__(self, module):
        super(DPAction, self).__init__(module)
        self.path = ACTION_QUEUE_URI.format(self.domain)
        self.method = 'POST'



class DPUploadFile(DPRequest):
    def __init__(self, module):
        super(DPUploadFile, self).__init__(module)  
        # Always strip /
        self.dir = self.dir.rstrip('/').lstrip('/')
        if self.overwrite:
            self.method = 'PUT'
            self.path = FILESTORE_URI_PUT.format(self.domain, self.dir, self.filename)
        else:
            self.method = 'POST'
            self.path = FILESTORE_URI_POST.format(self.domain, self.dir)
       
        self.body = {
            'file': {
                'name': self.filename,
                'content': self.content
            }
        }


class DPExportList:
    def __init__(self, objects):
        for obj in objects:
            for k, v in obj.items():
                if k == 'name' or k == 'class':
                    continue
                # Need a couple strips here to accommodate for - and _ in python code.
                # Keys need to match DP REST interface.
                obj[k.replace('_', '-')] = v
                del obj[k]
        self.objects = objects
    def _get_export_list(self):
        return self.objects


class DPConfigActions(DPRequest):

    def __init__(self, module):
        super(DPConfigActions, self).__init__(module)

    def _process_request(self, method, path, body):
        result = super(DPConfigActions, self)._process_request(method, path, body)
        export_path = None
        if result.get(RESPONSE_KEY).get('_links', None):
            export_path = result.get(RESPONSE_KEY)['_links']['location']['href']
        else:
            return result
        if export_path:
            while True:
                exp_res = super(DPConfigActions, self)._process_request('GET', export_path, body=None)
                if exp_res.get(RESPONSE_KEY)['status'] == 'completed':
                    return exp_res
                time.sleep(2)
        return result


class DPExport(DPConfigActions):

    def __init__(self, module):
        super(DPExport, self).__init__(module)
        if self.body.get('Export').get('Domain') and self.body.get('Export').get('Object'):
            raise AttributeError('Domain and Object are mutually exclusive')
        if self.body.get('Export').get('Domain', None):
            list_type = 'Domain'
        elif self.body.get('Export').get('Object', None):
            list_type = 'Object'
        else: 
            list_type = 'All'
        self.path = self.get_path()
        self.method = 'POST'
        if list_type != 'All':
            dp_exports = DPExportList(
                self.body.get('Export').get(list_type)
            )._get_export_list()
            self.body['Export'][list_type] = dp_exports


    def get_path(self):
        return ACTION_QUEUE_URI.format(self.domain)


class DPLoadConfig(DPConfigActions):

    def __init__(self, module):
        super(DPLoadConfig, self).__init__(module)
        self.path = ACTION_QUEUE_URI.format(self.domain)
        self.method = 'POST'


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


# TODO
# This is hardcoded, pinned to DataPower v 10.0.1.0.
# This could be greatly improved by having it check an AnsibleFact.
# Would need to add a fact Module that gathers valid config object types
# from GET /mgmt/config/ and store it as a fact.
def is_valid_class(class_name):
    return config.val_obj_dict['_links'].get(class_name) or False
