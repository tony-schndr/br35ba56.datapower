from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPManageConfigRequest,
    DPGetConfigRequest,
    DPActionQueueRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPManageConfigObject,
    DPManageConfigSchema
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.actionqueue import (
    DPActionQueue
)
from ansible_collections.community.datapower.tests.unit.module_utils.test_data import (
    dp_mgmt_test_data as test_data,
    dp_actionq_test_data as action_test_data
)
# Tests building requests objects from the DPManageConfigObject.

def test_DPActionQueueRequest_1():
    task_args = {
        'domain':'default',
        'action': 'SaveConfig',
        'parameters': None
    }
    valid_actions = action_test_data.valid_actions

    dp_action = DPActionQueue(**task_args)
    dp_action_req = DPActionQueueRequest(dp_action)
    assert dp_action_req.path == '/mgmt/actionqueue/default'
    assert dp_action_req.body == {
            'SaveConfig' : {}
        }
    assert dp_action_req.info_path == '/mgmt/actionqueue/default/operations/SaveConfig?schema-format=datapower'
    
    #ACTION_QUEUE_SCHEMA_URI = '/mgmt/actionqueue/{0}/{1}?schema-format=datapower'
    #ACTION_QUEUE_OPERATIONS_URI = '/mgmt/actionqueue/{0}/operations'
def test_DPActionQueueRequest_2():
    task_args = {
        'domain':'default',
        'action': 'TraceRoute',
        'parameters': {
            'RemoteHost': 'www.google.com'
        }
    }
    valid_actions = action_test_data.valid_actions

    dp_action = DPActionQueue(**task_args)
    dp_action_req = DPActionQueueRequest(dp_action)
    assert dp_action_req.path == '/mgmt/actionqueue/default'
    assert dp_action_req.body == {
            'TraceRoute' : {'RemoteHost': 'www.google.com'}
        }
    assert dp_action_req.info_path == '/mgmt/actionqueue/default/operations/TraceRoute?schema-format=datapower'
    
    #ACTION_QUEUE_SCHEMA_URI = '/mgmt/actionqueue/{0}/{1}?schema-format=datapower'
    #ACTION_QUEUE_OPERATIONS_URI = '/mgmt/actionqueue/{0}/operations'


'''
def test_DPManageConfigRequest_w_field():
    task_args = {
        'domain':'snafu',
        'name': 'valcred',
        'class_name' :'CryptoValCred',
        'config': {
            'mAdminState':'disabled'            
        },
        'overwrite': True
    }
    
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    dp_req = DPManageConfigRequest(dp_mgmt_conf)
    #assert dp_req.path ==  '/mgmt/config/snafu/CryptoValCred/valcred/mAdminState'
    assert dp_req.method == 'PUT'
   # assert list(dp_mgmt_conf.config.keys())[0]  in dp_req.path
    assert dp_req.body == dp_mgmt_conf.config
'''

def test_DPManageConfigRequest_mod_args():
    task_args = {
        "class_name": None,
        "config": {
            "CryptoValCred": {
                "mAdminState": "enabled",
                "name": "valcred"
            }
        },
        "domain": "default",
        "name": None,
        "state": 'present'
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    dp_req = DPManageConfigRequest(dp_mgmt_conf)
    assert dp_req.path ==  '/mgmt/config/default/CryptoValCred/valcred'
    assert dp_req.method == 'PUT'
    assert dp_req.body == {
            "CryptoValCred": {
                "mAdminState": "enabled",
                "name": "valcred"
            }
        }

def test_DPManageConfigRequest_min():
    task_args = {
        'domain':'snafu',
        'config': {
            'CryptoValCred' : {
                'name':'valcred',
                'mAdminState':'disabled'
            }
        },
        'state': 'present'
    }

    dp_mgmt_conf = DPManageConfigObject(**task_args)
    dp_req = DPManageConfigRequest(dp_mgmt_conf)
    assert dp_req.path ==  '/mgmt/config/snafu/CryptoValCred/valcred'
    assert dp_req.method == 'PUT'

def test_DPManageConfigRequest_w_name():
    task_args = {
        'domain':'snafu',
        'config': {
            'CryptoValCred' : {
                'name':'valcred'
            }
        },
        'state': 'present'
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    dp_req = DPManageConfigRequest(dp_mgmt_conf)
    assert dp_req.path ==  '/mgmt/config/snafu/CryptoValCred/valcred'
'''
def test_DPManageConfigRequest_schema_array_1():
    task_args = {
        'domain':'snafu',
        'config': {
            'CryptoValCred': {
                'name': 'valcred',
                'Certificate': {
                    'Test2'
                }
            }
        },
        'overwrite': True
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    assert dp_mgmt_conf.name == 'valcred'
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    req = DPManageConfigRequest(dp_mgmt_conf, schema)
    assert req.check_for_array(dp_mgmt_conf.config, dp_mgmt_conf.class_name)
    assert req.body == {'Certificate': {'Test2' } }
    assert req.path == '/mgmt/config/snafu/CryptoValCred/valcred/Certificate'
    assert req.method == 'PUT'

def test_DPManageConfigRequest_schema_array_2():
    task_args = {
        'domain':'snafu',
        'name':'valcred',
        'config': {
            'CryptoValCred': {
                'Certificate': {
                    'Test2'
                }
            }
        },
        'overwrite': True
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    req = DPManageConfigRequest(dp_mgmt_conf, schema)
    assert req.check_for_array(dp_mgmt_conf.config, dp_mgmt_conf.class_name)
    assert req.body == {'Certificate': {'Test2' } }
    assert req.path == '/mgmt/config/snafu/CryptoValCred/valcred/Certificate'
    assert req.method == 'PUT'

def test_DPManageConfigRequest_schema_array_3():
    task_args = {
        'domain':'snafu',
        'class_name':'CryptoValCred',
        'name':'valcred',
        'config': {
            'Certificate': {
                'Test2'
            }
        },
        'overwrite': True
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    req = DPManageConfigRequest(dp_mgmt_conf, schema)
    assert req.check_for_array(dp_mgmt_conf.config, dp_mgmt_conf.class_name)
    assert req.body == {'Certificate': {'Test2'}}
    assert req.path == '/mgmt/config/snafu/CryptoValCred/valcred/Certificate'
    assert req.method == 'PUT'
    
def test_DPManageConfigRequest_schema_not_array_1():
    task_args = {
        'domain':'snafu',
        'class_name':'CryptoValCred',
        'name':'valcred',
        'config': {
            'mAdminState': 'disabled'
        },
        'overwrite': True
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    req = DPManageConfigRequest(dp_mgmt_conf, schema)
    assert req.check_for_array(dp_mgmt_conf.config, dp_mgmt_conf.class_name) == False
    assert req.body == {
            'CryptoValCred': {
                 'mAdminState': 'disabled',
                 'name':'valcred'
            }
        }
def test_DPManageConfigRequest_schema_not_array_2():
    task_args = {
        'domain':'snafu',
        'class_name':'CryptoValCred',
        'config': {
            'mAdminState': 'disabled',
            'name':'valcred'
        },
        'overwrite': True
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    assert DPManageConfigRequest(dp_mgmt_conf, schema).check_for_array(dp_mgmt_conf.config, dp_mgmt_conf.class_name) == False
 
def test_DPManageConfigRequest_schema_not_array_3():
    task_args = {
        'domain':'snafu',
        'class_name':'CryptoValCred',
        'config': {
            'CryptoValCred' : {
                'mAdminState': 'disabled',
                'name':'valcred'
            }
        },
        'overwrite': True
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    assert DPManageConfigRequest(dp_mgmt_conf, schema).check_for_array(dp_mgmt_conf.config, dp_mgmt_conf.class_name) == False
 
 
def test_DPManageConfigRequest_schema_not_array_4():
    task_args = {
        'domain':'snafu',
        'class_name':'CryptoValCred',
        'config': {
            'CryptoValCred' : {
                'mAdminState': 'disabled',
                'name':'valcred',
                'Certificate' : {
                    'Test1'
                }
            }
        },
        'overwrite': True
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    schema = DPManageConfigSchema(test_data.valcred_schema_resp)
    req = DPManageConfigRequest(dp_mgmt_conf, schema)
    assert req.check_for_array(dp_mgmt_conf.config, dp_mgmt_conf.class_name) == False

'''
def test_DPManageConfigRequest_invalid_class():
    task_args_w_invalid_class = {
        'domain':'snafu',
        'config': {
            'ValidationCredential' : {
                'name':'valcred'
            }
        },
        'state': 'present'
    }
    try:
        DPManageConfigObject(**task_args_w_invalid_class)
    except ValueError:
        assert True


def test_DPGetConfigRequest_1():
    get_task_args = {
        'domain':'snafu',
        'name': 'valcred',
        'config': {
            'CryptoValCred' : {
                'name':'valcred'
            }
        },
        'overwrite': True,
        'recursive':True,
        'status': True,
        'depth': 3
    }

    dp_mgmt_conf = DPManageConfigObject(**get_task_args)
    dp_req = DPGetConfigRequest(dp_mgmt_conf)
    assert dp_req.options == {
        'view': 'recursive',
        'state': 1,
        'depth' : 3
    }
    assert 'state=1' in dp_req.path and 'depth=3' in dp_req.path and 'view=recursive' in dp_req.path
    
    dp_mgmt_conf.depth = None
    dp_req = DPGetConfigRequest(dp_mgmt_conf)
    assert dp_req.options == {
        'view': 'recursive',
        'state': 1,
        'depth': 2
    }

    assert 'state=1' in dp_req.path and 'depth=2' in dp_req.path and 'view=recursive' in dp_req.path
    dp_mgmt_conf.recursive = False

    dp_req = DPGetConfigRequest(dp_mgmt_conf)
    assert dp_req.options == {
        'state': 1
    }
    assert 'state=1' in dp_req.path

