#!/usr/bin/env python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.mod_conf

short_description: Use for modifying various objects on IBM DataPower


version_added: "1.0.0"

description: Use for modifying configuration.  This request will overwrite the object if it exists, or create a new one if it doesn't.
    You can also use this request to target list properties of various objects.

options:
    domain:
        description: Target domain
        required: True
        type: str
    object_class:
        description: DataPower objects object_class.  Valid object_cass can be determined via GET at URI /mgmt/config/
        required: Only when targeting a list property
        type: str
    object:
        description: The configuration of the object as determined from a GET request.  
            Typically you will create the object in the GUI first.  Then you can retrieve the configuration via JSON with a GET.
            For list properties the object should represent that particiluar portion of the GET reponse, not the entire object.
        required: True
        type: dict
author:
    - Anthony Schneider
'''

EXAMPLES = r'''
# Modify a datapower object.  This example simply disables test_domain1.  
# This is an example where the request targets a list property
- name: Modify the valcred Certificate list
    community.datapower.mod_conf:
    domain: "{{ domain }}"
    class_name: CryptoValCred
    name: valcred
    obj_field: Certificate
    object:
        Certificate:
        - value: Test2

# This example targets the object as a whole
- name: Disable the valcred
    community.datapower.mod_conf:
    domain: "{{ domain }}"
    object:
        CryptoValCred:
            name: valcred
            mAdminState: disabled
'''

RETURN = r'''
request:
    description: The request that was sent to DataPower
    type: dict
    returned: always
    sample: {
        "object": {
            "Certificate": [
                {
                    "value": "Test2"
                }
            ]
        },
        "method": "POST",
        "path": "/mgmt/config/default/CryptoValCred/valcred/Certificate"
    }

response:
    description: A Dictionary representing the response returned from DataPowers Rest MGMT Interface
    type: dict
    returned: on success
    sample: {
        "Certificate": "Property was updated.",
        "_links": {
            "doc": {
                "href": "/mgmt/docs/config/CryptoValCred/Certificate"
            },
            "self": {
                "href": "/mgmt/config/default/CryptoValCred/valcred/Certificate"
            }
        }
    }
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.dp_obj import (
    DPApplyConfig
)

def run_module():
    module_args = dict(
        domain = dict(type='str', required=True),
        config = dict(type='dict', required=True),
        class_name=dict(type='str', required=False),
        object_name = dict(type='str', required=False),
        object_field = dict(type='str', required=False),
        overwrite = dict(type='bool', required=False, default=False)
        state = dict(type='str', choices=['present', 'absent'], required=True)
    )
   
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True 
    )
    
    dp_obj = DPConfigObject(**module.params)

    result = {}
    result['dp_obj'] = vars(dp_obj)

    module.exit_json(**result)

def main():
    run_module()


if __name__ == '__main__':
    main()