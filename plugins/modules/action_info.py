#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: action_info

short_description: Get the schema of an action.  Use the schema to help
    determine the parameters required for the action module parameter field.

version_added: "1.0.0"

description: Get the schema of an action.  Use the schema to help
    determine the parameters required for the action module parameter field.

options:
    action:
        description: The action to get the schema for.
        required: true
        type: str


author:
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: Return information about a particular action
  br35ba56.datapower.action_info:
    action: QuiesceDP
'''

RETURN = r'''
schema:
    description: The response from DataPower
    type: dict
    returned: on success
    sample:  {
        "QuiesceDP": {
            "delay": {
                "maxOccurs": 1,
                "minOccurs": 0,
                "simpleType": {
                    "union": {
                        "simpleType": [
                            {
                                "name": "dmUInt16",
                                "restriction": {
                                    "base": "unsignedShort"
                                }
                            },
                            {
                                "name": "dmEmptyElement",
                                "restriction": {
                                    "base": "string",
                                    "length": {
                                        "fixed": "true",
                                        "value": 0
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "timeout": {
                "maxOccurs": 1,
                "minOccurs": 1,
                "simpleType": {
                    "union": {
                        "simpleType": [
                            {
                                "name": "dmUInt16",
                                "restriction": {
                                    "base": "unsignedShort"
                                }
                            },
                            {
                                "name": "dmEmptyElement",
                                "restriction": {
                                    "base": "string",
                                    "length": {
                                        "fixed": "true",
                                        "value": 0
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        }
    }
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.utils import clean_dp_dict
from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueSchemaRequest
)


def run_module():
    module_args = dict(
        action=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    connection = Connection(module._socket_path)

    dp_req = ActionQueueSchemaRequest('default', module.params.get('action'))

    result = {}
    try:
        response = connection.send_request(**dp_req.get())
        clean_dp_dict(response)
    except ConnectionError as e:
        response = to_text(e)
        module.fail_json(msg=response, **result)

    result['schema'] = response
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
