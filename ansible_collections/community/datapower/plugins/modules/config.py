#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
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
    Config,
    get_remote_data
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ConfigRequest,
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
    domain = module.params.get('domain')
    class_name = module.params.get('class_name')
    name = module.params.get('name')
    config = module.params.get('config')
    state = module.params.get('state')

    dp_obj = Config(domain=domain,class_name=class_name, name=name, config=config )
    dp_req = ConfigRequest(connection)
    dp_req.set_path(domain, dp_obj.class_name, dp_obj.name) 
    dp_req.set_body(dp_obj.config)
    result = dict()

    try:
        dp_state_resp = get_remote_data(dp_req)
        result['remote_state'] = clean_dp_dict(dp_state_resp)
    except ConnectionError as ce:
        result['changed'] = False
        module.fail_json(msg=to_text(ce), **result)

    if module._diff:
        result['diff'] = dp_diff.get_change_list(dp_state_resp, dp_req.body)

    request = get_request_func(dp_req, before=dp_state_resp, after=dp_req.body, state=state)

    if module.check_mode:
        if request:
            result['changed'] = True
        else:
            result['changed'] = False
        module.exit_json(**result)

    if request:
        try:
            response = request()
        except ConnectionError as e:
            err = to_text(e)
            result['error'] = err
            result['changed'] = False
            module.fail_json(msg=to_text(e), **result)

        result['response'] = response
        result['changed'] = True

    module.exit_json(**result)


def get_request_func(req, before, after, state):
    if state == 'present':
        if before is None:
            return req.post
        elif dp_diff.is_changed(before, after):
            return req.put
    else:
        if before is None:
            return None
        else:
            return req.delete

    
def main():
    run_module()


if __name__ == '__main__':
    main()