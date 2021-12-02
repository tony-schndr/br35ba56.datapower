#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: export_zip

short_description: |
    Export configuration from a DataPower Application Domain.

version_added: "1.0.0"

description: Export configuration from a DataPower Application Domain.

options:
    domain:
        description: Domain to export objects from.
        required: true
        type: str
    objects:
        description: |
            A JSON-formatted array of objects to export.
            Each object must have a name and object class,
            but you can control the inclusion of referenced
            objects and files. If the object is a DataPower
            service, you can include probe data.
        required: true
        type: list
        elements: dict
    dest:
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
        default: false
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
        default: false
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
        default: false
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

author:
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: Export objects
  community.datapower.export_config:
    domain: default
    ref_objects: yes
    objects:
      - name: valcred
        class: CryptoValCred
'''

RETURN = r'''

config:
    description: Exported configuration.
    type: dict
    returned: on success
    sample:  {
        "CryptoValCred": {
            "CRLDPHandling": "ignore",
            "CertValidationMode": "legacy",
            "CheckDates": "on",
            "ExplicitPolicy": "off",
            "InitialPolicySet": "2.5.29.32.0",
            "RequireCRL": "off",
            "UseCRL": "on",
            "mAdminState": "enabled",
            "name": "valcred"
        }
    }
'''

from copy import deepcopy
import os
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueRequest,
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    convert_bool_to_on_or_off,
    map_module_args_to_datapower_keys,
    get_random_file_name,
    create_file_from_base64
)


def run_module():

    module_args = dict(
        domain=dict(type='str', required=True),
        dest=dict(type='path', required=True),
        objects=dict(type='list', required=True,
                     elements='dict'),
        ref_objects=dict(type='bool', required=False, default=False),
        ref_files=dict(type='bool', required=False, default=False),
        include_debug=dict(type='bool', required=False),
        user_comment=dict(type='str', required=False),
        all_files=dict(type='bool', required=False, default=False),
        persisted=dict(type='bool', required=False, default=False),
        include_internal_files=dict(type='bool', required=False, default=False),
        deployment_policy=dict(type='str', required=False),
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
    domain = module.params.get('domain')
    objects = []

    if module.params['objects']:
        for obj in module.params['objects']:
            obj_dict = {
                'name': obj['name'],
                'class': obj['class'],
                'ref-objects': 'on' if module.params['ref_objects'] else 'off',
                'ref-files': 'on' if module.params['ref_files'] else 'off',
                'include-debug': 'on' if module.params['include_debug'] else 'off'
            }
            objects.append(obj_dict)
        parameters['Object'] = objects

    action_req = ActionQueueRequest(connection, domain, action, parameters)
    filename = get_random_file_name('zip')

    try:
        response = action_req.post()
    except ConnectionError as e:
        response = to_text(e)
        result['changed'] = False
        result['parameters'] = parameters
        module.fail_json(msg=response, **result)

    dest = module.params['dest']
    path = os.path.join(dest, filename)

    try:
        create_file_from_base64(path, response['result']['file'])
    except (IOError, OSError) as e:
        module.fail_json(msg='Error while writing file to disk: {0}'.format(e))

    del response['result']['file']
    result['response'] = response
    result['path'] = path
    result['changed'] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
