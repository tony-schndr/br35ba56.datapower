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

def test_DPManageConfigSchema():
    assert DPManageConfigSchema(test_data.config_info_schema_response)
    
def test_DPManageConfigSchema_get_prop():   
    dp_schema = DPManageConfigSchema(test_data.config_info_schema_response)
    assert dp_schema.get_prop('Certificate')
    assert dp_schema.get_prop('nothing') == None

def test_DPManageConfigSchema_get_prop_href():   
    dp_schema = DPManageConfigSchema(test_data.config_info_schema_response)
    href = dp_schema.get_prop_href(dp_schema.get_prop('Certificate'))
    assert href ==  "/mgmt/types/default/dmReference"
    href = dp_schema.get_prop_href(dp_schema.get_prop('mAdminState'))
    assert href == "/mgmt/types/default/dmAdminState"

def test_DPManageConfigSchema_get_prop_test_type_is_set():   
    dp_schema = DPManageConfigSchema(test_data.config_info_schema_response)
    href = dp_schema.get_prop_href(dp_schema.get_prop('Certificate'))
    assert dp_schema.get_prop('Certificate')[href]['type']['name']== 'dmReference'
    href = dp_schema.get_prop_href(dp_schema.get_prop('mAdminState'))
    assert dp_schema.get_prop('mAdminState')[href]['type']['name']== 'dmAdminState'       

def test_DPManageConfigSchema_get_prop_type():   
    dp_schema = DPManageConfigSchema(test_data.config_info_schema_response)
    assert dp_schema.get_prop_type(test_data.config_info_schema_response, '/mgmt/types/default/dmString') == {
        "_links": {
            "doc": {
                "href": "/mgmt/docs/types/dmString"
            },
            "self": {
                "href": "/mgmt/types/default/dmString"
            }
        },
        "type": {
            "cli-arg": "string",
            "name": "dmString"
        }
    }

def test_DPManageConfigSchema_get_is_valid_param():
    dp_schema = DPManageConfigSchema(test_data.config_info_schema_response)
    assert dp_schema.is_valid_param('mAdminState', 'disabled')
    assert dp_schema.is_valid_param('Certificate', {'value': 'Test1'})
    assert dp_schema.is_valid_param('Certificate', {'Value': 'Test1'}) == False
    assert dp_schema.is_valid_param('ExplicitPolicy', 'on')
    assert dp_schema.is_valid_param('ExplicitPolicy', 'foo') == False
    assert dp_schema.is_valid_param('InitialPolicySet', 'anystring')
    assert dp_schema.is_valid_param('InitialPolicySet', 2) == False
    

def test_DPManageConfigSchema_with_EthernetInterface_type():
    dp_schema = DPManageConfigSchema(test_data.schema_ethernet_interface)
    assert dp_schema.is_valid_param('mAdminState', 'disabled')


def test_DPManageConfigSchema_schema_get_type_int_boundries():
    type_ = test_data.int_type
    dp_schema = DPManageConfigSchema(test_data.schema_ethernet_interface)
    assert dp_schema.get_type_int_boundries(type_) == (0, 65535)
