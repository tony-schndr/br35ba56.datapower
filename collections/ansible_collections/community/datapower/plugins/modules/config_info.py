#!/usr/bin/env python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.config_info

short_description: Get information on available configuration objects.


version_added: "1.0.0"

description: Use for retrieving information on various objects.  Target the 

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
# List all available objects
- name: Get object config info
    community.datapower.config_info:
# Get data on the object including its schema
- name: Get details on a specific object
    community.datapower.config_info:
        class_name: CryptoValCred
'''

RETURN = r'''
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import (
    ConnectionError, 
    Connection
) 
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    MGMT_CONFIG_URI,
    MGMT_CONFIG_METADATA_URI
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPManageConfigRequestHandler
)


def run_module():
    module_args = dict(
        domain = dict(type='str', required=False, default='default'),
        class_name=dict(type='str', required=False)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True 
    )

    connection = Connection(module._socket_path)
    
    dp_handler = DPManageConfigRequestHandler(connection)

    resp = dp_handler.config_info(module.params['domain'], module.params['class_name'])

    result = {}
    result['config_info'] = resp

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()