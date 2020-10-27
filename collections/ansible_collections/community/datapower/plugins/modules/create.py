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

description: Use for creating configuration, this won't succeed if the object already exists protecting from overwrite.

options:
    domains:
        description: List of domains to execute on.
        required: true
        type: list
    defintions:
        description: DataPower object config defined in yaml.  Determine fromat using a GET and then convert to YAML.
        required: true
        type: list of dictionaries (in YAML)


author:
    - Your Name (anthonyschneider)
'''

EXAMPLES = r'''
# Create a datapower object.  You can determine the correct definition by performing a datapower.get after creating it in the WebGUI.
  
  - name: Create a datapower domain(s)
    community.datapower.create:
      domains:
      - default
      definitions:
      - Domain:
          name: test_domain1
          mAdminState: enabled
          NeighborDomain:
            value: default
          FileMap:
            CopyFrom: 'on'
            CopyTo: 'on'
            Delete: 'on'
            Display: 'on'
            Exec: 'on'
            Subdir: 'on'
          MonitoringMap:
            Audit: 'off'
            Log: 'off'
          ConfigMode: local
          ImportFormat: ZIP
          LocalIPRewrite: 'on'
          MaxChkpoints: 3
          ConfigPermissionsMode: scope-domain
      
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
from ansible_collections.community.datapower.plugins.module_utils.datapower import DPCreate


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        domain = dict(type='str', required=True),
        body = dict(type='dict', required=True)
    )
    
    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
  

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
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
    dp_create = DPCreate(module)
    create_result = dp_create.execute_task()
    result['result'] = create_result

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()