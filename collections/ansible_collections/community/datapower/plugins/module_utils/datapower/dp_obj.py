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
                raise ValueError('Invalid class_name.')

        if not hasattr(self, 'object_name'):
            self.object_name = self.config.get(self.class_name).get('name', None)
    

