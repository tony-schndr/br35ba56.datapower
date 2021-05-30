from __future__ import absolute_import, division, print_function

__metaclass__ = type

#from urllib.parse import quote
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

VALID_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

URI_OPTIONS = {
    'recursive' : {
        'view': 'recursive'
    },
    'state' : {
        'state': 1
    },
    'depth': {
        'depth' : 2
    }
}

def join_filestore_path(*args):
    file_path = '/'.join(args).rstrip('/')
    return posixpath.join('/mgmt/filestore/', file_path)

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



class Request:

    def __init__(self, connection):
        self.connection = connection
        self.body = None
        self.path = None
        self.method = None

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
    base_path = '/mgmt/filestore/'

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
        self.path = self.join_path(domain, base_path='/mgmt/filestore/')
    
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
                depth = 3
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



class DPRequest:
    def __init__(self):
        self.body = None
        self.path = None
        self.method = None



class DPActionQueueRequest(DPRequest):
    def __init__(self, dp_action):
        super(DPActionQueueRequest, self).__init__()
        self.path = ACTION_QUEUE_URI.format(dp_action.domain)
        if hasattr(dp_action, 'parameters'):
            if dp_action.parameters is None:
                self.body = { dp_action.action : {} }
            else:
                 self.body = { dp_action.action : dp_action.parameters }
        else:
            self.body = None
        self.method = 'POST'  


class DPListActionsRequest(DPRequest):
    def __init__(self, dp_action):
        super(DPListActionsRequest, self).__init__()
        self.method = 'GET'
        self.path = ACTION_QUEUE_OPERATIONS_URI.format(dp_action.domain)


class DPActionQueueSchemaRequest(DPRequest):
    def __init__(self, dp_action):
        super(DPActionQueueSchemaRequest, self).__init__()
        self.method = 'GET'
        self.path = ACTION_QUEUE_SCHEMA_URI.format(dp_action.domain, dp_action.action)


class DPManageConfigRequest(DPRequest):

    def __init__(self, dp_mgmt_conf):
        super(DPManageConfigRequest, self).__init__()
        if dp_mgmt_conf.state == 'present':
            self.method = 'PUT'
            self.set_path(
                dp_mgmt_conf.domain,
                dp_mgmt_conf.class_name,
                dp_mgmt_conf.name
            )
            self.set_body(dp_mgmt_conf)
        elif dp_mgmt_conf.state == 'absent':
            self.method = 'DELETE'
            self.set_path(
                dp_mgmt_conf.domain,
                dp_mgmt_conf.class_name,
                dp_mgmt_conf.name
            )
        else:
            raise AttributeError('Could not build request object from parsed module parameters.')

    def set_body(self, dp_mgmt_conf):
        # For all requests except for array updates, use this to build a valid body that will work for 
        # POST and PUT methods.
        if dp_mgmt_conf.class_name in dp_mgmt_conf.config:
            if dp_mgmt_conf.name in dp_mgmt_conf.config[dp_mgmt_conf.class_name]:
                self.body = dp_mgmt_conf.config
            else:
                dp_mgmt_conf.config[dp_mgmt_conf.class_name]['name'] = dp_mgmt_conf.name
                self.body = dp_mgmt_conf.config
        else:
            if dp_mgmt_conf.name not in dp_mgmt_conf.config:
                dp_mgmt_conf.config['name'] = dp_mgmt_conf.name
            self.body = {
                dp_mgmt_conf.class_name: dp_mgmt_conf.config
            }

    def set_path(self, domain, class_name=None, name=None, field=None):
        if class_name and not name and not field:
            self.path = MGMT_CONFIG_BASE_WITH_OBJECT_CLASS_URI.format(domain, class_name)
        elif class_name and name and not field:
            self.path = MGMT_CONFIG_WITH_NAME_URI.format(domain, class_name, name)
        elif class_name and name and field:
            self.path = MGMT_CONFIG_WITH_FIELD_URI.format(domain, class_name, name, field)
        else:
            raise AttributeError('no valid URI could be derived')


class DPGetConfigRequest(DPManageConfigRequest):
    def __init__(self, dp_mgmt_conf):
       # super(DPGetConfigRequest, self).__init__()
        self.body = None
        self.method = 'GET'
        self.options = {}
        self.set_path(
            dp_mgmt_conf.domain,
            dp_mgmt_conf.class_name,
            dp_mgmt_conf.name
        )
        
        if hasattr(dp_mgmt_conf, 'recursive') and dp_mgmt_conf.recursive:
            self.options.update(URI_OPTIONS['recursive'])
            self.options.update(URI_OPTIONS['depth'])
        if hasattr(dp_mgmt_conf, 'status') and dp_mgmt_conf.status:
            self.options.update(URI_OPTIONS['state'])
        if hasattr(dp_mgmt_conf, 'depth') and dp_mgmt_conf.depth:
            self.options['depth'] = dp_mgmt_conf.depth
        self.path = self.path + '?' + urlencode(self.options, doseq=0)


