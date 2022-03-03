#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: password_map

short_description: Manage Password Map Aliases on a DataPower Application Domain.

version_added: "1.0.0"

description: Manage Password Map Aliases on a DataPower Application Domain.

options:
    domain:
        description: Domain to execute action on.
        required: true
        type: str
    name:
        description: Name of the password map alias object.
        required: true
        type: str
    password:
        description: string value of the password
        required: true
        type: str
    state:
        description: create or delete the password map alias
        required: true
        type: str
        choices:
          - present
          - overriden
          - absent
author:
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: Create password map alias
  br35ba56.datapower.password_map:
    domain: default
    name: test_password_map
    password: $ecureP@$$
    state: present
'''

RETURN = r'''
config:
    description: The configuration after the changes were made.
    type: dict
    returned: on success
    sample: {
        "PasswordAlias": {
            "EncryptedPassword": "UaujJasXOri4+wTe3fvT9YV16SLzzL5C",
            "mAdminState": "enabled",
            "name": "test_password_map"
        }
    }
response:
    description: The response from DataPower
    type: dict
    returned: on success
    sample: {
        "_links": {
            "doc": {
                "href": "/mgmt/docs/config/PasswordAlias"
            },
            "location": {
                "href": "/mgmt/config/foo/PasswordAlias/test_password_map"
            },
            "self": {
                "href": "/mgmt/config/foo/PasswordAlias"
            }
        },
        "test_password_map": "Configuration was created."
    }

'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.utils import (
    clean_dp_dict
)
from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.utils import ensure_config


def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        name=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', required=True, choices=['absent', 'present', 'overriden'])
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    connection = Connection(module._socket_path)
    result = {}
    result['changed'] = False
    domain = module.params.get('domain')
    name = module.params.get('name')
    password = module.params.get('password')
    state = module.params.get('state')

    config = {
        "PasswordAlias": {
            "name": name,
            "Password": password,
            "mAdminState": "enabled"
        }
    }

    try:
        map = connection.get_resource_or_none('/mgmt/config/{domain}/PasswordAlias/{name}'.format(domain=domain, name=name))
    except ConnectionError as e:
        response = to_text(e)
        result['changed'] = False
        module.fail_json(msg=response, **result)

    if map is not None:
        clean_dp_dict(map)

    if map is None and state == 'present':
        result = ensure_config(module, domain, config, 'merged')
        module.exit_json(**result)
    elif (map is None and state == 'absent') or (map is not None and state == 'present'):
        result['config'] = map
        module.exit_json(**result)
    elif map is not None and state == 'overriden':
        result = ensure_config(module, domain, config, 'merged')
        module.exit_json(**result)
    elif map is not None and state == 'absent':
        result = ensure_config(module, domain, config, 'deleted')
        module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
