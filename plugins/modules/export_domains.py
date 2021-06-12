#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: action

short_description: Use for executing actions on IBM DataPower

version_added: "1.0.0"

description: Use for performing actions such as quiesce, save config, reboot, export, import etc...  

options:
    domain:
        description: Domain to execute action on.
        required: true
        type: str
    action:
        description: The action to be performed
        required: true
        type: str
        aliases: 
          - name
    parameters:
        description: parameters, if any, that the action requires
        required: false
        type: dict

author: 
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: Save a domains configuration
  community.datapower.action:
    domain: default
    action: SaveConfig

- name: Quiesce DP prior to change
  community.datapower.action:
    domain: default
    action: QuiesceDP
    parameters:
      timeout: 60

- name: UnQuiesce DP prior to change
  community.datapower.action:
    domain: default
    action: UnquiesceDP
'''

RETURN = r'''
request:
    description: The request that was sent to DataPower
    type: dict
    returned: always
    sample: {
        "body": {
            "UnquiesceDP": {}
        },
        "method": "POST",
        "path": "/mgmt/actionqueue/default"
    }

response:
    description: The response from DataPower
    type: dict
    returned: on success
    sample: {
        "_links": {
            "self": {
                "href": "/mgmt/actionqueue/default/pending/UnquiesceDP-20201231T105919Z-12"
            }
        },
        "status": "completed"
    }
'''
import os
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueRequest,
    ConfigRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    isBase64,
    LocalFile
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    convert_bool_to_on_or_off,
    map_module_args_to_datapower_keys,
    get_file_name
)


def run_module():
    #https://www.ibm.com/docs/en/datapower-gateways/10.0.x?topic=actions-export-action 
    module_args = dict(
        export_path = dict(type='path', required=True),
        domains = dict(type='list', required=False),
        ref_objects = dict(type='bool', required=False, default=False),
        ref_files = dict(type='bool', required=False, default=True),
        include_debug = dict(type='bool', required=False, default=False),
        user_comment = dict(type='str', required=False),
        all_files = dict(type='bool', required=False, default=False),
        persisted = dict(type='bool', required=False, default=True),
        include_internal_files = dict(type='bool', required=False, default=True),
        deployment_policy = dict(type='str', required=False),
    )
      
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    connection = Connection(module._socket_path)
    result = {}
    
    action = "Export"

    parameters = map_module_args_to_datapower_keys(module.params)
    parameters = convert_bool_to_on_or_off(parameters)

    parameters['Format'] = 'ZIP'

    domains = []
    if module.params['domains']:
        for domain in module.params['domains']:
            domain_dict = {
                'name': domain,
                'ref-objects' : module.params['ref_objects'],
                'ref-files': module.params['ref_files'],
                'include-debug': module.params['include_debug']
            }
            domains.append(domain_dict)
        parameters['Domain'] = domains
    action_req = ActionQueueRequest(connection, 'default', action, parameters)
    

    filename = get_file_name(connection)
    try:
        response = action_req.create()
    except ConnectionError as e:
        response = to_text(e)
        result['parameters'] = parameters
        result['changed'] = False
        module.fail_json(msg=response, **result)
    
    export_path = module.params['export_path'] or module._tmpdir
    full_file_path = os.path.join(export_path, filename)
    if isBase64(response['result']['file']):
        LocalFile(full_file_path, response['result']['file'])
    
    result['export'] = full_file_path
    result['args'] = module.params
    result['changed'] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()