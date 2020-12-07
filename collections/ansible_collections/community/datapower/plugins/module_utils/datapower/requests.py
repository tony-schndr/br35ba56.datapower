from __future__ import absolute_import, division, print_function

__metaclass__ = type

#from urllib.parse import quote
import time
from ansible.module_utils._text import to_text
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_text


MGMT_CONFIG_BASE_WITH_OBJECT_CLASS_URI = '/mgmt/config/{0}/{1}' 
MGMT_CONFIG_WITH_NAME_URI = '/mgmt/config/{0}/{1}/{2}'
MGMT_CONFIG_WITH_FIELD_URI = '/mgmt/config/{0}/{1}/{2}/{3}'
ACTION_QUEUE_URI = '/mgmt/actionqueue/{0}'
FILESTORE_URI_PUT = '/mgmt/filestore/{0}/{1}/{2}'
FILESTORE_URI_POST = '/mgmt/filestore/{0}/{1}'

# Define the keys that get returned to the modules.  
# REQUEST_DETAILS_KEY is helps for debugging.
RESPONSE_KEY = 'response'
REQUEST_DETAILS_KEY = 'request'
VALID_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

URI_OPTIONS = {
    'recursive' : {
        'view': True
    },
    'state' : {
        'state': 1
    },
    'depth': {
        'depth' : 2
    }
}


def _make_request(connection, method, path,  body=None):
    return connection.send_request(body, path, method)

   
def clean_dp_dict(dict_):
    _scrub(dict_, '_links')
    _scrub(dict_, 'href')
    _scrub(dict_, 'state')


class DPRequest:

    def __init__(self):
        pass




class DPManageConfigRequest(DPRequest):

    def __init__(self, dp_mgmt_conf):
        super(DPManageConfigRequest, self).__init__()
        self.body = {}
        if dp_mgmt_conf.overwrite and not dp_mgmt_conf.object_field:
            self.method = 'PUT'
            self.set_path(
                dp_mgmt_conf.domain,
                dp_mgmt_conf.class_name,
                dp_mgmt_conf.object_name
            )
            self.body = dp_mgmt_conf.config
        elif not dp_mgmt_conf.overwrite and not dp_mgmt_conf.object_field:
            self.method = 'POST'
            self.set_path(
                dp_mgmt_conf.domain,
                dp_mgmt_conf.class_name,
            )
            self.body.update(dp_mgmt_conf.config)
            #Need to ensure name is include for POST requests.
            self.body['name'] = dp_mgmt_conf.object_name
        elif dp_mgmt_conf.object_field: 
            self.method = 'PUT'
            self.set_path(
                dp_mgmt_conf.domain,
                dp_mgmt_conf.class_name,
                dp_mgmt_conf.object_name,
                dp_mgmt_conf.object_field
            )
            self.body.update(dp_mgmt_conf.config)
        


    def set_path(self, domain, class_name=None, object_name=None, object_field=None):
        if class_name and not object_name and not object_field:
            self.path = MGMT_CONFIG_BASE_WITH_OBJECT_CLASS_URI.format(domain, class_name)
        elif class_name and object_name and not object_field:
            self.path = MGMT_CONFIG_WITH_NAME_URI.format(domain, class_name, object_name)
        elif class_name and object_name and object_field:
            self.path = MGMT_CONFIG_WITH_FIELD_URI.format(domain, class_name, object_name, object_field)
        else:
            raise AttributeError('no valid URI could be derived')


class DPGetConfigRequest(DPManageConfigRequest):
    def __init__(self, dp_mgmt_conf):
        super(DPGetConfigRequest, self).__init__(dp_mgmt_conf)
        self.method = 'GET'
        self.options = {}
        if hasattr(dp_mgmt_conf, 'recursive') and dp_mgmt_conf.recursive:
            self.options.update(URI_OPTIONS['recursive'])
            self.options.update(URI_OPTIONS['depth'])
        if hasattr(dp_mgmt_conf, 'state') and dp_mgmt_conf.state:
            self.options.update(URI_OPTIONS['state'])
        if hasattr(dp_mgmt_conf, 'depth') and dp_mgmt_conf.depth:
            self.options['depth'] = dp_mgmt_conf.depth
        self.path = self.path + '?' + urlencode(self.options, doseq=0)

    def get_path(self, **kwargs):
        return self.path + '?' + urlencode(self.options, doseq=0)



class DPDeleteConfig(DPManageConfigRequest):
    
    def __init__(self, module):
        super(DPDelete, self).__init__(module)
        self.set_path()
        self.set_method('DELETE')


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
