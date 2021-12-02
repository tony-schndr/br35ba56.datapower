#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: status

short_description: Get status data from DataPower.

version_added: "1.0.0"

description: Retrieve status data from DataPower resources.

options:
    domain:
        description: The domain to retrieve the schema from.
        required: true
        type: str
    name:
        description: Name of the status
        required: true
        type: str

author:
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: Get all object statuses from the default domain
  community.datapower.status:
    domain: default
    name: ObjectStatus
'''

RETURN = r'''
response:
    description: The response from DataPower
    type: dict
    returned: on success
    sample: {
        "ObjectStatus": [
            {
                "AdminState": "enabled",
                "Class": "DNSNameService",
                "ConfigState": "saved",
                "ErrorCode": "",
                "EventCode": "0x00000000",
                "Name": "dns",
                "OpState": "up"
            },
            {
                "AdminState": "enabled",
                "Class": "CRLFetch",
                "ConfigState": "saved",
                "ErrorCode": "",
                "EventCode": "0x00000000",
                "Name": "crl",
                "OpState": "down"
            }
        ]
    }
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    StatusRequest
)


def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        name=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    dp_req = StatusRequest(connection, module.params.get(
        'domain'), module.params.get('name'))
    result = {}

    try:
        response = dp_req.get()
    except ConnectionError as e:
        response = to_text(e)
        module.fail_json(msg=response, **result)

    result['response'] = response
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
