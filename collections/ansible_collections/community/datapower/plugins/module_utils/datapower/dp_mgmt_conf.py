from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    config
)


# This is hardcoded, pinned to DataPower v 10.0.1.0.
# This could be greatly improved by having it check an AnsibleFact.
# Would need to add a fact Module that gathers valid config object types
# from GET /mgmt/config/ and store it as a fact.
def is_valid_class(class_name):
    return config.val_obj_dict['_links'].get(class_name) or False

class DPManageConfigObject:
    # domain and class_name are the bare minimum required to get a valid
    # response from DataPower
    # kwargs consisting of the arguments defined in the Ansible Modules
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)
        # If class_name not specified try to set it 
        # from config
        if not hasattr(self, 'class_name'):
            self.class_name = list(self.config.keys())[0]
            if not is_valid_class(self.class_name):
                raise ValueError('Invalid class_name or no class_name provided.')

        if not hasattr(self, 'name'):
            if self.class_name in self.config:
                self.name = self.config.get(self.class_name).get('name', None)
            elif 'name' in self.config:
                self.name = self.config.get('name')
            else:
                raise AttributeError('name attribute is required.')
            
        if not hasattr(self, 'domain'):
            raise AttributeError('missing domain')

        if not hasattr(self,'config'):
            raise AttributeError('missing config')

class DPManageConfigSchema:
    
    def __init__(self, schema_resp):
        self.set_props(schema_resp)

    def get_prop(self, field):
        for prop in self.props:
            if prop.name == field:
                return prop
        else:
            return None

    # Create a property array to store the property objects, these are retrieved from the METADATA_URI
    # and store useful data like name of the feild, type, and if its an array or not.
    def set_props(self, schema_resp):
        self.props = []
        for dp_prop in schema_resp['object']['properties']['property']:
            prop = DPProperty()
            for k,v in dp_prop.items():
                if k == 'array':
                    if v == 'true':
                        setattr(prop, k, True)
                    else:
                        setattr(prop, k, False)
                else:
                    setattr(prop, k, v)
                self.props.append(prop)
            
class DPProperty:
    pass