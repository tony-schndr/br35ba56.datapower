#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: export_domains

short_description: Export DataPower Application Domain(s)

version_added: "1.0.0"

description: Export DataPower Application Domain(s)
        
options:
    domains:
        description: List of domains to export, if not specified only default domain is exported.
        required: false
        type: list
        elements: str
    export_path:
        description: Directory path to save the export in.
        type: path
        required: true
    ref_objects:
        description: Determines whether to export referenced objects.
        required: false
        type: bool
        default: false
    ref_files:
        description: Determines whether to export referenced files.
        required: false
        type: bool
        default: true
    user_comment:
        description: Comment to include in export.
        required: false
        type: str
    all_files:
        description: |
            Determines whether to include all files
            in the local: directory for the domain.
        required: false
        type: bool
        default: false
    persisted:
        description: |
            Determines whether to export from
            persisted or running configuration. 
        required: false
        type: bool
        default: true     
    include_debug:
        description: Determines whether to export probe data for a DataPower service.
        type: bool
        required: false 
    deployment_policy:
        description: |
            Specifies the optional but valid deployment 
            policy that exists in the application domain.
            The deployment policy is included in the export
            package and processed during the import operation. 
        type: str
        required: false 
    include_internal_files:
        description: |
            Determines whether to include internal files.
            The inclusion of the internal files can reduce 
            import errors when the export package is from 
            an earlier firmware version. Therefore, when 
            you export and import at the same firmware version, 
            these files are unnecessary.
        required: false
        type: bool
        default: true

author: 
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: Export foo domain from datapower config
  community.datapower.export_domains:
    export_path: /tmp/
    all_files: yes
    domains: 
        - foo
    register: full_export
'''

RETURN = r'''
export:
    description: Path to export zip file
    type: str
    returned: on success
    sample:  /tmp/aaf2cf18d49b_6-11-21T2222.45.zip
'''
import os
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueRequest
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
        domains = dict(type='list', required=False, elements='str'),
        ref_objects = dict(type='bool', required=False, default=False),
        ref_files = dict(type='bool', required=False, default=True),
        include_debug = dict(type='bool', required=False),
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
        response = action_req.post()
    except ConnectionError as e:
        response = to_text(e)
        result['changed'] = False
        module.fail_json(msg=response, **result)
    
    export_path = module.params['export_path'] or module._tmpdir
    full_file_path = os.path.join(export_path, filename)
    if isBase64(response['result']['file']):
        LocalFile(full_file_path, response['result']['file'])
    
    result['export'] = full_file_path
    result['changed'] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()