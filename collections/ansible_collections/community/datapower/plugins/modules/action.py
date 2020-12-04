#!/usr/bin/env python

# Copyright: (c) 2020,Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.action

short_description: Use for creating various objects on IBM DataPower


version_added: "1.0.0"

description: Use for performing actions such as quiesce, save config, reboot, etc...  Get a list of actions from URI /mgmt/actionqueue/{domain}/operations

options:
    domains:
        description: List of domains to execute on.
        required: true
        type: list
    body:
        description: The action to be performed
        required: true
        type: dict


author:
    - Anthony Schneider
'''

EXAMPLES = r'''
- name: Save a domains configuration.
community.datapower.action:
    domain: "{{ domain }}
    body:
    SaveConfig: {}
'''

RETURN = r'''
request:
    description: The request that was sent to DataPower
    type: dict
    returned: always
    sample: {
        "body": null,
        "method": "GET",
        "path": "/mgmt/config/default/CryptoValCred?"
    }

response:
    description: The response from DataPower
    type: dict
    returned: on success
    sample: {
        "SaveConfig": "Operation completed.",
        "_links": {
            "doc": {
                "href": "/mgmt/docs/actionqueue"
            },
            "self": {
                "href": "/mgmt/actionqueue/default"
            }
        }
    }      
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower import DPAction


def run_module():
    module_args = dict(
        domain = dict(type='str', required=True),
        body = dict(type='dict', required=True)
    )
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    
    dp_act = DPAction(module)

    try:
        result = dp_act.send_request()
    except ConnectionError as ce:
        result = dict()
        result['changed'] = False
        module.fail_json(msg=to_text(ce), **result)

    result['changed'] = False 

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()