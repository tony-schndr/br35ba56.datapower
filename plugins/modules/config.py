#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: config

short_description: Use for managing configuration objects on IBM DataPower

version_added: "1.0.0"

description: Use for modifying configuration.  This request will overwrite the object if it exists, or create a new one if it doesn't.
    You can also use this request to target list properties of various objects.

options:
    domain:
        description: Target domain
        required: true
        type: str
    class_name:
        description: 
            - DataPower config object class name.  Valid class name can be determined via GET at URI /mgmt/config/ or the config_info module.
        required: false
        type: str
    name:
        description: DataPower config object name.  
        required: false
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
request:
    description: The request that was sent to DataPower, can be useful to audit exactly what was sent to DataPower
                to make the change
    type: dict
    returned: always
    sample: {
        "body":{
            "CryptoValCred":{
                "mAdminState":"enabled",
                "name":"valcred"
            }
        },
        "method":"PUT",
        "path":"/mgmt/config/default/CryptoValCred/valcred"
    }

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
from ansible.module_utils.connection import (
    ConnectionError, 
    Connection
) 
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPManageConfigObject
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPManageConfigRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPManageConfigRequestHandler,
    clean_dp_dict
)
from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    dp_diff
)

def run_module():
    module_args = dict(
        domain = dict(type='str', required=True),
        config = dict(type='dict', required=True),
        class_name = dict(type='str', required=False),
        name = dict(type='str', required=False),
        state = dict(type='str', choices=['present', 'absent'], required=True)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True 
    )

    connection = Connection(module._socket_path)
    dp_obj = DPManageConfigObject(**module.params)
    req_handler = DPManageConfigRequestHandler(connection)
    dp_req = DPManageConfigRequest(dp_obj)
    result = dict()
    try:
        dp_state_resp = req_handler.process_request(dp_req.path, 'GET')
    except ConnectionError as e:
        dp_state_resp = to_text(e)
        if 'Resource not found' not in dp_state_resp:        
            result['changed'] = False
            module.fail_json(msg=dp_state_resp, **result)
        elif dp_obj.state == 'absent' and 'Resource not found' in dp_state_resp:
            result['dp_resp'] = 'Resource not found'
            result['changed'] = False
            module.exit_json(**result)

    #Gets rid of keys we don't want compared (_links, href, state)
    clean_dp_dict(dp_state_resp)
    #result['state'] = dp_state_resp
    #module.exit_json(**result)
    if not dp_diff.is_changed(dp_state_resp, dp_req.body):
        result['changed'] = False
        module.exit_json(**result)
    # If check mode grab the change list and return it.
    if module.check_mode:
        if dp_diff.is_changed(dp_state_resp, dp_req.body):
            changes = dp_diff.get_change_list(dp_state_resp, dp_req.body)
            result['changed'] = True
            result['changes'] = changes
        else:
            result['changed'] = False
        module.exit_json(**result)

    try:
        dp_mk_chg_resp = req_handler.process_request(dp_req.path, dp_req.method, dp_req.body)
    except ConnectionError as e:
        dp_mk_chg_resp = to_text(e)
        result['datapower_response'] = dp_mk_chg_resp
        result['changed'] = False
        module.fail_json(msg=to_text(e), **result)

    result['response'] = dp_mk_chg_resp
    result['request'] = {'path':dp_req.path, 'method': dp_req.method, 'body': dp_req.body}
    result['changed'] = True
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()