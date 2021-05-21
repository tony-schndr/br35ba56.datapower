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
    from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import DPFileRequest
except:
    from DPFileRequest import *


__metaclass__ = type

TOP_DIRS = ['local', 'cert', 'sharedcert']



def is_valid_class(class_name):
    return class_name in valid_objects


class DPObject():
    def __init__(self, domain: str):
        self.domain = domain

    def __str__(self):
        return "domain: " + self.domain


class DPConfig(DPObject):

    # domain and class_name are the bare minimum required to get a valid
    # response from DataPower
    def __init__(self, domain, config=None, class_name=None, name=None):
        super(DPConfig, self).__init__(domain)
        self.set_class_name(class_name, config)
        self.set_name(name, config)
        self.set_config(config)

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



class DPActionQueue(DPObject):
    def __init__(self, domain, action, parameters=None):
        super(DPActionQueue, self).__init__(domain)
        self.action = action
        self.parameters = parameters


class DPFile(DPObject):

    def __init__(self, domain: str, local_path: str, remote_path: str, content=None, connection=None):
        super(DPFile, self).__init__(domain)
        self.local_file = LocalFile(local_path, content)
        self.top_directory = get_top_dir(remote_path)
        self.remote_path = get_dest_file_path(remote_path)
        self.connection = connection
    
    def get_remote_state(self):
        get_file_request = DPFileRequest.get_file_request(
            domain=self.domain,
            top_directory=self.top_directory,
            file_path=self.remote_path
        )
        try:
            get_req_result = self.connection(*get_file_request)
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


class DPDirectory(DPObject):

    def __init__(self, domain, dest):
        super(DPFile, self).__init__(domain)
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


class DPResourceNotFoundError(Exception):
    pass


def clean_dp_path(path):
    return path.rstrip('/').lstrip('/')


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


class InvalidDPDirectoryException(Exception):
    pass


if __name__ == '__main__':
    domain = 'default'
    file_path = '/Users/anthonyschneider/DEV/ansible-datapower-playbooks/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/test/to/GetStat/getCPU.js'
    lf = LocalFile(file_path)
    obj = DPFile(domain, content=lf.get_base64(), path='local/GetStat/getCPU.js')
    print(obj.__str__())
