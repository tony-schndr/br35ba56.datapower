from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import time
import posixpath
from xml.sax.saxutils import unescape
from ansible.module_utils._text import to_text
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


def join_path(*args, base_path=None):
    ''' Join the path to form the full URI
    args -- list to join with base path, composes the right half of the URI
    base_path -- string representing the base uri of the rest mgmt interface call, ie /mgmt/config/
    '''
    if not base_path:
        raise ValueError(NO_BASE_PATH_ERROR)
    path = '/'.join([arg for arg in args if arg is not None]).rstrip('/')
    return posixpath.join(base_path, path)


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

    def set_body(self, **kwargs):
        self.body = kwargs.get('body', None)

    def set_path(self, **kwargs):
        self.path = kwargs.get('path', None)

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

    def put(self):
        method = 'PUT'
        return self._process_request(self.path, method, self.body)

    def get(self):
        method = 'GET'
        return self._process_request(self.path, method, None)

    def delete(self):
        method = 'DELETE'
        return self._process_request(self.path, method, None)

    def post(self):
        method = 'POST'
        return self._process_request(self.path, method, self.body)


class DirectoryRequest(Request):
    # Override super init till all request classes are finished.
    def __init__(self):
        pass

    def set_path(self, **kwargs):
        domain = kwargs['domain']
        dir_path = kwargs['dir_path'].strip('/')
        self.path = join_path(
            domain,
            dir_path,
            base_path='/mgmt/filestore/'
        )

    def set_body(self, **kwargs):
        dir_path = kwargs['dir_path']
        # drop root directory
        if dir_path.split('/')[0] == 'local':
            dir_path = '/'.join(dir_path.split('/')[1:])
        self.body = {
            "directory": {
                "name": dir_path
            }
        }

    def post(self):
        method = 'POST'
        # Equates to /mgmt/filestore/<domain>/<top_directory>
        path = '/'.join(self.path.split('/')[0:5])
        return {'path': path, 'method': method, 'data': self.body}

    def put(self):
        raise NotImplementedError('PUT for directories is not implemented')

    def get(self):
        method = 'GET'
        return {'path': self.path, 'method': method, 'data': None}

    def delete(self):
        method = 'DELETE'
        return {'path': self.path, 'method': method, 'data': None}


class FileRequest(Request):
    def __init__(self):
        pass

    def set_path(self, **kwargs):
        domain = kwargs['domain']
        file_path = kwargs['file_path'].strip('/')
        self.path = join_path(domain, file_path, base_path='/mgmt/filestore/')

    def set_body(self, **kwargs):
        file_path = kwargs['file_path']
        content = kwargs['content']
        file_name = posixpath.split(file_path)[1]
        self.body = {
            'file': {
                'name': file_name,
                'content': content
            }
        }

    def post(self):
        method = 'POST'
        path = posixpath.split(self.path)[0]
        return {'path': path, 'method': method, 'data': self.body}

    # The rest should be inherited from parent class.
    def put(self):
        method = 'PUT'
        return {'path': self.path, 'method': method, 'data': self.body}

    def get(self):
        method = 'GET'
        return {'path': self.path, 'method': method, 'data': None}

    def delete(self):
        method = 'DELETE'
        return {'path': self.path, 'method': method, 'data': None}


class ListConfigObjectsRequest(Request):
    # FIXME: Why is domain being passed and not used?
    def __init__(self, connection, domain='default'):
        super().__init__(connection)
        self.set_path(domain=domain)

    def set_path(self, **kwargs):
        domain = kwargs['domain']
        self.path = join_path(base_path='/mgmt/config/')


class ListActionsRequest(Request):
    def __init__(self, connection, domain='default'):
        super().__init__(connection)
        self.set_path(domain=domain)

    def set_path(self, **kwargs):
        domain = kwargs.get('domain', 'default')
        self.path = join_path(
            domain,
            'operations',
            base_path='/mgmt/actionqueue/'
        )


class ConfigRequest(Request):
    def __init__(self):
        self.options = None

    def set_path(self, **kwargs):
        self.path = join_path(
            kwargs.get('domain', None),
            kwargs.get('class_name', None),
            kwargs.get('name', None),
            kwargs.get('field', None),
            base_path='/mgmt/config/'
        )

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
        return {'path': path, 'method': method, 'data': None}

    def post(self):
        method = 'POST'
        # Equates to /mgmt/filestore/<domain>/<class_name>
        path = '/'.join(self.path.split('/')[0:5])
        return {'path': path, 'method': method, 'data': self.body}

    def put(self):
        method = 'PUT'
        return {'path': self.path, 'method': method, 'data': self.body}

    def delete(self):
        method = 'DELETE'
        return {'path': self.path, 'method': method, 'data': None}


class ConfigInfoRequest(Request):
    def __init__(self, connection):
        super().__init__(connection)

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
        super().__init__(connection)
        self.path = ACTION_QUEUE_SCHEMA_URI.format(domain, action_name)


class ActionQueueTimeoutError(Exception):
    pass


class ActionQueueRequest(Request):
    task_completed_messages = [
        'Operation completed.',
        'completed',
        'processed',
        'processed-with-errors'
    ]

    def __init__(self, connection, domain, action_name, parameters=None):
        super().__init__(connection)
        self.path = ACTION_QUEUE_URI.format(domain)

        if parameters:
            self.body = {action_name: parameters}
        else:
            self.body = {action_name: {}}

    def post(self):
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
                    raise ActionQueueTimeoutError(
                        'Could not retrieve status within defined time out' + path)
                time.sleep(2)
                resp = self._process_request(path, 'GET', None)
        return resp

    def is_completed(self, resp):
        for message in self.task_completed_messages:
            if message in to_text(resp):
                return True
        return False


class StatusRequest(Request):
    def __init__(self, connection, domain, status_name):
        super().__init__(connection)
        self.path = join_path(
            domain,
            status_name,
            base_path='/mgmt/status/'
        )


class ListStatusObjectsRequest(Request):
    def __init__(self, connection):
        super().__init__(connection)
        self.path = join_path(base_path='/mgmt/status/')


def get_request_func(req, before, after, state):
    if state == 'present':
        if before is None:
            return req.post
        elif before != after:
            return req.put
    elif before is None:
        return None
    else:
        return req.delete
