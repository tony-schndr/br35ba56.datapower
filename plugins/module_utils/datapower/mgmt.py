from __future__ import absolute_import, division, print_function
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    LocalFile,
    LocalDirectory,
    DirectoryComparitor,
    FileDiff
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.classes import valid_objects

__metaclass__ = type


class DPActionQueue():
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class DPGetConfigObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class DPManageConfigObject:
    # domain and class_name are the bare minimum required to get a valid
    # response from DataPower
    # kwargs consisting of the arguments defined in the Ansible Modules
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        # Try to set class_name, the module allows for some flexibility
        # it can be set by specifying it as class_name
        # or within the config dictionary
        if not hasattr(self, 'class_name') or self.class_name is None:
            self.class_name = list(self.config.keys())[0]
            if not is_valid_class(self.class_name):
                raise ValueError(
                    'Invalid class_name or no class_name provided.')

        # Try to set name, the module allows for some flexibility
        # it can be set by specifying it as name
        # or within the config dictionary
        if not hasattr(self, 'name') or self.name is None:
            if self.class_name in self.config:
                self.name = self.config.get(self.class_name).get('name')
            elif 'name' in self.config:
                self.name = self.config.get('name')
            else:
                raise AttributeError('name attribute is required.')

# This is hardcoded, the response is from DataPower v 10.0.1.0.
# This should greatly improved by having it check at the beginning
# of module execution


def is_valid_class(class_name):
    return class_name in valid_objects

# This is first attempt at creating these objects with inheritence, DPFile and DPDirectory.
# Dependent on success / value in doing this the above objects will follow suite.
# DPFile and DPDirectory are direct representations of all the attributes/parameters
# required to create a file / directory on DataPower's filesystem.


class DPObject():
    
    def __init__(self, domain: str):
        self.domain = domain

    def __str__(self):
        return "domain: " + self.domain


class DPFile(DPObject):

    def __init__(self, domain: str, content: str, path: str ):
        super().__init__(domain)
        self.content = content
        self.path = path


    def as_dict(self):
        pass

    def __str__(self):
        return "\n".join([super().__str__(), self.path, self.content])

class DPDirectory():
    pass


if __name__ == '__main__':
    domain = 'default'
    file_path = '/Users/anthonyschneider/DEV/ansible-datapower-playbooks/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/test/to/GetStat/getCPU.js'
    lf = LocalFile(file_path)
    obj = DPFile(domain, content=lf.get_base64(), path='local/GetStat/' )
    print(obj.__str__())
