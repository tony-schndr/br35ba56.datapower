#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: load_config

short_description: Import objects/files into a DataPower Application Domain.

version_added: "1.0.0"

description: Import objects/files into a DataPower Application Domain.

options:
    domain:
        description: Domain to load objects into
        required: true
        type: str
    config:
        description: |
            Dictionary of config to import.
            This dictionary should be retrieved from the
            from export_objects module with the returned
            config variable.
        required: true
        type: dict

author:
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
    - name: load objects
      community.datapower.load_config:
        domain: snafu
        config: {
                "CryptoValCred": {
                    "CRLDPHandling": "ignore",
                    "CertValidationMode": "legacy",
                    "CheckDates": "on",
                    "ExplicitPolicy": "off",
                    "InitialPolicySet": "2.5.29.32.0",
                    "RequireCRL": "off",
                    "UseCRL": "on",
                    "mAdminState": "enabled",
                    "name": "valcred"
                },
                "SSLClientProfile": [
                    {
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
                        "Valcred": "valcred",
                        "ValidateHostname": "off",
                        "ValidateServerCert": "on",
                        "mAdminState": "enabled",
                        "name": "clientprofile"
                    },
                    {
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
                        "Valcred": "valcred",
                        "ValidateHostname": "off",
                        "ValidateServerCert": "on",
                        "mAdminState": "enabled",
                        "name": "client_profile"
                    }
                ]
            }
'''

RETURN = r'''
response:
    description: The response from DataPower
    type: dict
    returned: on success
    sample: {
        "_links": {
            "self": {
                "href": "/mgmt/actionqueue/default/pending/LoadConfiguration-20210611T232241Z-13"
            }
        },
        "result": {
            "config-item": [
                {
                    "id": "valcred",
                    "status": "ok",
                    "text": "Configuration was updated.",
                    "type": "CryptoValCred"
                },
                {
                    "id": "clientprofile",
                    "status": "ok",
                    "text": "Configuration was updated.",
                    "type": "SSLClientProfile"
                },
                {
                    "id": "client_profile",
                    "status": "ok",
                    "text": "Configuration was updated.",
                    "type": "SSLClientProfile"
                }
            ]
        },
        "status": "completed"
    }
'''

from copy import deepcopy
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueRequest
)


def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        config=dict(type='dict', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    connection = Connection(module._socket_path)
    result = {}

    action = "LoadConfiguration"
    objects = deepcopy(module.params.get('objects'))
    # Convert booleans in the domain dictionaries
    action_req = ActionQueueRequest(module.params.get('domain'), action, objects)

    try:
        response = connection.execute_action(**action_req.post())
    except ConnectionError as e:
        response = to_text(e)
        result['changed'] = False
        module.fail_json(msg=response, **result)

    result['response'] = response
    result['changed'] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
