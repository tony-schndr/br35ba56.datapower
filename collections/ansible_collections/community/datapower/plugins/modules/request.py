#!/usr/bin/env python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.request

short_description: Use for generic requests to DataPower


version_added: "1.0.0"

description: Use this module incase some functionality is not implemented.  This allows you to pass path, method, body
    directly to DataPower REST Mgmt Interface

options:
    path:
        description: URI to be called.
        required: True
        type: str
    method:
        description: GET | POST | PUT | DELETE 
    body:
        description:  Body of request in JSON/YAML
        required: True
        type: dict

author:
    - Anthony Schneider
'''

EXAMPLES = r'''
- name: Request example, this will return Config Items
  community.datapower.request:
    path: /mgmt/config/
    method: GET
'''

RETURN = r'''
request:
    description: The request sent to DataPower that yielded the response value.
    
    returned: always
    sample:  {
        "_links": {
            "AAAJWTGenerator": {
                "href": "/mgmt/config/{domain}/AAAJWTGenerator"
            },
            "AAAJWTValidator": {
                "href": "/mgmt/config/{domain}/AAAJWTValidator"
            },
            "AAAPolicy": {
                "href": "/mgmt/config/{domain}/AAAPolicy"
            } ...
        }
    }
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower import DPRequest


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path = dict(type='str', required=True),
        body = dict(type='dict', required=False),
        method = dict(type='str', choices=['PUT', 'POST', 'GET', 'DELETE'])
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

    
    dp_req = DPRequest(module)
    try:
        result = dp_req.send_request()
    except ConnectionError as ce:
        result = dict()
        result['changed'] = False
        module.fail_json(msg=to_text(ce), **result)

    result['changed'] = False # Place holder, need to build logic to determine if something was changed.

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()