#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: export_config

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
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueRequest,
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    convert_bool_to_on_or_off,
    map_module_args_to_datapower_keys
)


def run_module():
    # https://www.ibm.com/docs/en/datapower-gateways/10.0.x?topic=actions-export-action
    module_args = dict(
        domain=dict(type='str', required=True),
        objects=dict(type='list', required=True, elements='dict'),
        ref_objects=dict(type='bool', required=False, default=False),
        ref_files=dict(type='bool', required=False, default=False),
        all_files=dict(type='bool', required=False, default=False),
        persisted=dict(type='bool', required=False, default=True),
        include_internal_files=dict(type='bool', required=False, default=False)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    connection = Connection(module._socket_path)
    result = {}
    params = deepcopy(module.params)
    action = "Export"

    for obj in params['objects']:
        obj['ref-objects'] = "on" if module.params['ref_objects'] else "off"
        obj['ref-files'] = "on" if module.params['ref_files'] else "off"

    del params['ref_objects']
    del params['ref_files']

    parameters = map_module_args_to_datapower_keys(params)
    parameters = convert_bool_to_on_or_off(parameters)
    parameters['Format'] = 'JSON'
    action_req = ActionQueueRequest(
        connection, module.params['domain'], action, parameters)

    try:
        response = action_req.post()
    except ConnectionError as e:
        response = to_text(e)
        result['changed'] = False
        module.fail_json(msg=response, **result)

    result['objects'] = response['result']['LoadConfiguration'] or None
    result['changed'] = False
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
