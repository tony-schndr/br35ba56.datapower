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
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    try:
        dp_diff.get_change_dict(from_dict, to_dict, schema)
    except:
        assert True


def test_get_change_dict_user_passes_Value():
    from_dict = { 
        "CryptoValCred": {
            "CRLDPHandling": "ignore",
            "CertValidationMode": "legacy",
            "CheckDates": "on",
            "ExplicitPolicy": "off",
            "RequireCRL": "off",
            "UseCRL": "off",
            "mAdminState": "enabled",
            "name": "valcred"
        }
    }

    to_dict = {
        "CryptoValCred": {
            "Certificate": [
                {
                    "Value": "Test1"
                },
                {
                    "Value": "Test2"
                }
            ],
            "UseCRL": "off",
            "mAdminState": "enabled",
            "name": "valcred"
        }
    }

    change_dict = {
        "CryptoValCred": {
            "name": "valcred",
            "RequireCRL": "on",
            "ExplicitPolicy": "on",
            "Certificate" : [
                {
                    "Value": "Test1"
                },
                {
                    "Value": "Test2"
                }
            ]
        }
    }
    
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    try:
        dp_diff.get_change_dict(from_dict, to_dict, schema) 
    except:
        return True


def test_get_change_dict_user_passes_empty_prop():
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
            "Certificate" : {}
        }
    }
    change_dict = {
        "CryptoValCred": {
            "name": "valcred",
            "RequireCRL": "on",
            "ExplicitPolicy": "on",
            "Certificate" : {}
        }
    }
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    assert dp_diff.get_change_dict(from_dict, to_dict, schema) == change_dict



def test_get_change_dict():
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
            "UseCRL": "on"
        }
    }
    change_dict = {
        "CryptoValCred": {
            "name": "valcred",
            "RequireCRL": "on",
            "ExplicitPolicy": "on",
        }
    }
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    assert dp_diff.get_change_dict(from_dict, to_dict, schema) == change_dict

#Handles case where DataPower returns dictionary and the user passes a list with 1 item.
def test_get_change_dict_to_array_from_dict():
    from_dict =  {
        "CryptoValCred": {
            "CRLDPHandling": "ignore",
            "CertValidationMode": "legacy",
            "Certificate": {
                 "value": "Test1"
            },
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
                }
            ],
        }
    }
    change_dict = {
        "CryptoValCred": {
            "name": "valcred",
            "RequireCRL": "on",
            "ExplicitPolicy": "on"
        }
    }
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    assert dp_diff.get_change_dict(from_dict, to_dict, schema) == change_dict

#Handles case where DataPower returns dictionary and the user passes a list with 1 item.
def test_get_change_dict_to_array_from_dict_not_equal():
    from_dict =  {
        "CryptoValCred": {
            "CRLDPHandling": "ignore",
            "CertValidationMode": "legacy",
            "Certificate": {
                 "value": "Test1"
            },
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
            ],
        }
    }
    change_dict = {
        "CryptoValCred": {
            "name": "valcred",
            "RequireCRL": "on",
            "ExplicitPolicy": "on",
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
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    assert dp_diff.get_change_dict(from_dict, to_dict, schema) == change_dict


def test_get_change_dict_user_passes_arrays_not_equal():
    from_dict =  {
        "CryptoValCred": {
            "CRLDPHandling": "ignore",
            "CertValidationMode": "legacy",
            "Certificate": 
            [
                {
                 "value": "Test2"
                },
                {
                 "value": "Test1"
                },
                {
                 "value": "Test3"
                }  
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

    to_dict = {
        "CryptoValCred": {
            "CRLDPHandling": "ignore",
            "CertValidationMode": "legacy",
            "Certificate": 
            [
                {
                 "value": "Test2"
                },
                {
                 "value": "Test4"
                },
                {
                 "value": "Test3"
                }  
            ],
            "CheckDates": "on",
            "ExplicitPolicy": "on",
            "InitialPolicySet": "2.5.29.32.0",
            "RequireCRL": "off",
            "UseCRL": "on",
            "mAdminState": "enabled",
            "name": "valcred"
        }
    }
    change_dict = {
        "CryptoValCred": {
            "name": "valcred",
            "ExplicitPolicy": "on",
            "Certificate": [
                {
                 "value": "Test2"
                },
                {
                 "value": "Test4"
                },
                {
                 "value": "Test3"
                }  
            ],
        }
    }
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    assert dp_diff.get_change_dict(from_dict, to_dict, schema) == change_dict


