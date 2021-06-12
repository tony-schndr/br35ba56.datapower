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
from copy import deepcopy
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
        overwrite_objects = dict(type='bool', required=False, default=False),
        overwrite_files = dict(type='bool', required=False, default=False),
        rewrite_local_ip = dict(type='bool', required=False, default=False),
        domains = dict(type='list', required=False),
        files = dict(type='list', required=False)
    )
      
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    connection = Connection(module._socket_path)
    result = {}
    
    action = "Import"
    params = deepcopy(module.params)
    # Convert booleans in the domain dictionaries
    if  params['domains']:
        for domain in params['domains']:
            convert_bool_to_on_or_off(domain)
    params = map_module_args_to_datapower_keys(params)
    params = convert_bool_to_on_or_off(params)

    params['Format'] = 'ZIP'

    export_path = module.params['export_path'] 
    params['InputFile'] = LocalFile(export_path).get_base64()
    action_req = ActionQueueRequest(connection, 'default', action, params)

    
    try:
        response = action_req.create()
    except ConnectionError as e:
        response = to_text(e)
        result['parameters'] = params
        result['changed'] = False
        module.fail_json(msg=response, **result)
    
    
    del params['InputFile']
    result['parameters'] = params
    result['changed'] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()