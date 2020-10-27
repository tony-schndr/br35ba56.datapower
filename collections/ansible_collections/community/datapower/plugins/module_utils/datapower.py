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

class DPDomain():
    
    def __init__(self, module):
        if module.params.get('domain') is not None:
            self.domain = module.params.get('domain')
        else:
            raise AttributeError('Missing domain')
        if module.params['definition'] is not None:
            self.definition = module.params.get('definition')
            self.class_name = list(self.definition.keys())[0]
            if config.val_obj_dict['_links'].get(self.class_name) is None:
                raise ValueError('Invalid class_name, ref GET /mgmt/config/')
            if 'name' not in self.definition:
                raise AttributeError('missing name, ref GET /mgmt/config/')
        elif module.params['class_name'] is not None and module.params['name'] is not None:
            self.class_name = module.params['class_name']
            self.name = module.params['name']

        self.connection = Connection(module._socket_path)
    
    
    def _process_request(self, method, path, body):
        try:
            result = self.connection.send_request(body, path, method)
            _scrub(result, '_links')
        except ConnectionError as ce:
            return {'CONN_ERR': to_text(ce)}
        return result


    def execute_task(self):
        self._process_request(self.method, self.path, self.definition)
            

class DPCreate(DPDomain):
    def __init__(self, module):
        super(DPCreate, self).__init__(module)
        if module.params['definition'] is not None:
            self.definition = module.params.get('definition')
        else:
            raise AttributeError('Missing definition, ref GET /mgmt/config/')
        self.class_name = list(self.definition.keys())[0]
        if config.val_obj_dict['_links'].get(self.class_name) is None:
            raise ValueError('Invalid class_name, ref GET /mgmt/config/')
        self.path = CREATE_CONFIG_URI.format(self.domain, self.class_name)
        self.method = 'POST'


class DPModify(DPDomain):
    def __init__(self, module):
        super(DPModify, self).__init__(module)
        if module.params['definition'] is not None:
            self.definition = module.params.get('definition')
        else:
            raise AttributeError('Missing definition, ref GET /mgmt/config/')
        self.class_name = list(self.definition.keys())[0]
        if config.val_obj_dict['_links'].get(self.class_name) is None:
            raise ValueError('Invalid class_name, ref GET /mgmt/config/')
        if 'name' not in self.definition:
            raise AttributeError('missing name, ref GET /mgmt/config/')
        self.name = self.definition.get('class_name').get('name')
        self.path = MODIFY_URI.format(self.domain, self.class_name, self.name)
        self.method = 'POST'

class DPDelete(DPDomain):
    def __init__(self, module):
        super(DPDelete, self).__init__(module)
        if module.params['class_name'] is not None:
            if config.val_obj_dict['_links'].get(self.class_name) is None:
                raise ValueError('Invalid class_name, ref GET /mgmt/config/')
            
        else:
            raise AttributeError('Missing class_name, ref GET /mgmt/config/')
        self.class_name = module.params['class_name']
        

        
        self.path = DELETE_URI.format(self.domain, self.class_name, self.name)
        self.method = 'DELETE'

class DPAction(DPDomain):
    def __init__(self, module):
        super(DPAction self).__init__(module)





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