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

def test_DPManageConfigObject_schema():
    assert DPManageConfigSchema(test_data.config_info_schema_response)
    
def test_DPManageConfigObject_schema_get_prop():   
    dp_schema = DPManageConfigSchema(test_data.config_info_schema_response)
    assert dp_schema.get_prop('Certificate')
    assert dp_schema.get_prop('nothing') == None

def test_DPManageConfigObject_schema_get_prop_test_type_is_set():   
    dp_schema = DPManageConfigSchema(test_data.config_info_schema_response)
    assert dp_schema.get_prop('Certificate')['type']['name']== 'dmReference'
    assert dp_schema.get_prop('mAdminState')['type']['name']== 'dmAdminState'       

def test_DPManageConfigObject_schema_get_prop_type():   
    dp_schema = DPManageConfigSchema(test_data.config_info_schema_response)
    assert dp_schema.get_prop_type(test_data.config_info_schema_response, '/mgmt/types/default/dmString') == {
            "cli-arg": "string",
            "name": "dmString"
    }

def test_DPManageConfigObject_schema_get_is_valid_param():   
    dp_schema = DPManageConfigSchema(test_data.config_info_schema_response)
    assert dp_schema.get_prop_type(test_data.config_info_schema_response, '/mgmt/types/default/dmString') == {
            "cli-arg": "string",
            "name": "dmString"
    }
