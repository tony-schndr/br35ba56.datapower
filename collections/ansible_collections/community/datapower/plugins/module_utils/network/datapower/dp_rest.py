from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.connection import Connection
from ansible.module_utils.network.datapower import (
    actionqueue,
    filestore,
    config,
)


GET_CONFIG_URI = '/mgmt/config/{0}/{1}' 
GET_CONFIG_NAME_URI = '/mgmt/config/{0}/{1}/{2}'
MOD_CONFIG_URI = '/mgmt/config/{0}/{1}/{2}'

def get_config(module):
    object_class = module.params['object_class']
    if module.params['name']:
        name = module.params['name']
        uri = GET_CONFIG_NAME_URI
    else:
        uri = GET_CONFIG_URI
    
    for domain in module.params['domains']:
        if module.params['name']:
            path = uri.format(domain, object_class, module.params['name'])
        else:
            path = uri.format(domain, object_class)
    connection = Connection(module._socket_path)
    
    results = connection.send_request(None, path=path, method="GET")
    return format_results(results)


def create_config(module):
    connection = Connection(module._socket_path)
    results = []
    for domain in module.params['domains']:
        for dict_ in module.params['definitions']:
            object_class = dict_.keys()[0]
            body = dict_
            path = '/mgmt/config/' + domain + '/' + object_class
            try:
                result = connection.send_request(body, path=path, method="POST")
                results.append(result)
            except Exception as e:
                results.append({"body": body,"path": path, "method": "POST"})               
            
    return format_results({'results': results})


def modify_config(module):
    connection = Connection(module._socket_path)
    results = []
    for domain in module.params['domains']:
        for dict_ in module.params['definitions']:
            object_class = dict_.keys()[0]
            body = dict_
            path = '/mgmt/config/' + domain + '/' + object_class + '/' + dict_[object_class]['name']
            try:
                result = connection.send_request(body, path=path, method="PUT")
                results.append(result)
            except Exception as e:
                results.append({"body": body,"path": path, "method": "PUT", "exception": e})               
            
    return format_results({'results': results})


def delete_config(module):
    if module.params['object_class'] in config.dp_objects:
        object_class = module.params['object_class']

    connection = Connection(module._socket_path)
    results = []
    for domain in module.params['domains']:
        path = '/mgmt/config/' + domain + '/' + object_class + '/' + module.params['name']
        results.append(connection.send_request(None, path=path, method="DELETE"))

    return format_results({'results': results})


def do_action(module):
    if module.params['action'] in dp_object_list.dp_objects:
        action = module.params['action']
   
    body = { 
            object_class: { 
                'name': module.params['name'] 
            }
    }
  
    connection = Connection(module._socket_path)
    results = []
    for domain in module.params['domains']:
        path = '/mgmt/actionqueue/' + domain + '/' + object_class 
        results.append(connection.send_request(body, path=path, method="POST"))
    return format_results({'results': results})


def format_results(dict_):
    dp_objects = []
    for key, value in dict_.items():
        if key != '_links' and key != '_embedded':
            app_dict = { key : value }
            dp_objects.append(app_dict)
    if '_embedded' in dict_.keys():
        for dp_object in dict_['_embedded']['descendants']:
            dp_objects.append(dp_object)
    _scrub(dp_objects, 'href')
    _scrub(dp_objects, '_links')
    return dp_objects


def _scrub(obj, bad_key):
    """
    Removes specified key from the dictioary in place.
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