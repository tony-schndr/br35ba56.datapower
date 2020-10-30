#!/usr/bin/env python

# Copyright: (c) 2020, Your Name <YourName@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.create

short_description: Use for creating various objects on IBM DataPower


version_added: "1.0.0"

description: Use for deleting configuration.

options:
    domains:
        description: List of domains to execute on.
        required: true
        type: list
    object_Class:
        description: DataPower objects object_class.  Determine object_class by...
        required: true
        type: str
    name:
        description: Name of object as seen in DataPwer


author:
    - Your Name (anthonyschneider)
'''

EXAMPLES = r'''
# Delete a datapower object.  Determine object_class by ...
  - name: Create a datapower domain(s)
    community.datapower.delete:
      domains:
      - default
      object_class: Domain
      name: test_domain     
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
my_useful_info:
    description: The dictionary containing information about your system.
    type: dict
    returned: always
    sample: {
        'foo': 'bar',
        'answer': 42,
    }
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower import DPDelete 

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

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result = dict(
        changed=False
    )
    dp_del = DPDelete(module)
    result['datapower_result'] = dp_del.send_request()

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()