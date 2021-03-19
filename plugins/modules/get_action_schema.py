#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: get_action_schema

short_description: Get the schema on a particular action.  Then use that to help build
                   the parameters required by the DataPower REST Management Interface

version_added: "1.0.0"

description: Get the schema on a particular action you retrieved from get_actions module.
             You can then use the schema to help build valid parameters.

options:
    domain:
        description: The domain to retrieve the schema from.
        required: true
        type: str
    action:
        description: The action to get the schema for.
        required: true
        type: str


author: 
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: Get an actions schema
  community.datapower.get_action_schema:
    domain: default
    action: QuiesceDP
'''

RETURN = r'''
request:
    description: The request that was sent to DataPower
    type: dict
    returned: always
    sample: {
        "body": null,
        "method": "GET",
        "path": "/mgmt/actionqueue/default/operations/QuiesceDP?schema-format=datapower"
    }
response:
    description: The response from DataPower
    type: dict
    returned: on success
    sample:  {
        "QuiesceDP": {
            "delay": {
                "maxOccurs": 1,
                "minOccurs": 0,
                "simpleType": {
                    "union": {
                        "simpleType": [
                            {
                                "name": "dmUInt16",
                                "restriction": {
                                    "base": "unsignedShort"
                                }
                            },
                            {
                                "name": "dmEmptyElement",
                                "restriction": {
                                    "base": "string",
                                    "length": {
                                        "fixed": "true",
                                        "value": 0
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "timeout": {
                "maxOccurs": 1,
                "minOccurs": 1,
                "simpleType": {
                    "union": {
                        "simpleType": [
                            {
                                "name": "dmUInt16",
                                "restriction": {
                                    "base": "unsignedShort"
                                }
                            },
                            {
                                "name": "dmEmptyElement",
                                "restriction": {
                                    "base": "string",
                                    "length": {
                                        "fixed": "true",
                                        "value": 0
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        },
        "_links": {
            "doc": {
                "href": "/mgmt/docs/actionqueue"
            },
            "self": {
                "href": "/mgmt/actionqueue/default/operations/QuiesceDP"
            }
        }   
    }  
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.actionqueue import (
    DPActionQueue
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPActionQueueSchemaRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPRequestHandler
)

def run_module():
    module_args = dict(
        domain = dict(type='str', required=True),
        action = dict(type='str', required=True)
    )
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    connection = Connection(module._socket_path)
    
    dp_act = DPActionQueue(**module.params)
    dp_req = DPActionQueueSchemaRequest(dp_act)

    req_handler =  DPRequestHandler(connection)
    result = {}
    try:
        response = req_handler.process_request(dp_req.path, dp_req.method)
    except ConnectionError as e:
        response = to_text(e)
        result = {'uri': dp_req.path, 'method': dp_req.method}
        module.fail_json(msg=response, **result)

    result['request'] = {'path': dp_req.path, 'method': dp_req.method, 'body': dp_req.body}
    result['response'] = response
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()