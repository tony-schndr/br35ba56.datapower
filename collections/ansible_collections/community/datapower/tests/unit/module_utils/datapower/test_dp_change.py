from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    dp_change
)

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
            "CheckDates": "off"
        }
    }

    compared_valcred = {
        "CryptoValCred": {
            'name':'valcred',
            "Certificate": {
                'to': [
                    {
                        "value": "Test1"
                    },
                    {
                        "value": "demo_Cert"
                    }
                ],
                'from': {
                    "value": "Test1"
                },
            },
            "CheckDates": {
                'from': 'on',
                'to': "off"
            }
        }
    }
        
    assert dp_change.DPChange.state_diff(current_valcred, proposed_valcred) == compared_valcred


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

    try:
        dp_change.DPChange.state_diff(current_valcred, proposed_valcred)
    except TypeError:
        assert True
    else:
        assert False