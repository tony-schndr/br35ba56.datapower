from __future__ import absolute_import, division, print_function

__metaclass__ = type


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
MOD_CONFIG_URI = '/mgmt/config/{0}/{1}/{2}'
DELETE_URI = '/mgmt/config/{0}/{1}/{2}'
MODIFY_URI = '/mgmt/config/{0}/{1}/{2}'
CREATE_CONFIG_URI = '/mgmt/config/{0}/{1}'
ACTION_QUEUE_URI = '/mgmt/actionqueue/{0}'



def is_valid_class(class_name):
    return config.val_obj_dict['_links'].get(class_name) or False

def has_definition(module):
    return 'definition' in module.params
    


class DPDomain():

    def __init__(self, module):
        self.module = module
        if module.params.get('domain') is not None:
            self.domain = module.params.get('domain')
        else:
            raise AttributeError('Missing domain')
        if isinstance(self, DPAction):
            pass
        elif isinstance(self, DPCreate):
            self.init_definition()
        elif isinstance(self, DPModify):
            self.init_definition()
        elif isinstance(self, DPDelete):
            self.init_other()
        elif isinstance(self, DPGet):
            self.init_other()
        self.connection = Connection(module._socket_path)
    
    def init_other(self):
        if self.module.params['class_name'] is not None: 
            self.class_name = self.module.params['class_name']
        else:
            raise AttributeError('Missing class_name.')
        if self.module.params['name'] is not None:
            self.name = self.module.params['name']
        

    def init_action(self):
        if self.module.params['action']:
            self.action = self.module.params['action']


    def init_definition(self):
        if has_definition(self.module):
            self.definition = self.module.params.get('definition')
        if is_valid_class(list(self.definition.keys())[0]):
            self.class_name = list(self.definition.keys())[0]
        else:
            raise AttributeError('Missing class_name or Invalid class_name, ref GET /mgmt/config/')
        if 'name' in  self.definition.get(self.class_name):
            self.name = self.definition.get(self.class_name).get('name')
        else:
            raise AttributeError('missing name, ref GET /mgmt/config/')


    def _process_request(self, method, path, body):
        try:
            result = self.connection.send_request(body, path, method)
            result['request_details'] = {'body': body, 'path': path, 'method': method}
        except ConnectionError as ce:
            return {'CONN_ERR': to_text(ce)}
        return result


    def execute_task(self):
        if hasattr(self, 'definition'):
            return self._process_request(self.method, self.path, self.definition)
        else:
            return self._process_request(self.method, self.path, None)
            

class DPCreate(DPDomain):
    def __init__(self, module):
        super(DPCreate, self).__init__(module)
        self.path = CREATE_CONFIG_URI.format(self.domain, self.class_name)
        self.method = 'POST'


class DPGet(DPDomain):
    def __init__(self, module):
        super(DPGet, self).__init__(module)
        if hasattr(self, 'name'):
            self.path = GET_CONFIG_NAME_URI.format(self.domain, self.class_name, self.name)
        else:
            self.path = CREATE_CONFIG_URI.format(self.domain, self.class_name)
        self.method = 'GET'


class DPModify(DPDomain):
    def __init__(self, module):
        super(DPModify, self).__init__(module)
        self.path = MODIFY_URI.format(self.domain, self.class_name, self.name)
        self.method = 'PUT'


class DPDelete(DPDomain):
    def __init__(self, module):
        super(DPDelete, self).__init__(module)
        if hasattr(self, 'name'):
            self.path = DELETE_URI.format(self.domain, self.class_name, self.name)
        else: 
            raise AttributeError('DPDelete task requires name')
        self.method = 'DELETE'

class DPAction(DPDomain):
    def __init__(self, module):
        super(DPAction, self).__init__(module)
        self.path = ACTION_QUEUE_URI.format(self.domain)
        self.method = 'PUT'

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