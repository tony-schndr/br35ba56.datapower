from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest
'''
from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    config_diff
)

def test_config_diff_basic():
    current_state = { 
        'a': 1,
        'b': 3,
        'c': 5
    }

    proposed_state = { 
        'a': 2,
        'b': 5,
        'c': 5
    }

    diff_dict ={ 
        'a': {
            'from': 1,
            'to' : 2
        },
        'b': {
            'from': 3,
            'to' : 5
        }
    }
    assert config_diff.get_diff_keys(current_state, proposed_state) == set({'a','b'})
    assert config_diff.dict_diff(current_state, proposed_state) == diff_dict

def test_config_diff_dict_to_list():
    current_state = { 
        'a': 1,
        'b': 3,
        'c': 5
    }

    proposed_state = { 
        'a': 2,
        'b': [ 1, 2, 3],
        'c': 5
    }

    diff_dict = { 
        'a': {
            'from': 1,
            'to' : 2
        },
        'b': {
            'from': 3,
            'to' : [
                1, 2, 3
            ]
        }
    }
    assert config_diff.get_diff_keys(current_state, proposed_state) == set({'a','b'})
    assert config_diff.dict_diff(current_state, proposed_state) == diff_dict


def test_dp_valcred_state():
    current_valcred = {
        "CryptoValCred": {
            "name": "valcred",
            "mAdminState": "enabled",
            "Certificate": {
                "value": "Test1"
            },
            "CertValidationMode": "legacy",
            "UseCRL": "on",
            "RequireCRL": "off",
            "CRLDPHandling": "ignore",
            "InitialPolicySet": "2.5.29.32.0",
            "ExplicitPolicy": "off",
            "CheckDates": "on"
        }
    }
    proposed_valcred = {
        "CryptoValCred": {
            "name": "valcred",
            "mAdminState": "enabled",
            "Certificate": [
                {
                    "value": "Test1"
                },
                {
                    "value": "demo_Cert"
                }
            ],
            "CertValidationMode": "legacy",
            "UseCRL": "on",
            "RequireCRL": "off",
            "CRLDPHandling": "ignore",
            "InitialPolicySet": "2.5.29.32.0",
            "ExplicitPolicy": "off",
            "CheckDates": "on"
        }
    }
    dup_keys = config_diff.get_duplicate_keys(current_valcred, proposed_valcred)
    assert len(dup_keys) == 1
    assert config_diff.matching_prim_keys(current_valcred, proposed_valcred)
    assert config_diff.get_diff_keys(current_valcred['CryptoValCred'], proposed_valcred['CryptoValCred']) == set({'Certificate'})


def test_config_diff_mismatch_objects():
    dict1 = {
        "CryptoValCred": {
            "name": "valcred",
            "mAdminState": "enabled",
            "Certificate": {
                "value": "Test1"
            },
            "CertValidationMode": "legacy",
            "UseCRL": "on",
            "RequireCRL": "off",
            "CRLDPHandling": "ignore",
            "InitialPolicySet": "2.5.29.32.0",
            "ExplicitPolicy": "off",
            "CheckDates": "on"
        }
    }
    dict2 = {
        "CryptoCertificate": {
            "name": "Test1",
            "mAdminState": "enabled",
            "Filename": "cert:///webgui-sscert.pem",
            "PasswordAlias": "off",
            "IgnoreExpiration": "off"
        }
    }
    assert config_diff.matching_prim_keys(dict1, dict2) == False
'''