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
      br35ba56.datapower.import_zip:
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
import base64
from copy import deepcopy
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueRequest
)

from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.utils import (
    convert_bool_to_on_or_off
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
    domain = module.params.get('domain')
    action = "Import"
    params = deepcopy(module.params)
    params['OverwriteFiles'] = 'on'
    params['OverwriteObjects'] = 'on'
    params = convert_bool_to_on_or_off(params)
    params['Format'] = 'ZIP'

    try:
        with open(module.params['export_path'], 'rb') as f:
            data = f.read()
    except (IOError, OSError) as e:
        module.fail_json(msg='Error while reading export zip file from disk: {0}'.format(e))

    params['InputFile'] = base64.b64encode(data).decode()
    action_req = ActionQueueRequest(domain, action, params)

    try:
        response = connection.execute_action(**action_req.post())
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
