#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: list_objects

short_description: Get information on available configuration objects.

version_added: "1.0.0"

description: Use for retrieving information on various objects.  Target the 

options:
    domain:
        description: Target domain
        default: default
        type: str
        required: false
  
author: 
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
# List all available objects
- name: List all objects, if not domain is specified the default domain is used
  community.datapower.list_objects:

- name: List all objects from foo domain
  community.datapower.list_objects:
    domain: foo
'''
 
RETURN = r'''
objects:
    description: List of configurable objects for a DataPower domain
    type: list
    returned: always
    sample:  [
        "...",
        "MCFHttpMethod",
        "MCFHttpURL",
        "MCFXPath",
        "MPGWErrorAction",
        "MPGWErrorHandlingPolicy",
        "MQFTESourceProtocolHandler",
        "MQGW",
        "MQManager",
        "MQManagerGroup",
        "MQQM",
        "MQQMGroup",
        "MQSourceProtocolHandler",
        "MQhost",
        "MQproxy",
        "MQv9PlusMFTSourceProtocolHandler",
        "MQv9PlusSourceProtocolHandler",
        "MTOMPolicy",
        "...",
    ]
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
        domain = dict(type='str', required=False, default='default')
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True 
    )
    
    connection = Connection(module._socket_path)
    
    req_handler = DPManageConfigRequestHandler(connection)

    resp = req_handler.config_info(module.params['domain'], module.params['class_name'])

    result = {}
    result['objects'] = resp

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()