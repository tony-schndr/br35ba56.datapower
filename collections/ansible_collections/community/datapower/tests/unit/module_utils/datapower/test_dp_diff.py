from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    dp_diff
)

def test_dp_valcred_state():
    dp_state_resp =  {
        "CryptoValCred": {
            "CRLDPHandling": "ignore",
            "CertValidationMode": "legacy",
            "Certificate": {
                "href": "/mgmt/config/default/CryptoCertificate/Test1",
                "value": "Test1"
            },
            "CheckDates": "on",
            "ExplicitPolicy": "off",
            "InitialPolicySet": "2.5.29.32.0",
            "RequireCRL": "off",
            "UseCRL": "on",
            "mAdminState": "enabled",
            "name": "valcred"
        },
        "_links": {
            "doc": {
                "href": "/mgmt/docs/config/CryptoValCred"
            },
            "self": {
                "href": "/mgmt/config/default/CryptoValCred/valcred"
            }
        }
    }
    proposed_valcred = {
        "CryptoValCred": {
            "name": "valcred",
            "mAdminState": "disabled"
        }
    }
    compared_valcred = {
        "CryptoValCred": {
            'name':'valcred',
            'mAdminState': {
                'from': 'enabled',
                'to':'disabled'
            }
        }
    }
        
    assert dp_diff.matching_prim_keys(dp_state_resp, proposed_valcred)
    dup_keys = dp_diff.get_duplicate_keys(dp_state_resp['CryptoValCred'], proposed_valcred['CryptoValCred'])
    assert dup_keys == {'name', 'mAdminState'}


    diff_keys = dp_diff.get_diff_keys(dp_state_resp['CryptoValCred'], proposed_valcred['CryptoValCred'])
    assert diff_keys == {'mAdminState'}