#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: import_zip

short_description: Import an config zip file into a DataPower Application Domain.

version_added: "1.0.0"

description: Import an config zip file into a DataPower Application Domain.

options:
    domain:
        description: Domain to import zip package.
        required: true
        type: str
    export_path:
        description: Path to config export in zip format
        required: true
        type: path

author:
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
    - name: Import Zip
      community.datapower.import_zip:
        domain: snafu
        export_path: /tmp/export.zip
'''

RETURN = r'''
response:
    description: The response from DataPower
    type: dict
    returned: on success
    sample: {}
'''

from copy import deepcopy
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    LocalFile
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    convert_bool_to_on_or_off,
    map_module_args_to_datapower_keys
)


def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        export_path=dict(type='path', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    connection = Connection(module._socket_path)
    result = {}
    export_path = module.params.get('export_path', None)
    domain = module.params.get('domain')
    action = "Import"
    params = deepcopy(module.params)
    params['OverwriteFiles'] = 'on'
    params['OverwriteObjects'] = 'on'
    params = convert_bool_to_on_or_off(params)
    params['Format'] = 'ZIP'
    export_path = module.params['export_path']
    params['InputFile'] = LocalFile(export_path).get_base64()
    action_req = ActionQueueRequest(connection, domain, action, params)

    try:
        response = action_req.post()
    except ConnectionError as e:
        response = to_text(e)
        result['changed'] = False
        module.fail_json(msg=response, **result)

    result['response'] = response
    result['changed'] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
