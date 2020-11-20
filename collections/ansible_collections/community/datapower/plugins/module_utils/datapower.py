from __future__ import absolute_import, division, print_function

__metaclass__ = type

#from urllib.parse import quote
import time
from ansible.module_utils._text import to_text
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_text
from ansible_collections.community.datapower.plugins.module_utils import (
    actionqueue,
    filestore,
    config,
)
#import config

GET_CONFIG_URI = '/mgmt/config/{0}/{1}' 
GET_CONFIG_NAME_URI = '/mgmt/config/{0}/{1}/{2}'
GET_CONFIG_NAME_FIELD_URI = '/mgmt/config/{0}/{1}/{2}/{3}'
MOD_CONFIG_URI = '/mgmt/config/{0}/{1}/{2}'
MOD_CONFIG_FIELD_URI = '/mgmt/config/{0}/{1}/{2}/{3}'
DELETE_URI = '/mgmt/config/{0}/{1}/{2}'
DELETE_FIELD_URI = '/mgmt/config/{0}/{1}/{2}/{3}'
MODIFY_URI = '/mgmt/config/{0}/{1}/{2}'
CREATE_CONFIG_URI = '/mgmt/config/{0}/{1}'
ACTION_QUEUE_URI = '/mgmt/actionqueue/{0}'
FILESTORE_URI = '/mgmt/filestore/{0}/{1}/{2}'

#Define the keys that get returned to the modules.  REQUEST_DETAILS_KEY is here for debugging purposes.
RESPONSE_KEY = 'response'
REQUEST_DETAILS_KEY = 'request'
CONNECTION_ERROR_KEY = 'ConnectionError'

def is_valid_class(class_name):
    return config.val_obj_dict['_links'].get(class_name) or False


# TODO  Should this stay here?  
def _body_has_name(body):
    return 'name' in  body.get(list(body.keys())[0])


def check_for_error(response):
    for k in response.get(RESPONSE_KEY).keys():
        if 'error' in k.lower():
            return True
    else:
        return False


class DPRequest:

    def __init__(self, module, **kwargs):
        if module:
            self.module = module
            for k, v in module.params.items():
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
        self.connection = Connection(module._socket_path)

    def _process_request(self, method, path, body):
        result = {}
        # If the payload is being generated and modified from a get request you will have these keys in the payload
        # For convineince remove these so its a valid payload being sent back to DataPower REST Interface

        _scrub(body, '_links')
        _scrub(body, 'href')
        _scrub(body, 'state')
        try:
            result[REQUEST_DETAILS_KEY] = {'body': body, 'path': path, 'method': method}
            result[RESPONSE_KEY] = self.connection.send_request(body, path, method)
        except ConnectionError:
            raise
        return result

    def send_request(self):
        try:
            if hasattr(self, 'body'):
                return self._process_request(self.method, self.path, self.body)
            else:
                return self._process_request(self.method, self.path, None)
        except ConnectionError:
            raise

    def get_class_name(self):
        if hasattr(self, 'class_name') and self.class_name is not None:
            return self.class_name
        else:# hasattr(self, 'body'):
            return list(self.body.keys())[0]
                    

class DPModify(DPRequest):
    def __init__(self, module):
        super(DPModify, self).__init__(module)
        self.class_name = self.get_class_name()
        if not is_valid_class(self.class_name):
            raise AttributeError('Class name %s is not a valid DataPower class_name' % self.class_name)
        if self.class_name and self.name and self.obj_field:
            pass
        elif _body_has_name(self.body):
            self.name = self.body.get(
                 self.class_name
            ).get('name')
        else:
            raise AttributeError('DPModify miscombination, if your targeting the object, body is all you need.  \
            If your targeting a list property in an object, you need to pass class_name, name and obj_field')
        
        self.path = self._get_uri()
        if module.check_mode:
            self.method = 'GET'
            self.body = None

    def _get_uri(self):
        if self.obj_field:
            self.method = 'POST'
            return MOD_CONFIG_FIELD_URI.format(self.domain, self.class_name, self.name, self.obj_field)
        else:
            self.method = 'PUT'
            return MOD_CONFIG_URI.format(self.domain, self.class_name, self.name)


class DPGet(DPRequest):
    def __init__(self, module):
        super(DPGet, self).__init__(module)
        if not is_valid_class(self.class_name):
            raise ValueError('Invalid class_name.')
        self.path = self._get_uri()
        self.method = 'GET'

    def _get_uri(self):
        opt_str = self._get_options()
        if self.name:
            if self.obj_field:
                return GET_CONFIG_NAME_FIELD_URI.format(
                                                        self.domain,
                                                        self.class_name,
                                                        self.name,
                                                        self.obj_field
                                                        ) + '?' + opt_str
            else:
                return GET_CONFIG_NAME_URI.format(
                                                  self.domain,
                                                  self.class_name,
                                                  self.name
                                                  ).rstrip('/') + '?' + opt_str
        else:
            return CREATE_CONFIG_URI.format(
                                            self.domain,
                                            self.class_name
                                            ).rstrip('/') + '?' + opt_str

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
                url_params['depth'] = '5'
        return urlencode(url_params, doseq=0)


class DPDelete(DPRequest):
    
    def __init__(self, module):
        super(DPDelete, self).__init__(module)
        if not is_valid_class(self.class_name): 
            raise ValueError('Invalid class_name.')
        if not hasattr(self, 'name'):
            raise AttributeError('DPDelete() requires name')
        self.path = self._get_uri()
        self.method = 'DELETE'

    def _get_uri(self):
        if self.name:
            if self.obj_field:
                return DELETE_FIELD_URI.format(self.domain, self.class_name, self.name, self.obj_field).rstrip('/')
            else:
                return DELETE_URI.format(self.domain, self.class_name, self.name).rstrip('/')
        else:
            raise AttributeError('DPDelete requires name to target a resouce.')


class DPCreate(DPRequest):
    def __init__(self, module):
        super(DPCreate, self).__init__(module)
        if is_valid_class(self.get_class_name()):
            self.class_name = self.get_class_name()
        self.path = CREATE_CONFIG_URI.format(self.domain, self.class_name)
        self.method = 'POST'


class DPAction(DPRequest):
    def __init__(self, module):
        super(DPAction, self).__init__(module)
        self.path = ACTION_QUEUE_URI.format(self.domain)
        self.method = 'POST'


class DPUploadFile(DPRequest):
    def __init__(self, module):
        super(DPUploadFile, self).__init__(module)  
        #self.path = '/mgmt/filestore/default/cert/demo.crt'
        self.path = FILESTORE_URI.format(self.domain, self.top_dir, self.file_path.strip('/'))
        self.body = self.build_body()
        if self.overwrite:
            self.method = 'PUT'
        else:
            self.method = 'POST'

    def build_body(self):
        return {
            'file': {
                'name': self.path.split('/')[-1],
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
        self.path = self._get_uri()
        self.method = 'POST'
        if list_type != 'All':
            dp_exports = DPExportList(
                self.body.get('Export').get(list_type)
            )._get_export_list()
            self.body['Export'][list_type] = dp_exports


    def _get_uri(self):
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