from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    dp_diff
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPManageConfigObject
)
from ansible_collections.community.datapower.tests.unit.module_utils.test_data import (
    dp_mgmt_test_data as test_data,
    dp_actionq_test_data as action_test_data
)

def test_get_changes_valcred_1():
    from_dict =  {
        "CryptoValCred": {
            "CRLDPHandling": "ignore",
            "CertValidationMode": "legacy",
            "CheckDates": "on",
            "ExplicitPolicy": "off",
            "InitialPolicySet": "2.5.29.32.0",
            "RequireCRL": "off",
            "UseCRL": "on",
            "mAdminState": "enabled",
            "name": "valcred",
            "Certificate": [
                {
                    "value": "Test1"
                },
                {
                    "value": "Test1"
                }
            ]
        }
    }

    to_dict = {
        "CryptoValCred": {
            "name": "valcred",
            "mAdminState": "enabled",
            "CheckDates": "on",
            "ExplicitPolicy": "on",
            "InitialPolicySet": "2.5.29.32.0",
            "RequireCRL": "on",
            "UseCRL": "on",
        }
    }
    changes = [
        {
            "path": "CryptoValCred.ExplicitPolicy",
            "diff": {
                "from": "off",
                "to": "on"
            }
        },
        {
            "path": "CryptoValCred.RequireCRL",
            "diff": {
                "from": "off",
                "to": "on"
            }
        }
    ]

    assert list(dp_diff.get_changes(from_dict, to_dict)) == changes


def test_get_changes_valcred_array_to_array_with_diff_order_but_same_elements():
    from_dict =  {
        "CryptoValCred": {
            "CRLDPHandling": "ignore",
            "CertValidationMode": "legacy",
            "CheckDates": "on",
            "ExplicitPolicy": "off",
            "InitialPolicySet": "2.5.29.32.0",
            "RequireCRL": "off",
            "UseCRL": "on",
            "mAdminState": "enabled",
            "name": "valcred",
            "Certificate":[
                {
                    "value": "Test1"
                },
                {
                    "value": "Test2"
                }
            ]
            
        }
    }

    to_dict = {
        "CryptoValCred": {
            "CRLDPHandling": "ignore",
            "CertValidationMode": "legacy",
            "CheckDates": "on",
            "ExplicitPolicy": "off",
            "InitialPolicySet": "2.5.29.32.0",
            "RequireCRL": "off",
            "UseCRL": "on",
            "mAdminState": "enabled",
            "name": "valcred",
            "Certificate":[
                {
                    "value": "Test2"
                },
                {
                    "value": "Test1"
                }
            ]
        }
    }

    assert len(list(dp_diff.get_changes(from_dict, to_dict))) == 2


def test_get_changes_aaa_policy():
    from_dict = test_data.AAA_Policy_from
    to_dict = test_data.AAA_Policy_to

    assert len(list(dp_diff.get_changes(from_dict, to_dict))) == 2


def test_is_changed():
    from_dict = test_data.AAA_Policy_from
    to_dict = test_data.AAA_Policy_to

    assert dp_diff.is_changed(from_dict, to_dict)
    to_dict = test_data.AAA_Policy_from
    assert dp_diff.is_changed(from_dict, to_dict) == False

def test_get_patched_dict_valcred_2():

    from_dict =  {
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
        }
    }

    to_dict = {
        "CryptoValCred": {
            "name": "valcred",
            "mAdminState": "enabled",
            "CheckDates": "on",
            "ExplicitPolicy": "on",
            "InitialPolicySet": "2.5.29.32.0",
            "RequireCRL": "on",
            "UseCRL": "on",
            "Certificate": [
                {
                    "value": "Test1"
                },
                {
                    "value": "Test2"
                }
            ]
        }
    }
    patched ={
        "CryptoValCred": {
            "CheckDates": "on",
            "ExplicitPolicy": "on",
            "InitialPolicySet": "2.5.29.32.0",
            "RequireCRL": "on",
            "UseCRL": "on",
            "mAdminState": "enabled",
            "name": "valcred",
            "Certificate": [
                {
                    "value": "Test1"
                },
                {
                    "value": "Test2"
                }
            ]
        }
    }
    assert dp_diff.get_patched_dict(from_dict, to_dict) == patched
