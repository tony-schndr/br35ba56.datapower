from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    diff
)

from ansible_collections.community.datapower.tests.unit.module_utils.test_data import (
    dp_mgmt_test_data as test_data
)


def test_get_changes_valcred_1():
    from_dict = {
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
            "Certificate":[]
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

    raise Exception(diff.config_diff(to_dict, from_dict))