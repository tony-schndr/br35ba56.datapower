from __future__ import absolute_import, division, print_function

__metaclass__ = type

#from urllib.parse import quote
import time
import base64
from copy import copy
from ansible.module_utils.six.moves.urllib.parse import urlencode

MGMT_CONFIG_BASE_WITH_OBJECT_CLASS_URI = '/mgmt/config/{0}/{1}' 
MGMT_CONFIG_WITH_NAME_URI = '/mgmt/config/{0}/{1}/{2}'
MGMT_CONFIG_WITH_FIELD_URI = '/mgmt/config/{0}/{1}/{2}/{3}'
MGMT_CONFIG_METADATA_URI = '/mgmt/metadata/{0}/{1}'
MGMT_CONFIG_URI = '/mgmt/config/'
ACTION_QUEUE_URI = '/mgmt/actionqueue/{0}'
ACTION_QUEUE_SCHEMA_URI = '/mgmt/actionqueue/{0}/operations/{1}?schema-format=datapower'
ACTION_QUEUE_OPERATIONS_URI = '/mgmt/actionqueue/{0}/operations'
FILESTORE_URI_PATH = '/mgmt/filestore/{0}/{1}/{2}'
FILESTORE_URI_DIR = '/mgmt/filestore/{0}/{1}'

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

class DPRequest:
    def __init__(self):
        self.body = None
        self.path = None
        self.method = None


class DPFileStoreRequest(DPRequest):
    def __init__(self, fs):
        self.fs = fs

    @staticmethod
    def get_body(dir):
        return {
            "directory": {
                "name": dir
            }
        }

    def dir_reqs(self, method='GET'):
        for dir in self.fs.dirs():
            yield self.get_dir_path(self.fs.domain, self.fs.root_dir), method, self.get_body(dir)

    def file_reqs(self, method='GET'):
        for file in self.fs.files():
            path = FILESTORE_URI_PATH.format(self.fs.domain, self.fs.root_dir, file[0])
            body = {
                'file' : {
                    'name' : file[1],
                    'content' : file[2]
                }
            }
            yield path, method, body

    def file_req(self, method='GET'):
        path = FILESTORE_URI_PATH.format(self.fs.domain, self.fs.root_dir, self.fs.dest)
        body = {
            'file' : {
                'name' : self.fs.file_name,
                'content' : self.fs.content
            }
        }
        return path, method, body
        
    def get_dir_path(self, domain, root_dir):
        return FILESTORE_URI_DIR.format(domain, root_dir)

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
        if hasattr(dp_action, 'action') and dp_action.action is not None:
            self.info_path = ACTION_QUEUE_SCHEMA_URI.format(dp_action.domain, dp_action.action)
        else:
            self.info_path = ACTION_QUEUE_OPERATIONS_URI.format(dp_action.domain)


class DPManageConfigRequest(DPRequest):
     
    # Need to check against the objects schema to determine the correct method.
    # Only POST can be used against field Array Property to append a list item.
    # Appending to a list should also require overwrite being set to false as a 
    # put against a list results in the list being overwritten.
    def __init__(self, dp_mgmt_conf):
        super(DPManageConfigRequest, self).__init__()
        # At this time schema is only used to check if a DataPower object
        # field is an array.  This could be utilized further to validate
        # other or all portions of a object passed to ansible prior to the 
        # request to DataPower.
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
        #super(DPGetConfigRequest, self).__init__()
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
