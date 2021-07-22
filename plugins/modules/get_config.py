#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: get_config

short_description: Get object configuration from DataPower Application Domains.

version_added: "1.0.0"

description: Get object configuration from DataPower Application Domains.

options:
    domain:
        description: Target domain
        required: True
        type: str
    class_name:
        description: DataPower object class name.
        required: true
        type: str
    name:
        description: Name that identifies the object in DataPower
        required: false
        type: str
    object_field:
        description: Target a specific field of an object in DataPower
        required: false
        type: str
    recursive:
        description: Get target objects referenced objects.
        required: False
        type: bool
    depth:
        description: Set the depth of the recursion.
        required: False
        type: int
    status:
        description: If true return status information on all returned objects.
        required: False
        type: bool

author: 
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
# Get a datapower object.  Determine object_class by ...
- name: Get a tls profile
  community.datapower.get_config:
    domain: default
    class_name: SSLClientProfile
    
- name: Get a tls profile
  community.datapower.get_config:
    domain: default
    class_name: SSLClientProfile
    status: True
'''

RETURN = r'''
response:
    description: A Dictionary representing the response returned from DataPowers Rest MGMT Interface
    type: dict
    returned: always
    sample: {
    "SSLClientProfile": {
        "CacheSize": 100,
        "CacheTimeout": 300,
        "Caching": "on",
        "Ciphers": [
            "AES_256_GCM_SHA384",
            "CHACHA20_POLY1305_SHA256",
            "AES_128_GCM_SHA256",
            "ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", 
            "ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "ECDHE_ECDSA_WITH_AES_256_CBC_SHA384",
            "ECDHE_RSA_WITH_AES_256_CBC_SHA384",
            "ECDHE_ECDSA_WITH_AES_256_CBC_SHA",
            "ECDHE_RSA_WITH_AES_256_CBC_SHA",
            "DHE_DSS_WITH_AES_256_GCM_SHA384",
            "DHE_RSA_WITH_AES_256_GCM_SHA384",
            "DHE_RSA_WITH_AES_256_CBC_SHA256",
            "DHE_DSS_WITH_AES_256_CBC_SHA256",
            "DHE_RSA_WITH_AES_256_CBC_SHA",
            "DHE_DSS_WITH_AES_256_CBC_SHA",
            "RSA_WITH_AES_256_GCM_SHA384",
            "RSA_WITH_AES_256_CBC_SHA256",
            "RSA_WITH_AES_256_CBC_SHA",
            "ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
            "ECDHE_RSA_WITH_AES_128_GCM_SHA256",
            "ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
            "ECDHE_RSA_WITH_AES_128_CBC_SHA256",
            "ECDHE_ECDSA_WITH_AES_128_CBC_SHA",
            "ECDHE_RSA_WITH_AES_128_CBC_SHA",
            "DHE_DSS_WITH_AES_128_GCM_SHA256",
            "DHE_RSA_WITH_AES_128_GCM_SHA256",
            "DHE_RSA_WITH_AES_128_CBC_SHA256",
            "DHE_DSS_WITH_AES_128_CBC_SHA256",
            "DHE_RSA_WITH_AES_128_CBC_SHA",
            "DHE_DSS_WITH_AES_128_CBC_SHA",
            "RSA_WITH_AES_128_GCM_SHA256",
            "RSA_WITH_AES_128_CBC_SHA256",
            "RSA_WITH_AES_128_CBC_SHA"
        ],
        "EllipticCurves": [
            "secp521r1",
            "secp384r1",
            "secp256k1",
            "secp256r1"
        ],
        "EnableTLS13Compat": "on",
        "HostnameValidationFailOnError": "off",
        "HostnameValidationFlags": {
            "X509_CHECK_FLAG_ALWAYS_CHECK_SUBJECT": "off",
            "X509_CHECK_FLAG_MULTI_LABEL_WILDCARDS": "off",
            "X509_CHECK_FLAG_NO_PARTIAL_WILDCARDS": "off",
            "X509_CHECK_FLAG_NO_WILDCARDS": "off",
            "X509_CHECK_FLAG_SINGLE_LABEL_SUBDOMAINS": "off"
        },
        "Protocols": {
            "SSLv3": "off",
            "TLSv1d0": "off",
            "TLSv1d1": "on",
            "TLSv1d2": "on",
            "TLSv1d3": "on"
        },
        "SSLClientFeatures": {
            "compression": "off",
            "permit-insecure-servers": "off",
            "use-sni": "on"
        },
        "UseCustomSNIHostname": "no",
        "ValidateHostname": "off",
        "ValidateServerCert": "off",
        "_links": {
            "doc": {
                "href": "/mgmt/docs/config/SSLClientProfile"
            },
            "self": {
                "href": "/mgmt/config/default/SSLClientProfile/client-profile"
            }
        },
        "mAdminState": "enabled",
        "name": "client-profile"
    },
    "_links": {
        "doc": {
            "href": "/mgmt/docs/config/SSLClientProfile"
        },
        "self": {
            "href": "/mgmt/config/default/SSLClientProfile"
        }
    }
}

'''

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ConfigRequest
)
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import (
    ConnectionError,
    Connection
)
from ansible.module_utils._text import to_text


def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        class_name=dict(type='str', required=True),
        name=dict(type='str', required=False),
        object_field=dict(type='str', required=False),
        recursive=dict(type='bool', required=False),
        depth=dict(type='int', required=False),
        status=dict(type='bool', required=False)
    )

    mutually_exclusive = [
        ['object_field', 'recursive'],
    ]

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive
    )

    domain = module.params.get('domain')
    class_name = module.params.get('class_name')
    name = module.params.get('name', None)
    field = module.params.get('field', None)

    recursive = module.params.get('recursive')
    depth = module.params.get('depth')
    status = module.params.get('status')
    
    connection = Connection(module._socket_path)
    dp_req = ConfigRequest(connection)
    dp_req.set_path(domain, class_name, name, field)
    dp_req.set_options(recursive=recursive, depth=depth, status=status)
    result = {}
    result['options'] = dp_req.options
    
    try:
        dp_resp = dp_req.get()
    except ConnectionError as e:
        dp_resp = to_text(e)
    result = {}
    result['response'] = dp_resp

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
