#!/usr/bin/env python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.import_conf

short_description: Use for importing configuration to IBM DataPower


version_added: "1.0.0"

description: Use for importing configuration to IBM DataPower.

options:
    domain:
        description: Target domain
        required: True
        type: str
    object_class:
        description: DataPower objects object_class.  Valid object_cass can be determined via GET at URI /mgmt/config/
        required: true
        type: str
    name:
        description: Name of object as seen in DataPwer
    body:
        description: The configuration of the object as determined from a GET request.  
            Typically you will create the object in the GUI first.  Then you can retrieve the configuration via JSON with a GET.
        required: True
        type: dict
author:
    - Anthony Schneider
'''

EXAMPLES = r'''
- name: Create certificate
  community.datapower._conf:
    domain: "{{ domain }}"
    body:
      CryptoCertificate:
        name: Test2
        mAdminState: enabled
        Filename: cert:///webgui-sscert.pem
        PasswordAlias: 'off'
        IgnoreExpiration: 'off'

'''

RETURN = r'''
request:
    description: The request that was sent to DataPower
    type: dict
    returned: always
    sample: {
        "body": {
            "CryptoCertificate": {
                "Filename": "cert:///webgui-sscert.pem",
                "IgnoreExpiration": "off",
                "PasswordAlias": "off",
                "mAdminState": "enabled",
                "name": "Test2"
            }
        },
        "method": "POST",
        "path": "/mgmt/config/default/CryptoCertificate"
    }

response:
    description: A Dictionary representing the response returned from DataPowers Rest MGMT Interface
    type: dict
    returned: on success
    sample:  {
        "Test2": "Configuration was created.",
        "_links": {
            "doc": {
                "href": "/mgmt/docs/config/CryptoCertificate"
            },
            "location": {
                "href": "/mgmt/config/default/CryptoCertificate/Test2"
            },
            "self": {
                "href": "/mgmt/config/default/CryptoCertificate"
            }
        }
    }
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower import DPLoadConfig


def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        body=dict(
            type='dict', required=True,
            LoadConfiguration=dict(type='dict', required=True)
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    result = dict(
        changed=False
    )

    dp_load_config = DPLoadConfig(module)
    try:
        result = dp_load_config.send_request()
    except ConnectionError as ce:
        result = dict()
        result['changed'] = False
        module.fail_json(msg=to_text(ce), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()