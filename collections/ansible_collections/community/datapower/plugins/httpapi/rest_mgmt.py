# Copyright (c) 2018 Cisco and/or its affiliates.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
author: Anthony Schneider
httpapi: datapower
short_description: HttpApi Plugin for IBM DataPower
description:
- This HttpApi plugin provides methods to connect to IMB DataPower REST management interface.
version_added: 1.0.0
options:
  root_path:
    type: str
    description:
    - Specifies the location of the Restconf root.
    default: /restconf
    vars:
    - name: ansible_httpapi_restconf_root
"""

import json

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.plugins.httpapi import HttpApiBase


CONTENT_TYPE = "application/yang-data+json"


class HttpApi(HttpApiBase):
    def send_request(self, data, path, method):
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
    def get(self):
      return 'stuff'


def handle_response(response, response_data):
    try:
        response_data = json.loads(response_data.read())
    except ValueError:
        response_data = 'Invalid JSON returned from the DataPower REST management interface.'

    if isinstance(response, HTTPError):
        if response_data:
            response_err = []
            i = 0
            for error in response_data['error']:
                response_err.append({'Message-{0}'.format(i): to_text(error)})
                i = i + 1
            return {'error': { 'error_messages': response_err}}
    elif isinstance(response, URLError):
        raise ConnectionError(to_text(response_data))

    return {'data': response_data }