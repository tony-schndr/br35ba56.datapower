from __future__ import absolute_import, division, print_function

__metaclass__ = type

#from urllib.parse import quote
import time
from copy import copy
from ansible.module_utils._text import to_text
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_text

MGMT_CONFIG_BASE_WITH_OBJECT_CLASS_URI = '/mgmt/config/{0}/{1}' 
MGMT_CONFIG_WITH_NAME_URI = '/mgmt/config/{0}/{1}/{2}'
MGMT_CONFIG_WITH_FIELD_URI = '/mgmt/config/{0}/{1}/{2}/{3}'
ACTION_QUEUE_URI = '/mgmt/actionqueue/{0}'
ACTION_QUEUE_SCHEMA_URI = '/mgmt/actionqueue/{0}/operations/{1}?schema-format=datapower'
ACTION_QUEUE_OPERATIONS_URI = '/mgmt/actionqueue/{0}/operations'
FILESTORE_URI_PUT = '/mgmt/filestore/{0}/{1}/{2}'
FILESTORE_URI_POST = '/mgmt/filestore/{0}/{1}'

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
        if dp_action.action is not None:
            self.info_path = ACTION_QUEUE_SCHEMA_URI.format(dp_action.domain, dp_action.action)
        else:
            self.info_path = ACTION_QUEUE_OPERATIONS_URI.format(dp_action.domain)

class DPManageConfigRequest(DPRequest):
     
    #Need to check against the object schema to determine the correct method.
    # Only POST can be used against field Array Property to append a list item.
    # Appending to a list should also require overwrite being set to false as a 
    # put against a list results in the list being overwritten.
    def __init__(self, dp_mgmt_conf, schema=None):
        super(DPManageConfigRequest, self).__init__()
        # At this time schema is only used to check if a DataPower object
        # field is an array.  This could be utilized further to validate
        # other or all portions of a object passed to ansible prior to the 
        # request to DataPower.
        self.schema = schema

        if self.schema and self.check_for_array(dp_mgmt_conf.config, dp_mgmt_conf.class_name):
            self.set_body_for_array_field(dp_mgmt_conf.config, dp_mgmt_conf.class_name)
            self.set_path(
                dp_mgmt_conf.domain,
                dp_mgmt_conf.class_name,
                dp_mgmt_conf.name,
                list(self.body.keys())[0]
            )
            #Sets array list update behaivior, POST appends, PUT overwrites.
            if dp_mgmt_conf.overwrite:
                self.method = 'PUT'
            else:
                self.method = 'POST'
        
        if dp_mgmt_conf.overwrite:
            self.method = 'PUT'
            self.set_path(
                dp_mgmt_conf.domain,
                dp_mgmt_conf.class_name,
                dp_mgmt_conf.name
            )
            self.set_body(dp_mgmt_conf)
        elif not dp_mgmt_conf.overwrite:
            self.method = 'POST'
            self.set_path(
                dp_mgmt_conf.domain,
                dp_mgmt_conf.class_name,
            )
            self.set_body(dp_mgmt_conf)
            #Need to ensure name is include for POST requests.
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

    def check_for_array(self, config, class_name):
        if class_name in config:
            if len(config[class_name]) == 2 and 'name' in config[class_name]:
                for k in list(config[class_name].keys()):
                    if k != 'name':
                        prop = self.schema.get_prop(k)
                        if hasattr(prop, 'array'):
                            return prop.array
                return False
            elif len(config[class_name]) == 1:
                k = list(config[class_name].keys())[0] 
                if k != 'name':
                    prop = self.schema.get_prop(k)
                    if hasattr(prop, 'array'):
                        return prop.array
                    else:
                        return False
                else:
                    return False
        if len(config.keys()) == 1:
            k = list(config.keys())[0] 
            prop = self.schema.get_prop(k)
            if hasattr(prop, 'array'):
                return prop.array
            else:
                return False
        
        return False

    def set_body_for_array_field(self, config, class_name):
        body = {}
        if class_name in config:
            body = copy(config.get(class_name))
        else:
            body = copy(config)
        if 'name' in body:
            del body['name']
        if len(list(body.keys())) != 1:
            raise AttributeError('If this error is thrown there may be a bug, at this point the body/config should only have 1 key in it.')
        self.body = body
   
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


'''
class DPAction(DPRequest):
    def __init__(self, module):
        super(DPAction, self).__init__(module)
        self.path = ACTION_QUEUE_URI.format(self.domain)
        self.method = 'POST'



class DPUploadFile(DPRequest):
    def __init__(self, module):
        super(DPUploadFile, self).__init__(module)  
        # Always strip /
        self.dir = self.dir.rstrip('/').lstrip('/')
        if self.overwrite:
            self.method = 'PUT'
            self.path = FILESTORE_URI_PUT.format(self.domain, self.dir, self.filename)
        else:
            self.method = 'POST'
            self.path = FILESTORE_URI_POST.format(self.domain, self.dir)
       
        self.body = {
            'file': {
                'name': self.filename,
                'content': self.content
            }
        }


class DPExportList:
    def __init__(self, objects):
        for obj in objects:
            for k, v in obj.items():
                if k == 'name' or k == 'class':
                    continue
                # Need a couple strips here to accommodate for - and _ in python code.
                # Keys need to match DP REST interface.
                obj[k.replace('_', '-')] = v
                del obj[k]
        self.objects = objects
    def _get_export_list(self):
        return self.objects


class DPConfigActions(DPRequest):

    def __init__(self, module):
        super(DPConfigActions, self).__init__(module)

    def _process_request(self, method, path, body):
        result = super(DPConfigActions, self)._process_request(method, path, body)
        export_path = None
        if result.get(RESPONSE_KEY).get('_links', None):
            export_path = result.get(RESPONSE_KEY)['_links']['location']['href']
        else:
            return result
        if export_path:
            while True:
                exp_res = super(DPConfigActions, self)._process_request('GET', export_path, body=None)
                if exp_res.get(RESPONSE_KEY)['status'] == 'completed':
                    return exp_res
                time.sleep(2)
        return result


class DPExport(DPConfigActions):

    def __init__(self, module):
        super(DPExport, self).__init__(module)
        if self.body.get('Export').get('Domain') and self.body.get('Export').get('Object'):
            raise AttributeError('Domain and Object are mutually exclusive')
        if self.body.get('Export').get('Domain', None):
            list_type = 'Domain'
        elif self.body.get('Export').get('Object', None):
            list_type = 'Object'
        else: 
            list_type = 'All'
        self.path = self.get_path()
        self.method = 'POST'
        if list_type != 'All':
            dp_exports = DPExportList(
                self.body.get('Export').get(list_type)
            )._get_export_list()
            self.body['Export'][list_type] = dp_exports


    def get_path(self):
        return ACTION_QUEUE_URI.format(self.domain)


class DPLoadConfig(DPConfigActions):

    def __init__(self, module):
        super(DPLoadConfig, self).__init__(module)
        self.path = ACTION_QUEUE_URI.format(self.domain)
        self.method = 'POST'
'''
