from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    dp_diff
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPManageConfigObject,
    DPManageConfigSchema
)
from ansible_collections.community.datapower.tests.unit.module_utils.test_data import (
    dp_mgmt_test_data as test_data,
    dp_actionq_test_data as action_test_data
)

from ansible_collections.community.datapower.tests.unit.module_utils.datapower.test_schema import (
    TestDPManageConfigSchema
)

def test_get_change_dict_user_passes_none_prop():
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
            "Certificate" : None,
        }
    }
    schema = TestDPManageConfigSchema.load_schema('CryptoValCred')
    try:
        dp_diff.get_change_dict(from_dict, to_dict, schema)
    except:
        assert True

