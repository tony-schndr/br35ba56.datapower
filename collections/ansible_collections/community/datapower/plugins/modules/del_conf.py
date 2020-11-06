#!/usr/bin/env python

# Copyright: (c) 2020, Your Name <YourName@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.delete

short_description: Use for delete various objects on IBM DataPower


version_added: "1.0.0"

description: Use for deleting configuration.

options:
    domain:
        description: List of domains to execute on.
        required: true
        type: list
    object_Class:
        description: DataPower objects object_class.  Determine object_class by...
        required: true
        type: str
    name:
        description: Name of object as seen in DataPower


author:
    - Your Name (anthonyschneider)
'''

EXAMPLES = r'''
# Delete a datapower object.  Determine object_class by ...
- name: Delete valcred
  community.datapower.del_conf:
    domain: "{{ domain }}"
    class_name: CryptoValCred
    name: valcred

- name: Delete Password Map Alias
  community.datapower.del_conf:
    domain: "{{ domain }}"
    class_name: PasswordAlias
    name: SecretPassword2
   
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
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
                "href": "/mgmt/config/default/PasswordAlias/SecretPassword2"
            }
        }
    }

URLError | HTTPError | Connection_Error:
    description: The error message(s) returned by DataPower
    type: dict
    returned: on failure
    sample: {
        "URLError": "message",
    }
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    DPDelete,
    check_for_error
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
    
    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    dp_del = DPDelete(module)
    result = dp_del.send_request()

    if check_for_error(result):
        module.fail_json(msg="Failed to delete configuration", **result)

    result['changed'] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()