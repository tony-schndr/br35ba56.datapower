#!/usr/bin/env python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.get_actions

short_description: Get a list of actions available to the REST Management Interface.
                   This does not necessarily mean that action is supported on your 
                   DataPower platform / firmware version


version_added: "1.0.0"

description: Use for getting a list of actions available to the REST Management Interface.
             You could then pull that list and get the actions schema so you can format a 
             task to execute that action on DataPower

options:
    domain:
        description: domain to get actions from
        required: true
        type: str

author:
    - Anthony Schneider
'''

EXAMPLES = r'''
- name: Get supported actions from the default domain
    community.datapower.get_actions:
        domain: default
'''

RETURN = r'''
request:
    description: The request that was sent to DataPower
    type: dict
    returned: always
    sample: {
        "body": null,
        "method": "GET",
        "path": "/mgmt/actionqueue/default/operations"
    }

response:
    description: The response from DataPower in list format.
    type: list
    returned: on success
    sample: [
        "...",
        "Shutdown",
        "SLMResetStats",
        "StandalonePacketCapture",
        "StandaloneStopPacketCapture",
        "StopPacketCapture",
        "TCPConnectionTest",
        "TestPasswordMap",
        "TestRadius",
        "TestURLMap",
        "TestURLRefresh",
        "TestURLRewrite",
        "TestValidateSchema",
        "TraceRoute",
        "...",
    ]
          
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.actionqueue import DPActionQueue

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPActionQueueRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPRequestHandler
)

def run_module():
    module_args = dict(
        domain = dict(type='str', required=True)
    )
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    connection = Connection(module._socket_path)
    
    dp_act = DPActionQueue(**module.params)
    dp_req = DPActionQueueRequest(dp_act)
    req_handler =  DPRequestHandler(connection)
    result = {}
    #Override the default of POST
    dp_req.method = 'GET'
    try:
        response = req_handler.process_request(dp_req.info_path, dp_req.method)
    except ConnectionError as e:
        response = to_text(e)
        module.fail_json(msg=response, **result)

    result['request'] = {'path': dp_req.info_path, 'method': dp_req.method, 'body': dp_req.body}
    values = list(response['_links'].keys())
    values.remove('self')
    result['response'] = values
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()