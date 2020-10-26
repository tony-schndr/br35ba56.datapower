from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_text
from ansible_collections.community.datapower.plugins.module_utils import (
    actionqueue,
    filestore,
    config,
)

GET_CONFIG_URI = '/mgmt/config/{0}/{1}' 
GET_CONFIG_NAME_URI = '/mgmt/config/{0}/{1}/{2}'
MOD_CONFIG_URI = '/mgmt/config/{0}/{1}/{2}'
CREATE_CONFIG_URI = '/mgmt/config/{0}/{1}'
ACTION_QUEUE_URI = '/mgmt/actionqueue/{0}'
DELETE_URI = '/mgmt/config/{0}/{1}/{2}'
MODIFY_URI = '/mgmt/config/{0}/{1}/{2}'


def get_config(module):
    class_name = module.params['class_name']
    results = []
    for domain in module.params['domains']:
        if module.params['object_name']:
            path = GET_CONFIG_NAME_URI.format(domain, class_name, module.params['object_name'])
        else:
            path = GET_CONFIG_URI.format(domain, class_name)
            result = process_request(module, domain, None, path=path, method="GET")
            results.append(result)
    return results


def create_config(module):
    connection = Connection(module._socket_path)
    results = []
    for domain in module.params['domains']:
        for body in module.params['definitions']:
            class_name = dict_.keys()[0]
            path = CREATE_CONFIG_URI.format(domain, class_name)
            result = process_request(module, domain, body, path=path, method="POST")
        results.append(result)
    return results
            


def modify_config(module):
    results = []
    for domain in module.params['domains']:
        for body in module.params['definitions']:
            class_name = body.keys()[0]
            path = MODIFY_URI.format(domain, class_name, body[class_name]['name'])
            result = process_request(module, domain, body, path=path, method="PUT")
        results.append(result)
    return results


def delete_config(module):
    connection = Connection(module._socket_path)
    results = []
    for domain in module.params['domains']:
        path = DELETE_URI.format(domain, module.params['class_name'], module.params['object_name'])
        result = process_request(module, domain, None, path=path, method="DELETE")
        results.append(result)
    return results



def action(module):
    body = module.params['action']
    results = []
    for domain in module.params['domains']:
        path = ACTION_QUEUE_URI.format(domain)
        result = process_request(module, domain, body, path, method="POST")
        results.append(result)
    return results


def process_request(module, domain, body, path, method):
    try:
        connection = Connection(module._socket_path)
        result = connection.send_request(body, path, method)
        _scrub(result, '_links')
    except ConnectionError as ce:
        return {'Domain': domain, 'CONN_ERR': to_text(ce)}
    return result


def _format_config_results(dict_):
    dp_objects = []
    for key, value in dict_.items():
        if key != '_links' and key != '_embedded':
            app_dict = { key : value }
            dp_objects.append(app_dict)
    if '_embedded' in dict_.keys():
        for dp_object in dict_['_embedded']['descendants']:
            dp_objects.append(dp_object)
    _scrub(dp_objects, '_links')
    return dp_objects


def _format_action_results(dict_):
    dp_objects = []
    for key, value in dict_.items():
        if key != '_links' and key != '_embedded':
            app_dict = { key : value }
            dp_objects.append(app_dict)
    if '_embedded' in dict_.keys():
        for dp_object in dict_['_embedded']['descendants']:
            dp_objects.append(dp_object)
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