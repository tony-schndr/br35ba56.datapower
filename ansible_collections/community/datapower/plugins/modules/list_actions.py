#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: list_actions

short_description: List supported actions to execute on DataPower Application Domains.

version_added: "1.0.0"

description: List supported actions to execute on DataPower Application Domains.

options:
    domain:
        description: Domain to retrieve action list from.
        required: false
        default: default
        type: str

author: 
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: Get supported actions from the default domain
  community.datapower.get_actions:
    domain: default
'''

RETURN = r'''
actions:
    description: List of actions available for a particular domain.  
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
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ListActionsRequest
)


def run_module():
    module_args = dict(
        domain = dict(type='str', required=False, default='default')
    )
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    connection = Connection(module._socket_path)
    
    dp_req = ListActionsRequest(connection, module.params['domain'])
    result = {}
    
    try:
        response = dp_req.get()
    except ConnectionError as e:
        response = to_text(e)
        module.fail_json(msg=response, **result)

    values = list(response['_links'].keys())
    values.remove('self')
    result['actions'] = values
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()