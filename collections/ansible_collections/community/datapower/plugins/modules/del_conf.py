#!/usr/bin/env python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.del_conf

short_description: Use for delete various objects on IBM DataPower


version_added: "1.0.0"

description: Use for deleting configuration.

options:
    domain:
        description: Target domain
        required: True
        type: str
    object_class:
        description: DataPower objects object_class.
        required: true
        type: str
    name:
        description: Name of object as seen in DataPower

author:
    - Anthony Schneider
'''

EXAMPLES = r'''
# Delete a datapower object.
- name: Delete Password Map Alias
    community.datapower.del_conf:
    domain: "{{ domain }}"
    class_name: PasswordAlias
    name: SecretPassword
'''

RETURN = r'''
request:
    description: The request that was sent to DataPower
    type: dict
    returned: always
    sample:  {
        "body": null,
        "method": "DELETE",
        "path": "/mgmt/config/default/PasswordAlias/SecretPassword2"
    }

response:
    description: A Dictionary representing the response returned from DataPowers Rest MGMT Interface
    type: dict
    returned: on success
    sample:  {
        "SecretPassword2": "Configuration was deleted.",
        "_links": {
            "doc": {
                "href": "/mgmt/docs/config/PasswordAlias"
            },
            "self": {
                "href": "/mgmt/config/default/PasswordAlias/SecretPassword"
            }
        }
    }
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.dp_obj import (
    DPConfigObject
)

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        domain = dict(type='str', required=True),
        class_name = dict(type='str', required=True),
        name = dict(type='str', required=True),
        obj_field = dict(type='str', required=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    
    dp_obj = DPConfigObject(**module.params)

    result = {}
    result['dp_obj'] = vars(dp_obj)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()