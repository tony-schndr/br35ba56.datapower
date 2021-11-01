#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: config

short_description: Manage Configuration objects in DataPower Application Domains.

version_added: "1.0.0"

description: Manage Configuration objects in DataPower Application Domains.
    This will overwrite the object if it exists, or create a new one if it doesn't.
    This module does not create child objects. If a parent object references a
    child object, that object must exist for the parent to be created successfully.

options:
    domain:
        description: Target domain
        required: true
        type: str
    config:
        description: The REST payload of the configuration object being targeted.  One way to determine a valid payload is to create
            the object in the GUI first, then retrieve it with a GET request or the get_config module.
        required: True
        type: dict
    state:
        description: Wether to create/modify or delete.
        required: True
        type: str
        choices:
          - present
          - absent

author:
- Anthony Schneider (@br35ba56)
'''

# Create a valcred in {{ domain }}.  With this example the class_name CryptoValCred and
# name "valcred" are in the body of the request.
EXAMPLES = r'''
---
- name: Modify the valcred Certificate list
  community.datapower.config:
    domain: default
    state: present
    config:
      CryptoValCred:
        CRLDPHandling: ignore
        CertValidationMode: legacy
        Certificate:
        - value: Test1
        - value: Test2
        CheckDates: 'on'
        ExplicitPolicy: 'off'
        RequireCRL: 'off'
        UseCRL: 'off'
        mAdminState: enabled
        name: valcred

# You can also just pass the paramters to the object by defining class_name and name.
- name: Disable the valcred
  community.datapower.config:
    state: present
    domain: default
    class_name: CryptoValCred
    name: valcred
    object:
      mAdminState: disabled
'''

RETURN = r'''
response:
    description: The response returned from DataPowers Rest MGMT Interface.
    type: dict
    returned: on success
    sample: {
        "_links": {
            "doc": {
                "href": "/mgmt/docs/config/CryptoValCred"
            },
            "self": {
                "href": "/mgmt/config/default/CryptoValCred/valcred"
            }
        },
        "valcred": "Configuration was updated."
    }
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    ensure_config
)

from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    dp_diff
)
from ansible.module_utils.basic import missing_required_lib


def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        config=dict(type='dict', required=True),
        state=dict(type='str', choices=['present', 'absent'], required=True)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    if dp_diff.DICTDIFFER_IMPORT_ERROR:
        module.fail_json(
            msg=missing_required_lib('dictdiffer'),
            exception=dp_diff.DICTDIFFER_IMPORT_ERROR)

    domain = module.params.get('domain')
    config = module.params.get('config')
    state = module.params.get('state')

    result = ensure_config(module, domain, config, state)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
