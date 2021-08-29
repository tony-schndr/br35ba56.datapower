from __future__ import absolute_import, division, print_function
__metaclass__ = type

import random
import string
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible_collections.community.datapower.plugins.module_utils.datapower.classes import valid_objects

PARAM_MAP = {
    #Export mapping
    'domains': 'Domain',
    'objects': 'Object',
    'format': 'Format',
    'ref_objects': 'ref-obj',
    'ref_files': 'ref-files',
    'include_debug':'include-debug',
    'user_comment': 'UserComment',
    'all_files': 'AllFiles',
    'persisted': 'Persisted',
    'include_internal_files': 'IncludeInternalFiles',
    'deployment_policy': 'DeploymentPolicy',
    'overwrite_objects': 'OverwriteObjects',
    'overwrite_files': 'OverwriteFiles',
    'rewrite_local_ip': 'RewriteLocalIP'
}

EXCLUDED_KEYS = ['domain',  'dest', 'export_path']

class Config():
    # domain and class_name are the bare minimum required to get a valid
    # response from DataPower
    def __init__(self, domain, config=None, class_name=None, name=None, field=None):
        self.domain = domain
        self.set_class_name(class_name, config)
        self.set_name(name, config)
        self.set_config(config)
        self.field = field

    def set_config(self, config=None):
        if not config:
            self.config = None
            return
        # This will build a valid body that will work for POST and PUT methods.
        if self.class_name in config:
            if self.name in config[self.class_name]:
                self.config = config
            else:
                config[self.class_name]['name'] = self.name
                self.config = config
        else:
            if self.name not in config:
                config['name'] = self.name
            self.config = {
                self.class_name: config
            }
    
    def set_options(self, options):
        self.options = options

    # Try to set class_name allowing for some flexibility
    # it can be set by specifying it as class_name
    # or within the config dictionary
    def set_class_name(self, class_name=None, config=None):
        if class_name and is_valid_class(class_name):
            self.class_name = class_name
        elif config and is_valid_class(list(config.keys())[0]):
            self.class_name = list(config.keys())[0]
        else:
            raise ValueError('Invalid class_name or no class_name provided.')

    # Try to set name, the module allows for some flexibility
    # it can be set by specifying it as name 
    # or within the config dictionary
    def set_name(self, name=None, config=None):
        if not name:
            if self.class_name in config:
                self.name = config.get(self.class_name).get('name')
            elif 'name' in self.config:
                self.name = config.get('name')
            else:
                raise AttributeError('name attribute is required.')
        else:
            self.name = name


# This is hardcoded, the response is from DataPower v 10.0.1.0.
# This should greatly improved by having it check at the beginning
# of module execution
def is_valid_class(class_name):
    return class_name in valid_objects


def get_remote_data(req):
    try:
        res = req.get()
    except ConnectionError as ce:
        err = to_text(ce)
        if 'Resource not found' in err:
            return None
        else:
            raise ce
    return res


def convert_bool_to_on_or_off(parameters):
    for k,v in parameters.items():
        if isinstance(v, bool):
            if v:
                parameters[k] = 'on'
            else:
                parameters[k] = 'off'
    return parameters


def map_module_args_to_datapower_keys(parameters):
    return {PARAM_MAP[key]: value for key, value in parameters.items() if value and key not in EXCLUDED_KEYS}


def get_random_file_name(extension=''):
    letters = string.ascii_lowercase
    filename =  ''.join(random.choice(letters) for i in range(16)) + '.' + extension
    return filename