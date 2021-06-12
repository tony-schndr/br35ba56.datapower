from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import time
import posixpath
from xml.sax.saxutils import unescape
from ansible.module_utils.six.moves.urllib.parse import urlencode


MGMT_CONFIG_METADATA_URI = '/mgmt/metadata/{0}/{1}'
MGMT_CONFIG_URI = '/mgmt/config/'
ACTION_QUEUE_URI = '/mgmt/actionqueue/{0}'
ACTION_QUEUE_SCHEMA_URI = '/mgmt/actionqueue/{0}/operations/{1}?schema-format=datapower'
ACTION_QUEUE_OPERATIONS_URI = '/mgmt/actionqueue/{0}/operations'
ACTION_QUEUE_TIMEOUT = 300

NO_BASE_PATH_ERROR = 'Base path was not provided. ie /mgmt/config/'



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


class Request:

    def __init__(self, connection):
        self.connection = connection
        self.body = None
        self.path = None
        self.method = None

    def _process_request(self, path, method, body=None):
        if body:
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
        return self._process_request(self.path, method, self.body)

    def get(self):
        method = 'GET'
        return self._process_request(self.path, method, None)

    def delete(self):
        method = 'DELETE'
        return self._process_request(self.path, method, None)

    def create(self):
        method = 'POST'
        return self._process_request(self.path, method, self.body)


class DirectoryRequest(Request):

    base_path = '/mgmt/filestore'

    def __init__(self, connection):
        super(DirectoryRequest, self).__init__(connection)

    def set_path(self, domain, dir_path):
        self.path = self.join_path(domain, dir_path, base_path='/mgmt/filestore/')

    def set_body(self, dir_path):
        self.body = {
            "directory": {
                "name": dir_path
            }
        }

    def create(self):
        method = 'POST'
        # Equates to /mgmt/filestore/<domain>/<top_directory>
        path = '/'.join(self.path.split('/')[0:5])
        return self._process_request(path, method, self.body)

    # PUT/POST have equivalent outcomes however have different implementions.
    # create/ update accomplish the same outcome, therefore use create()
    def update(self):
        raise NotImplementedError('Updates to directories are not implemented')


class FileRequest(Request):

    def __init__(self, connection):
        super(FileRequest, self).__init__(connection)

    def set_path(self, domain, file_path):
        self.path = self.join_path(
            domain, file_path, base_path='/mgmt/filestore/')

    def set_body(self, file_path, content):
        file_name = posixpath.split(file_path)[1]
        self.body = {
            'file': {
                'name': file_name,
                'content': content
            }
        }

    # path for creating files is always targeted at the parent directory
    def create(self):
        method = 'POST'
        path = posixpath.split(self.path)[0]
        return self._process_request(path, method, self.body)


class ListConfigObjectsRequest(Request):
    def __init__(self, connection, domain='default'):
        super(ListConfigObjectsRequest, self).__init__(connection)
        self.set_path(domain)

    def set_path(self, domain='default'):
        self.path = self.join_path(base_path='/mgmt/config/')
    
    def get(self):
        return self._process_request(self.path, 'GET', None)


class ListActionsRequest(Request):
    def __init__(self, connection, domain='default'):
        super(ListActionsRequest, self).__init__(connection)
        self.set_path(domain)

    def set_path(self, domain='default'):
        self.path = self.join_path(domain, base_path='/mgmt/actionqueue/')
    
    def get(self):
        return self._process_request(self.path, 'GET', None)


class ConfigRequest(Request):

    def __init__(self, connection):
        super(ConfigRequest, self).__init__(connection)
        self.options = None
    
    def set_path(self, domain=None, class_name=None,  name=None, field=None):
        self.path = self.join_path(domain, class_name, name, field, base_path='/mgmt/config/')

    def set_options(self, recursive=False, depth=3, status=False):
        options = {}

        if recursive:
            options['view'] = 'recursive'
            if depth:
                options['depth'] = depth
            else:
                options['depth'] = 3
        
        if status:
            options['state'] = 1

        self.options = urlencode(options, doseq=0)

    def get(self):
        method = 'GET'
        if self.options:
            path = self.path + '?' + self.options
        else: 
            path = self.path
        return self._process_request(path, method, None)

    def create(self):
        method = 'POST'
        # Equates to /mgmt/filestore/<domain>/<class_name>
        path = '/'.join(self.path.split('/')[0:5])
        return self._process_request(path, method, self.body)

# 
class ConfigInfoRequest(Request):

    def __init__(self, connection):
        super(ConfigInfoRequest, self).__init__(connection)

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


class ActionQueueSchemaRequest(Request):
    def __init__(self, connection, domain, action_name):
        super(ActionQueueSchemaRequest, self).__init__(connection)
        self.path = ACTION_QUEUE_SCHEMA_URI.format(domain, action_name)

    def get(self):
        return self._process_request(self.path, 'GET', None)


class ActionQueueTimeoutError(Exception):
    pass


class ActionQueueRequest(Request):
    def __init__(self, connection, domain, action_name, parameters=None):
        super(ActionQueueRequest, self).__init__(connection)
        self.path = ACTION_QUEUE_URI.format(domain)
        
        if parameters:
            self.body = { action_name : parameters }
        else:
            self.body = { action_name : {} }

    def create(self):
        path = self.path
        body = self.body
        method = 'POST'
        resp = self._process_request(path, method, body)
        if self.is_completed(resp):
            return resp
        else:
            path = resp['_links']['location']['href']
            start_time = time.time()
            while not self.is_completed(resp):
                if (time.time() - start_time) > ACTION_QUEUE_TIMEOUT:
                    raise ActionQueueTimeoutError('Could not retrieve status within defined time out' + path)
                time.sleep(2)
                resp = self._process_request(path, 'GET', None)     
        return resp

    def is_completed(self, resp):
        for k, v in resp.items():
            if v == 'Operation completed.' or v == 'completed' or v == 'processed' or v == 'processed-with-errors':
                return True
        else:
            return False
