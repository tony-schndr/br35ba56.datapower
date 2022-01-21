from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
author: Anthony Schneider
name: rest_mgmt
short_description: HttpApi Plugin for IBM DataPower
description:
- This HttpApi plugin provides methods to connect to IBM DataPower REST management interface.
version_added: 1.0.0
"""

from ansible.plugins.httpapi import HttpApiBase
from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.utils import (
    clean_dp_dict,
)
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils._text import to_text
from xml.sax.saxutils import unescape
import json
import time
from collections import OrderedDict
from ansible.utils.display import Display
ACTION_QUEUE_TIMEOUT = 300
TASK_COMPLETED_MESSAGES = [
    'Operation completed.',
    'completed',
    'processed',
    'processed-with-errors'
]

display = Display()


class HttpApi(HttpApiBase):

    def send_request(self, path, method, data):

        if data:
            clean_dp_dict(data)
            data = json.dumps(data)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response, response_data = self.connection.send(
            path, data, headers=headers, method=method
        )
        return handle_response(response, response_data)

    def info(self):
        results = {}
        results['action'] = self.mgmt_action_info()
        results['config'] = self.mgmt_config_info()
        results['status'] = self.mgmt_status_info()
        return results

    def execute_action(self, path, body):
        method = 'POST'

        body = reorder_name_key(body)
        resp = self.send_request(path, method, body)
        if is_action_completed(resp):
            return resp
        else:
            path = resp['_links']['location']['href']
            start_time = time.time()
            while not is_action_completed(resp):
                if (time.time() - start_time) > ACTION_QUEUE_TIMEOUT:
                    raise ActionQueueTimeoutError(
                        'Could not retrieve status within defined time out' + path)
                time.sleep(2)
                resp = self.send_request(path, 'GET', None)
        return resp

    def mgmt_config_info(self):
        path = '/mgmt/config/'
        response = self.send_request(path, 'GET', None)
        config = [k for k in response['_links'].keys() if k != 'self']
        return config

    def mgmt_status_info(self):
        path = '/mgmt/status/'
        response = self.send_request(path, 'GET', None)
        statuses = [k for k in response['_links'].keys() if k != 'self']
        return statuses

    def mgmt_action_info(self):
        path = '/mgmt/actionqueue/default/operations'
        response = self.send_request(path, 'GET', None)
        values = list(response['_links'].keys())
        values.remove('self')
        return values

    def get_resource_or_none(self, path):
        try:
            res = self.send_request(path, 'GET', None)
        except ConnectionError as ce:
            err = to_text(ce)
            if 'Resource not found' in err:
                return None
            else:
                raise ce
        return res


class ActionQueueTimeoutError(Exception):
    pass


def handle_response(response, response_data):

    try:
        # DataPower will sometimes return xml encoded strings, unescape
        # For example &amp is found in strings in AccessProfile and
        # ConfigDeploymentPolicy objects.
        response_data = json.loads(unescape(response_data.read().decode()))

    except ValueError:
        response_data = response_data.read()

    if isinstance(response, HTTPError):
        if response_data:
            if "errors" in response_data:
                errors = response_data["errors"]["error"]
                error_text = "\n".join(
                    (error["error-message"] for error in errors)
                )
            else:
                error_text = response_data

            raise ConnectionError(error_text, code=response.code)
        raise ConnectionError(to_text(response), code=response.code)

    return response_data


def is_action_completed(resp):
    for message in TASK_COMPLETED_MESSAGES:
        if message in to_text(resp):
            return True
    return False


def reorder_name_key(data):
    '''
    Recursively reorder the dictionary so the name key is always first.
    This is needed to workaround DataPower Rest MGMT Interface bug where
    the REST command will fail if the 'name' key is not the first key in
    the JSON body.  The bug has been found in the /mgmt/actionqueue endpoint
    for Export and LoadConfiguration.

    '''
    better_data = OrderedDict()

    def traverse(data, better_data):
        '''
        Recursively traverse a dictionary data structure and build an equivalent OrderedDict along the way.
        '''
        if 'name' in data:
            better_data['name'] = data['name']

        for k, v in data.items():
            if isinstance(v, dict):
                better_data[k] = OrderedDict()
                traverse(v, better_data[k])
            elif isinstance(v, list):
                better_data[k] = list()
                index = 0
                for elem in v:
                    if isinstance(elem, dict):
                        better_data[k].append(OrderedDict())
                        traverse(elem, better_data[k][index])
                    else:  # Don't need to traverse more as we assume everything in the list if of the same type.
                        better_data[k].append(elem)
                    index += 1
            else:
                if k != 'name':
                    better_data[k] = v

    traverse(data, better_data)
    return better_data
