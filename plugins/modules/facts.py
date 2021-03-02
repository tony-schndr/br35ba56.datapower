#!/usr/bin/env python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.facts

short_description: Get facts on DataPower


version_added: "1.0.0"

description: Use for getting object configuration

author:
    - Anthony Schneider
'''

EXAMPLES = r'''
# Get a datapower object.  Determine object_class by ...
- name: Get the facts from DataPower
  community.datapower.facts:
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
request:
    description: The request that was sent to DataPower
    type: dict
    returned: always
    sample: {
        "body": null,
        "method": "GET",
        "path": "/mgmt/config/default/CryptoValCred?"
    }

domains:
    description: A list of all DataPower Domains
    type: list
    returned: on success
    sample: [
        {
            "name": "default"
        }
    ]
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import (
    ConnectionError, 
    Connection
)
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPGetConfigObject
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPGetConfigRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPGetConfigRequestHandler,
    clean_dp_dict
)

def run_module():
    

    module_args = dict(
    )

 
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    result = {}
    connection = Connection(module._socket_path)
    dp_handler = DPGetConfigRequestHandler(connection)

    try:
        response = dp_handler.process_request('/mgmt/domains/config/', 'GET')
    except ConnectionError as e:
        response = to_text(e)
        result['changed'] = False
        module.fail_json(msg=response, **result)
    clean_dp_dict(response)
    
    domains = []
    if isinstance(response['domain'], list):
        for domain in response['domain']:
            domains.append(domain['name'])
    else:
        domains.append(response['domain'])

    result['domains'] = domains

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
