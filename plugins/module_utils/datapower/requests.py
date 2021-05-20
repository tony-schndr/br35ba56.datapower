from __future__ import absolute_import, division, print_function

__metaclass__ = type

#from urllib.parse import quote
import time
import base64
import json
import os
import posixpath
from xml.sax.saxutils import unescape
from ansible.module_utils.six.moves.urllib.parse import urlencode


MGMT_CONFIG_BASE_WITH_OBJECT_CLASS_URI = '/mgmt/config/{0}/{1}'
MGMT_CONFIG_WITH_NAME_URI = '/mgmt/config/{0}/{1}/{2}'
MGMT_CONFIG_WITH_FIELD_URI = '/mgmt/config/{0}/{1}/{2}/{3}'
MGMT_CONFIG_METADATA_URI = '/mgmt/metadata/{0}/{1}'
MGMT_CONFIG_URI = '/mgmt/config/'
ACTION_QUEUE_URI = '/mgmt/actionqueue/{0}'
ACTION_QUEUE_SCHEMA_URI = '/mgmt/actionqueue/{0}/operations/{1}?schema-format=datapower'
ACTION_QUEUE_OPERATIONS_URI = '/mgmt/actionqueue/{0}/operations'
ACTION_QUEUE_TIMEOUT = 300

VALID_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

URI_OPTIONS = {
    'recursive': {
        'view': 'recursive'
    },
    'state': {
        'state': 1
    },
    'depth': {
        'depth': 2
    }
}


NO_BASE_PATH_ERROR = 'Base path was not provided. ie /mgmt/config/'


class DPRequest:

    def __init__(self, connection):
        self.connection = connection
        self.body = None
        self.path = None
        self.method = None
        self.base_path = '/mgmt/'

    def _process_request(self, path, method, body=None):
        if body is not None:
            _scrub(body, '_links')
            _scrub(body, 'href')
            _scrub(body, 'state')
        try:
            resp = self.connection.send_request(path, method, body)
        except ConnectionError:
            raise
        resp_str = json.dumps(resp)
        # DataPower will sometimes return xml encoded strings, unescape
        # ie. &amp is found in strings in AccessProfile and ConfigDeploymentPolicy objects.
        data = json.loads(unescape(resp_str))
        return data

    def set_body(self, body):
        self.body = body

    def set_path(self, path):
        self.path = path

    @staticmethod
    def join_path(*args, base_path=None):
        ''' Join the path to form the full URI
        args -- list to join with base path, composes the right half of the URI
        base_path -- string representing the base uri of the rest mgmt interface call, ie /mgmt/config/
        '''
        if not base_path:
            raise ValueError(NO_BASE_PATH_ERROR)
        path = '/'.join([arg for arg in args if arg is not None]).rstrip('/')
        return posixpath.join(base_path, path)

    def update(self):
        method = 'PUT'
        return { 'path': self.path, 'method': method, 'body': self.body } 

    def get(self):
        method = 'GET'
        return { 'path': self.path, 'method': method, 'body': None } 

    def delete(self):
        method = 'DELETE'
        return { 'path': self.path, 'method': method, 'body': None } 

    def create(self):
        method = 'POST'
        return { 'path': self.path, 'method': method, 'body': self.body } 


class DPConfigRequest(DPRequest):

    def __init__(self, connection, domain, class_name, name=None, field=None, config=None):
        super(DPConfigRequest, self).__init__(connection)
        self.domain = domain
        self.class_name = class_name
        self.name = name
        self.path = self.join_path(domain, class_name, name, field, base_path='/mgmt/config/')
        self.set_body(config)

    def set_options(self, recursive=False, depth=3, state=False):
        options = {}

        if recursive:
            options['view'] = 'recursive'
            options['depth'] = depth
        if state:
            options['state'] = 1

        self.options = urlencode(options, doseq=0)


class DPConfigInfoRequest(DPRequest):
    
    def __init__(self, connection):
        super(DPConfigInfoRequest, self).__init__(connection)

    def config_info(self, domain='default', class_name=None):
        if class_name is None:
            path = MGMT_CONFIG_URI
        else:
            path = MGMT_CONFIG_METADATA_URI.format(domain, class_name)
        metadata = self.process_request(path, 'GET', body=None)
        if metadata['_links']['self']['href'] == MGMT_CONFIG_URI:
            metadata = list(metadata['_links'].keys())
            metadata.sort()
            metadata.remove('self')
            return metadata

        props = metadata['object']['properties']['property']
        types = self.get_types(props)

        return {'metadata': metadata, 'types': types}


class DPDirectoryRequest(DPRequest):

    base_path = '/mgmt/filestore'

    def __init__(self, connection, domain, top_directory, dir_path):
        super(DPDirectoryRequest, self).__init__(connection)
        self.domain = domain
        self.top_directory = top_directory
        self.dir_path = dir_path
        self.path = super().join_path(domain, top_directory,
                                      dir_path, base_path='/mgmt/filestore/')
        self.body = {
            "directory": {
                "name": dir_path
            }
        }

    def create(self):
        method = 'POST'
        path = super().join_path(self.domain, self.top_directory, base_path='/mgmt/filestore/')
        return{ 'path': path, 'method': method, 'body': self.body } 

    # PUT/POST have equivalent outcomes however have different implementions.
    # create/ update accomplish the same outcome, therefore use create()
    def update(self):
        raise NotImplementedError('Updates to directories are not implemented')


class DPFileRequest(DPRequest):
    base_path = '/mgmt/filestore/'
    def __init__(self, connection, domain, top_directory, file_path, content):
        super(DPFileRequest, self).__init__(connection)
        self.domain = domain
        self.top_directory = top_directory
        self.file_path = file_path
        self.content = content
        file_name = posixpath.split(file_path)[1]
        self.set_body(file_name, content)
        self.path = self.join_path(
            domain, top_directory, file_path, base_path='/mgmt/filestore/')

    def set_body(self, file_name, content):
        body = {
            'file': {
                'name': file_name,
                'content': content
            }
        }
        super().set_body(body)

    def create(self):
        method = 'POST'
        path = posixpath.split(self.path)[0]
        return { 'path': path, 'method': method, 'body': self.body } 


class ActionQueueTimeoutError(Exception):
    pass


class DPActionQueueRequest(DPRequest):

    def __init__(self, connection, dp_action):
        super(DPActionQueueRequest, self).__init__(connection)
        self.path = ACTION_QUEUE_URI.format(dp_action.domain)
        if hasattr(dp_action, 'parameters'):
            if dp_action.parameters is None:
                self.body = {dp_action.action: {}}
            else:
                self.body = {dp_action.action: dp_action.parameters}
        else:
            self.body = None
        self.method = 'POST'

    def _process_request(self, path, method, body=None):
        resp = super(DPActionQueueRequest, self).process_request(path, method, body)
        if self.is_completed(resp):
            return resp
        else:
            path = resp['_links']['location']['href']
            start_time = time.time()
            while not self.is_completed(resp):
                if (time.time() - start_time) > ACTION_QUEUE_TIMEOUT:
                    raise ActionQueueTimeoutError('Could not retrieve status within defined time out' + path)
                time.sleep(2)
                resp = super(DPActionQueueRequest, self).process_request(path, 'GET', None)     
        return resp

    def is_completed(self, resp):
        for k, v in resp.items():
            if v == 'Operation completed.' or v == 'completed':
                return True
        else:
            return False


class DPListActionsRequest(DPRequest):
    def __init__(self, dp_action):
        super(DPListActionsRequest, self).__init__()
        self.path = ACTION_QUEUE_OPERATIONS_URI.format(dp_action.domain)


class DPActionQueueSchemaRequest(DPRequest):
    def __init__(self, connection, dp_action):
        super(DPActionQueueSchemaRequest, self).__init__(connection)
        self.path = ACTION_QUEUE_SCHEMA_URI.format(
            dp_action.domain, dp_action.action)


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


def clean_dp_dict(dict_):
    _scrub(dict_, '_links')
    _scrub(dict_, 'href')
    _scrub(dict_, 'state')


if __name__ == '__main__':
    domain = 'default'
    top_directory = 'local'
    file_path = 'dir/subdir/get.js'
    content = 'aGVsbG8gd29ybGQK'
    req = DPFileRequest.update_file_request(
        domain, top_directory, file_path, content)
    print(req == ('/mgmt/filestore/default/local/dir/subdir/get.js',
          'PUT', {'file': {'name': 'get.js', 'content': content}}))
