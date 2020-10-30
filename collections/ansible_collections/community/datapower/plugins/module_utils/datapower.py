from __future__ import absolute_import, division, print_function

__metaclass__ = type

#from urllib.parse import quote
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


def is_valid_class(class_name):
    return config.val_obj_dict['_links'].get(class_name) or False

# TODO  Should this stay here?  
def _body_has_name(body):
    return 'name' in  body.get(list(body.keys())[0])


class DPRequest():

    def __init__(self, module):
        self.module = module
        for k, v in module.params.items():
            setattr(self, k, v)
        self.connection = Connection(module._socket_path)
                

    def get_class_name(self):
        if hasattr(self, 'class_name'):
            return self.class_name
        elif hasattr(self, 'body'):
            return list(self.body.keys())[0]
        else:
            return None
            

    def _process_request(self, method, path, body):
        result = {}
        try:
            result['request_details'] = {'body': body, 'path': path, 'method': method,}
            result['request_result'] = self.connection.send_request(body, path, method)
        except ConnectionError as ce:
            return {'CONN_ERR': to_text(ce ), 'result': result}
        return result

    def _get_uri(self):
        pass


    def send_request(self):
        if hasattr(self, 'body'):
            return self._process_request(self.method, self.path, self.body)
        else:
            return self._process_request(self.method, self.path, None)
            



class DPExportDomain():

    def __init__(self):
        pass


class DPExportObject():

    def __init__(self, objects):
        for obj in objects:
            for k,v in obj.items():
                # Need a couple strips here to accomadate for - and _ in python code.
                # Keys need to match DP REST interface.
                obj[k.replace('_', '-').strip('_').strip('-')] = v
                del obj[k]
        self.objects = objects

    def _get_export_list(self):
        return self.objects



class DPExportAll():

    def __init__(self):
        pass

class DPExport(DPRequest):

    def __init__(self, module):
        super(DPExport, self).__init__(module)
        if self.body.get('Export').get('Domain') and self.body.get('Export').get('Object'):
            raise AttributeError('Domain and Object are mutually exclusive')
        self.path = self._get_uri()
        self.method = 'POST'
        dp_exports = []
        if self.body.get('Export').get('Domain'):
            self.dp_exports = DPExportAll(module.params.get('Export').get('Domain'))._get_export_list()
        elif self.body.get('Export').get('Object'):
            self.dp_exports = DPExportAll(module.params.get('Export').get('Object'))._get_export_list()

#       self.body.get('Export') = self.dp_exports


    def _get_uri(self):
        return ACTION_QUEUE_URI.format(self.domain)


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
                return GET_CONFIG_NAME_FIELD_URI.format(self.domain, self.class_name, self.name, self.obj_field) + '?' + opt_str
            else:
                return GET_CONFIG_NAME_URI.format(self.domain, self.class_name, self.name).rstrip('/') + '?' + opt_str
        else:
            return CREATE_CONFIG_URI.format(self.domain, self.class_name).rstrip('/') + '?' + opt_str

    
    def _get_options(self):
        url_params = {}
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


class DPModify(DPRequest):
    def __init__(self, module):
        super(DPModify, self).__init__(module)
        if self.class_name and self.name and self.obj_field:
            pass
        elif _body_has_name(self.body):
             self.name = self.body.get(self.get_class_name()).get('name')
        else:
            raise AttributeError('DPModify miscombination, if your targeting the object, body is all you need.  If your targeting a list property in an object, you need to pass class_name, name and obj_field')
        if is_valid_class(self.get_class_name()):
            self.class_name = self.get_class_name()
        self.path = self._get_uri()
        #self.method = 'PUT'


    def _get_uri(self):
        if self.obj_field:
            self.method = 'POST'
            return MOD_CONFIG_FIELD_URI.format(self.domain, self.class_name, self.name, self.obj_field)
        else:
            self.method = 'PUT'
            return MOD_CONFIG_URI.format(self.domain, self.class_name, self.name)


class DPAction(DPRequest):
    def __init__(self, module):
        super(DPAction, self).__init__(module)
        self.path = ACTION_QUEUE_URI.format(self.domain)
        self.method = 'POST'


class DPUploadFile(DPRequest):
    def __init__(self, module):
        super(DPUploadFile, self).__init__(module)
        if self.dir == '/':
            self.path = FILESTORE_URI.format(self.domain, self.top_dir, "").rstrip('/')
        else:
            self.path = FILESTORE_URI.format(self.domain, self.top_dir, self.dir).rstrip('/')
        if self.overwrite:
            self.method = 'PUT'
        else:
            self.method = 'POST'


def _scrub(obj, bad_key):
    """
    Removes specified key from the dictioary in place.
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