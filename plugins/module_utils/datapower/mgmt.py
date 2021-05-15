from __future__ import absolute_import, division, print_function
try:
    from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
        LocalFile,
        LocalDirectory
    )
except:
    from files import *
try:
    from ansible_collections.community.datapower.plugins.module_utils.datapower.classes import valid_objects
except:
    from classes import *
    
try:
    from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import DPFileStoreRequests
except:
    from DPFileStoreRequests import *
    

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
                raise ValueError('Invalid class_name or no class_name provided.')

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

    def __init__(self, domain: str, local_path: str, remote_path: str, content=None, request_handler=None):
        super().__init__(domain)
        self.local_file = LocalFile(local_path, content)
        self.top_directory = get_top_dir(remote_path)
        self.remote_path = get_dest_file_path(remote_path)
        self.request_handler = request_handler
    
    def get_remote_state(self):
        get_file_request = DPFileStoreRequests.get_file_request(
            domain=self.domain,
            top_directory=self.top_directory,
            file_path=self.remote_path
        )
        try:
            get_req_result = self.req_handler.process_request(*get_file_request)
        except ConnectionError as gfce:
            gfce_text = to_text(gfce)
            if 'Resource not found' in gfce_text:
                raise DPResourceNotFoundError(get_file_request.path)
            else:
                raise

        content = get_req_result['file']
        dp_file_path = get_req_result['_links']['self']['href'].split(domain, 1)[1]
        dp_file_local_path = WORK_DIR.rstrip('/') + os.sep + dp_file_path.lstrip('/')
        self.remote_state = DPFile(domain, local_path=dp_file_local_path, remote_path=dp_file_path, content=content)

        return get_req_result


class DPResourceNotFoundError(Exception):
    pass

def clean_dp_path(path):
    return path.rstrip('/').lstrip('/')

TOP_DIRS = ['local', 'cert', 'sharedcert']
def get_dest_file_path(dest):
    if len(dest.split('/')) == 2: #Accounts for creating a file at the root of a top_directory
        dest_file_path = dest.split('/')[-1] 
    elif len(dest.split('/')) > 2:
        dest_file_path = '/'.join(dest.split('/')[1:])
    else: # len < 2
        raise Exception('Must specify full file path in destination, ie local/full/path/to/file.txt')
    return dest_file_path


def get_top_dir(dest):
    top_dir = clean_dp_path(dest).split('/')[0]
    for dir_ in TOP_DIRS:
        if dir_ in top_dir:
            return dir_
    else:
        raise Exception(
            top_dir +' is an invalid top directory, must be one of ', ' '.join(TOP_DIRS)
        )


class DPDirectory():

    def __init__(self, dest):
        dir_path = dest.split('/')[1:-1]
        if dest.split('/')[0] != 'local':
            raise InvalidDPDirectoryException('Subdirectories are only valid in local/')
        else:
            root = dest.split('/')[0]

    @staticmethod
    def get_root_dir(path):
        if 'local' not in path:
            raise AttributeError('can only create local direct')
        else:
            return True


class InvalidDPDirectoryException(Exception):
    pass


if __name__ == '__main__':
    domain = 'default'
    file_path = '/Users/anthonyschneider/DEV/ansible-datapower-playbooks/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/test/to/GetStat/getCPU.js'
    lf = LocalFile(file_path)
    obj = DPFile(domain, content=lf.get_base64(), path='local/GetStat/getCPU.js')
    print(obj.__str__())
