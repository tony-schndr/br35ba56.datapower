from __future__ import absolute_import, division, print_function
__metaclass__ = type

import random
import posixpath
import string
import base64
import hashlib
import os
from difflib import context_diff
from copy import deepcopy
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge
)
from ansible.module_utils.common.dict_transformations import (
    recursive_diff
)
from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.requests import (
    ConfigRequest,
    DirectoryRequest,
    FileRequest,
    join_path
)


PARAM_MAP = {
    # Export mapping
    'domains': 'Domain',
    'objects': 'Object',
    'format': 'Format',
    'ref_objects': 'ref-obj',
    'ref_files': 'ref-files',
    'include_debug': 'include-debug',
    'user_comment': 'UserComment',
    'all_files': 'AllFiles',
    'persisted': 'Persisted',
    'include_internal_files': 'IncludeInternalFiles',
    'deployment_policy': 'DeploymentPolicy',
    'overwrite_objects': 'OverwriteObjects',
    'overwrite_files': 'OverwriteFiles',
    'rewrite_local_ip': 'RewriteLocalIP'
}
EXCLUDED_KEYS = ['domain', 'dest', 'export_path']


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False


def create_file_from_base64(path, content):
    md5 = hashlib.md5()
    if not os.path.exists(os.path.dirname(path)) and os.path.dirname(path) != '':
        os.makedirs(os.path.dirname(path))

    with open(path, 'wb') as f:
        data = base64.b64decode(content)
        f.write(data)
        md5.update(data)
    return path, md5


def file_diff(from_data, to_data, full_path):
    if isinstance(from_data, bytes):
        from_str = from_data.decode('utf-8')
    else:
        from_str = from_data

    if isinstance(to_data, bytes):
        to_str = to_data.decode('utf-8')
    else:
        to_str = to_data

    from_lines = from_str.split('\n')
    to_lines = to_str.split('\n')

    return list(
        context_diff(
            a=from_lines,
            b=to_lines,
            fromfile='before: ' + full_path,
            tofile='after: ' + full_path,
            n=3
        )
    )


def convert_bool_to_on_or_off(parameters):
    for k, v in parameters.items():
        if isinstance(v, bool):
            if v:
                parameters[k] = 'on'
            else:
                parameters[k] = 'off'
    return parameters


def map_module_args_to_datapower_keys(parameters):
    mapped_keys = {}
    for key, value in parameters.items():
        if value and key not in EXCLUDED_KEYS:
            mapped_keys[PARAM_MAP[key]] = value
    return mapped_keys


def get_random_file_name(extension=''):
    letters = string.ascii_lowercase
    filename = ''.join(random.choice(letters)
                       for i in range(16)) + '.' + extension
    return filename


def class_name_from_config(config):
    if len(list(config.keys())) == 1:
        return list(config.keys())[0]
    else:
        raise Exception('Invalid configuration, expected to find json keypath class_name')


def name_from_config(config, class_name):
    if class_name in config:
        if 'name' in config[class_name]:
            return config[class_name]['name']
    raise Exception('Invalid configuration, expected to find json keypath class_name.name')


def ensure_config(module, domain, config, state):
    result = {}
    result['changed'] = False
    connection = Connection(module._socket_path)
    class_name = class_name_from_config(config)
    name = name_from_config(config, class_name)
    clean_dp_dict(config)  # Remove keys that aren't valid for configuration. (href, links, self, etc...)
    req = ConfigRequest()
    req.path = join_path(domain, class_name, name, base_path='/mgmt/config/')

    before = connection.get_resource_or_none(req.path)
    if before is not None:
        clean_dp_dict(before)
        diff = recursive_diff(before, config)
    else:
        diff = config
    result['before'] = before

    if module._diff:
        result['diff'] = diff

    # Determine the correct request to execute depending on desired state.
    request = None
    if state == 'merged':
        if before is None:
            req.body = config
            request = req.post
        elif diff and len(list(diff[1][class_name])) > 0:
            req.body = dict_merge(before, config)
            request = req.put
    elif state == 'replaced':
        if before is None:
            req.body = config
            request = req.post
        elif diff and len(list(diff[1][class_name])) > 0:
            req.body = config
            request = req.put
    elif state == 'deleted':
        if before is None:
            request = None
        else:
            request = req.delete

    if module.check_mode:
        if request:
            result['changed'] = True
        module.exit_json(**result)

    if request:
        try:
            response = connection.send_request(**request())
            result['config'] = connection.get_resource_or_none(req.path)
            clean_dp_dict(result['config'])
        except ConnectionError as e:
            err = to_text(e)
            result['request'] = request()
            result['error'] = err
            result['changed'] = False
            module.fail_json(msg=to_text(e), **result)

        result['response'] = response
        result['changed'] = True

    return result


def ensure_directory(module, domain, dir_path, state='present'):
    # Directory is a top_dir, nothing to ensure.
    diff = None
    result = {}
    result['changed'] = False

    if len(dir_path.split('/')) == 1:
        result = {}
        result['path'] = dir_path
        result['diff'] = {}
        return result

    connection = Connection(module._socket_path)
    dir_req = DirectoryRequest()
    dir_req.set_body(dir_path=dir_path)
    dir_req.set_path(domain=domain, dir_path=dir_path)
    dir_state = connection.get_resource_or_none(dir_req.path)

    if dir_state and state == 'present':
        result['path'] = dir_path
        diff = {}
        result['response'] = None
    elif dir_state is None and state == 'present':
        if not module.check_mode:
            resp = connection.send_request(**dir_req.post())
            result['response'] = resp
        result['changed'] = True
        diff = {'before': None, 'after': dir_path}
        result['path'] = dir_path
    elif dir_state and state == 'absent':
        if not module.check_mode:
            resp = connection.send_request(**dir_req.delete())
            result['response'] = resp
        diff = {'before': dir_path, 'after': None}
        result['changed'] = True
    elif dir_state is None and state == 'absent':
        diff = {'before': None, 'after': None}
        result['response'] = None

    if module._diff:
        result['diff'] = diff
    return result


def ensure_file(module, domain, file_path, data, state):
    result = {}
    result['changed'] = False
    connection = Connection(module._socket_path)
    parent_dir = posixpath.split(file_path)[0]
    top_dir = file_path.split('/')[0] or parent_dir  # Handles the case where the parent dir is also the root directory.
    diff = None

    # Ensure the parent directory is present before uploading file
    # If file state is 'absent' do nothing.
    if state != 'absent':
        result['directory'] = ensure_directory(module, domain, parent_dir)

    files = list_directory(
        module=module,
        domain=domain,
        dir_path=parent_dir
    )

    file_req = build_file_request(domain, file_path, data)

    if not has_file(files, file_path) and state == 'present':
        if not module.check_mode:
            file_create_resp = connection.send_request(**file_req.post())
            result['response'] = file_create_resp
            result['path'] = file_create_resp['_links']['location']['href']
        result['diff'] = {'before': None, 'after': file_path}
        result['changed'] = True

    elif has_file(files, file_path) and state == 'present':
        # Compare the files, can't compare cert/sharedcert.
        if 'sharecert' not in top_dir and 'cert' not in top_dir:
            resp = connection.get_resource_or_none(file_req.path)
            from_data = base64.b64decode(resp['file'])

            try:
                diff = file_diff(from_data, data, file_path,)
            except UnicodeDecodeError as e:
                # File seems to be binary
                diff = 'Not possible to compare a binary file.'

            # Compare md5, if data is different update the file
            to_md5 = hashlib.md5()
            to_md5.update(data)

            from_md5 = hashlib.md5()
            from_md5.update(from_data)
            if to_md5.hexdigest() != from_md5.hexdigest():
                if not module.check_mode:
                    update_resp = connection.send_request(**file_req.put())
                    result['response'] = update_resp
                result['changed'] = True

        # The requested file already exists in cert/shared cert
        # Not updating a file as there is no way to restore/backout
        # unless you have the original cert/key or secure backups.
        elif has_file(files, file_path):
            result['path'] = file_path
            result['msg'] = 'Files are in cert / sharedcert directories, not overwiting existing crypto files.'
            return result
        else:
            raise NotImplementedError("This condition was not expected, this is likely a bug.")
    elif not has_file(files, file_path) and state == 'absent':
        diff = {'before': None, 'after': None}
    elif has_file(files, file_path) and state == 'absent':
        diff = {'before': file_path, 'after': None}
        delete_resp = connection.send_request(**file_req.delete())
        result['changed'] = True
        result['response'] = delete_resp

    if module._diff:
        result['diff'] = diff

    return result


def build_file_request(domain, file_path, data):
    top_dir = file_path.split('/')[0] or posixpath.split(file_path)[0]

    if isBase64(data):
        data_base64 = data
    else:
        data_base64 = base64.b64encode(data).decode()

    file_req = FileRequest()
    # sharedcert is global and can only be used through the default domain.
    if 'sharedcert' in top_dir:
        file_req.set_path(domain='default', file_path=file_path)
    else:
        file_req.set_path(domain=domain, file_path=file_path)
    file_req.set_body(file_path=file_path, content=data_base64)
    return file_req


def has_file(files, file_path):
    file_hrefs = ['/'.join(file['href'].split('/')[4:]) for file in files]
    for href in file_hrefs:
        if file_path.strip('/') in href:
            return True
    return False


def list_directory(module, domain, dir_path):
    connection = Connection(module._socket_path)
    dir_req = DirectoryRequest()
    dir_req.set_path(domain=domain, dir_path=dir_path)

    dir_resp = connection.get_resource_or_none(dir_req.path)
    if dir_resp is None:
        return []
    data = dir_resp['filestore']['location']
    if 'file' in data and isinstance(data['file'], dict):
        return [data['file']]
    elif 'file' in data and isinstance(data['file'], list):
        return data['file']
    else:
        return []


def normalize_config_data(data):
    if 'No configuration retrieved.' in to_text(data):
        return None

    data = deepcopy(data)
    _scrub(data, '_links')
    _scrub(data, 'href')
    _scrub(data, 'state')

    if len(list(data.keys())) == 1:
        class_name = list(data.keys())[0]
    else:
        raise Exception('Could not parse class_name from data')
    configs = []
    if isinstance(data[class_name], list):
        for config in data[class_name]:
            configs.append({class_name: config})
    else:
        configs.append(data)

    return configs


def clean_dp_dict(dict_):
    _scrub(dict_, '_links')
    _scrub(dict_, 'href')
    _scrub(dict_, 'state')


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
