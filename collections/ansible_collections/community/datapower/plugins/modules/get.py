#!/usr/bin/env python

# Copyright: (c) 2020, Your Name <YourName@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.get

short_description: Use for geting objects on IBM DataPower


version_added: "1.0.0"

description: Use for getting object configuration

options:
    domain:
        description: Target domain
        required: True
        type: str
    object_class:
        description: DataPower objects object_class.  Determine object_class by...
        required: true
        type: str
    name:
        description: Name of object as seen in DataPwer
    options:
        description: Options for uri???
        required: False
        type: dict
        recursive:
            description: Get target objects referenced objects.
            required: False
            type: bool
        depth:
            description: Set the depth of the recursion.
            required: False
            type: int
            default: 7
        state:
            description: If true return state information on all returned objects.
            required: False
            type: bool
            default: False


author:
    - Your Name (anthonyschneider)
'''

EXAMPLES = r'''
# Get a datapower object.  Determine object_class by ...
  - name: Create a datapower domain(s)
    community.datapower.get:
      domain: default
      object_class: Domain
      name: SNAFU
      options:
        recursive: True 
        depth: 3
        state: True     
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
from ansible_collections.community.datapower.plugins.module_utils.datapower import DPGet

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        domain=dict(type='str', required=True),
        class_name=dict(type='str', required=True),
        name=dict(type='str', required=False),
        obj_field=dict(type='str', required=False),
        recursive=dict(type='bool', required=False),
        depth=dict(type='int', required=False),
        state=dict(type='bool', required=False)
        
    )
    mutually_exclusive = [
        ['obj_field', 'recursive'],
    ]
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive
    )
    
    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    #if module.check_mode:
    #    module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result = dict(
        changed=False,
    )
    dp_get = DPGet(module)
    result['datapower_config'] = dp_get.send_request()

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()