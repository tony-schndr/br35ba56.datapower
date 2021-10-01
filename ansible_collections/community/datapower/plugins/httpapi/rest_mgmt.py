
from __future__ import absolute_import, division, print_function
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import MGMT_CONFIG_URI
from ansible.plugins.httpapi import HttpApiBase
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils._text import to_text
import json
import posixpath

__metaclass__ = type

DOCUMENTATION = """
author: Anthony Schneider
httpapi: datapower
short_description: HttpApi Plugin for IBM DataPower
description:
- This HttpApi plugin provides methods to connect to IBM DataPower REST management interface.
version_added: 1.0.0
"""
NO_BASE_PATH_ERROR = 'Base path was not provided. ie /mgmt/config/'

MGMT_CONFIG_URI = '/mgmt/config/'

class HttpApi(HttpApiBase):

    def send_request(self, path, method, data):
        if data:
            data = json.dumps(data)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response, response_data = self.connection.send(
            path, data, headers=headers, method=method
        )
        return handle_response(response, response_data)

    def edit_config(self, commands):
        for command in commands:
            self.send_request(**command)

    def get_config(self, domain, class_name):
        path = join_path(domain, class_name, base_path=MGMT_CONFIG_URI)
        return self.send_request(path, 'GET', None)



    # TODO: What capabilites should be returned from datapower?
    def get_capabilities(self):
        return '{"rest_mgmt" : ""}'


def join_path(*args, base_path=None):
    ''' Join the path to form the full URI
    args -- list to join with base path, composes the right half of the URI
    base_path -- string representing the base uri of the rest mgmt interface call, ie /mgmt/config/
    '''
    if not base_path:
        raise ValueError(NO_BASE_PATH_ERROR)
    path = '/'.join([arg for arg in args if arg is not None]).rstrip('/')
    return posixpath.join(base_path, path)

def handle_response(response, response_data):
    try:
        response_data = json.loads(response_data.read())

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



