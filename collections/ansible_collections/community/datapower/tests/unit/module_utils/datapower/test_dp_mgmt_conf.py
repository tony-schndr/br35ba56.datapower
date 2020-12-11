from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.dp_mgmt_conf import (
    DPManageConfigObject,
    DPManageConfigSchema,
    DPProperty
)

from ansible_collections.community.datapower.tests.unit.module_utils.test_data import (
    dp_mgmt_test_data as test_data
)
# Tests building requests objects from the DPManageConfigObject.  Request objects are 
# passed to the request handlers

def test_DPManageConfigObject():
    task_args = {
        'domain':'snafu',
        'config': {
            'CryptoValCred' : {
                'name':'valcred'
            }
        },
        'overwrite': True
    }
    schema_resp = test_data.valcred_schema_resp
    mgmt_conf_schema = DPManageConfigSchema(schema_resp)

    dp_mgmt_conf = DPManageConfigObject(**task_args)
    assert dp_mgmt_conf.class_name == 'CryptoValCred'
    assert dp_mgmt_conf.name == 'valcred'
    assert dp_mgmt_conf.config == task_args['config']
    assert dp_mgmt_conf.domain == task_args['domain']
    assert dp_mgmt_conf.overwrite == task_args['overwrite']

def test_DPManageConfigObject_schema():
    
    schema_resp = test_data.valcred_schema_resp
    mgmt_conf_schema = DPManageConfigSchema(schema_resp)
    for prop in mgmt_conf_schema.props:
        assert isinstance(prop, DPProperty)
        if hasattr(prop, 'array'):
            assert prop.array
        assert hasattr(prop, 'name')
        assert hasattr(prop, 'type')

def test_DPManageConfigObject_schema_get_prop():   
    dp_schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    assert dp_schema.get_prop('Certificate')
    assert dp_schema.get_prop('nothing') == None



    
            


