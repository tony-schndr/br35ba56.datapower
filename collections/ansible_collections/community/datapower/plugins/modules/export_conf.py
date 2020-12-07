#!/usr/bin/env python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.export

short_description: Use for exporting configuration from IBM DataPower


version_added: "1.0.0"

description: Use for exporting configuration.

options:
    domain:
        description: Target domain
        required: True
        type: str
    body:
        description: Valid export request at the Domain, Object, or Appliance level. 
        required: true
        type: dictionary
author:
    - Anthony Schneider
'''

EXAMPLES = r'''
- name: Export object configuration
    community.datapower.export:
    domain: "{{ domain }}"
    body:
        Export:
        Format: JSON
        UserComment: comments
        AllFiles: 'off'
        Persisted: 'off'
        IncludeInternalFiles: 'off'
        Object:
            - name: valcred
            class: CryptoValCred

- name: Export object config in xml format (Shows up as base64 in response payload)
    community.datapower.export:
    domain: "{{ domain }}"
    body:
        Export:
        Format: XML
        UserComment: comments
        AllFiles: 'off'
        Persisted: 'off'
        IncludeInternalFiles: 'off'
        Object:
            - name: valcred
            class: CryptoValCred

- name: Export domain config in ZIP format.
    community.datapower.export:
    domain: "{{ domain }}"
    body:
        Export:
        Format: ZIP
        UserComment: comments
        AllFiles: 'off'
        Persisted: 'off'
        IncludeInternalFiles: 'off'
'''

RETURN = r'''
request:
    description: The request sent to DataPower that yielded the response value.
        This request is unique in which it does not return the original request from the module.  
        This is because the original request from the user does not generate the export, it simply queues the action.
        Thefore the underlying module logic loops until the export is complete, then returns that via a GET.
    type: dict
    returned: always
    sample: {
        "body": null,
        "method": "GET",
        "path": "/mgmt/actionqueue/default/pending/Export-20201105T215918Z-7"
    }
response:
    description: Response from DataPower
    type: dict
    returned: always
    sample:  {
        "_links": {
            "self": {
                "href": "/mgmt/actionqueue/default/pending/Export-20201105T221931Z-1"
            }
        },
        "result": {
            "LoadConfiguration": {
                "CryptoValCred": {
                    "CRLDPHandling": "ignore",
                    "CertValidationMode": "legacy",
                    "Certificate": [
                        "Test1",
                        "Test2"
                    ],
                    "CheckDates": "on",
                    "ExplicitPolicy": "off",
                    "InitialPolicySet": "2.5.29.32.0",
                    "RequireCRL": "off",
                    "UseCRL": "on",
                    "mAdminState": "enabled",
                    "name": "valcred"
                }
            }
        },
        "status": "completed"
    }
'''
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower import DPExport


def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        body=dict(type='dict', required=True,
            Export=dict(type='dict', required=True,
                Format=dict(choices=['JSON', 'XML', 'ZIP'], required=True),
                UserComments=dict(type='str', required=False),
                AllFiles=dict(type='bool', required=True),
                Persisted=dict(type='bool', required=True),
                IncludeInternalFiles=dict(type='bool', required=True),
                DeploymentPolicy=dict(type='str', required=False),
                Domain=dict(
                    type='list', required=False,
                    name=dict(type='str', required=True),
                    ref_objects=dict(type='bool', required=True),
                    ref_files=dict(type='bool', required=True),
                    include_debug=dict(type='bool', required=False)
                ),
                Object=dict(
                    type='list', required=False,
                    class_=dict(type='str', required=True),
                    name=dict(type='str', required=True),
                    ref_objects=dict(type='bool', required=True),
                    ref_files=dict(type='bool', required=True),
                    include_debug=dict(type='bool', required=False)
                )
            )
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False, # Should we check the objects/domains exist for exporting?
    )

    dp_exp = DPExport(module)

    try:
        result = dp_exp.send_request()
    except ConnectionError as ce:
        result = dict()
        result['changed'] = False
        module.fail_json(msg=to_text(ce), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
