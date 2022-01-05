#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: mgmt_info

short_description: Retrieve various info from DataPower.

version_added: "1.0.0"

description:  Retrieve various info from DataPower.
    Types of info include the statuses, actions, config class_names, actions, and the schema for actions available.
    This module is a helper module for constructing valid arguments for config, action, and status modules.

author:
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: Grab mgmt action/status/config info
  br35ba56.datapower.mgmt_info:
'''

RETURN = r'''
info:
    description: A list of all valid status objects in datapower.
        Use the values for determine what is a valid status to fetch in the status module.
    type: dict
    returned: on success
    sample: |
        "action": [
            "AddAPIApplication",
            "AddAPIClient",
            "AddKnownHost",
            "AddPasswordMap",
            "AddTrustedHost",
            ...
        ],
        "config": [
            "AAAJWTGenerator",
            "AAAJWTValidator",
            "AAAPolicy",
            "AccessControlList",
            "AccessProfile",
            ...
        ],
        "status": [
            "ActiveUsers",
            "AMQPBrokerStatus",
            "AMQPSourceProtocolHandlerSummary",
            "APIDocumentCachingSummary",
            "APIDocumentStatusSimpleIndex",
            ...
        ]

'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = {}
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    connection = Connection(module._socket_path)
    result = {}

    try:
        result['info'] = connection.info()
    except ConnectionError as ce:
        module.fail_json(msg=to_text(ce))

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
