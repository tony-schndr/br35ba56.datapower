from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPManageConfigRequest,
    DPGetConfigRequest
)

from ansible_collections.community.datapower.plugins.module_utils.datapower.dp_obj import (
    DPManageConfigObject
)


def test_DPApplyConfig():
    task_args = {
        'domain':'snafu',
        'config': {
            'CryptoValCred' : {
                'name':'valcred'
            }
        },
        'overwrite': True,
        'object_field' : None,
        'state': 'present'
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    assert dp_mgmt_conf.class_name == 'CryptoValCred'
    assert dp_mgmt_conf.object_name == 'valcred'
    assert dp_mgmt_conf.config == task_args['config']
    assert dp_mgmt_conf.domain == task_args['domain']
    assert dp_mgmt_conf.overwrite == task_args['overwrite']

def test_DPManageConfigRequest_w_field():
    task_args = {
        'domain':'snafu',
        'object_name': 'valcred',
        'config': {
            'CryptoValCred' : {
                'name':'valcred'
            }
        },
        'overwrite': True,
        'state': 'present',
        'object_field': 'Certificate'
    }
    
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    dp_req = DPManageConfigRequest(dp_mgmt_conf)
    #assert dp_req.path ==  '/mgmt/config/snafu/CryptoValCred/valcred/Certificate'
    assert dp_req.method == 'PUT'
    assert dp_req.body == dp_mgmt_conf.config

def test_DPManageConfigRequest_min():
    task_args = {
        'domain':'snafu',
        'config': {
            'CryptoValCred' : {
                'mAdminState':'disabled'
            }
        },
        'overwrite': False,
        'object_field' : None,
        'state': 'present'
    }

    dp_mgmt_conf = DPManageConfigObject(**task_args)
    dp_req = DPManageConfigRequest(dp_mgmt_conf)
    assert dp_req.path ==  '/mgmt/config/snafu/CryptoValCred'
    assert dp_req.method == 'POST'

def test_DPManageConfigRequest_w_name():
    task_args = {
        'domain':'snafu',
        'config': {
            'CryptoValCred' : {
                'name':'valcred'
            }
        },
        'overwrite': True,
        'object_field' : None,
        'state': 'present'
    }
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    dp_req = DPManageConfigRequest(dp_mgmt_conf)
    assert dp_req.path ==  '/mgmt/config/snafu/CryptoValCred/valcred'


def test_DPManageConfigRequest_invalid_class():
    task_args_w_invalid_class = {
        'domain':'snafu',
        'object_name': 'valcred',
        'config': {
            'ValidationCredential' : {
                'name':'valcred'
            }
        },
        'overwrite': True,
        'state': 'present',
        'object_field': 'Certificate'
    }
    try:
        dp_mgmt_conf = DPManageConfigObject(**task_args_w_invalid_class)
    except ValueError:
        assert True


def test_DPGetConfigRequest():
    get_task_args = {
        'domain':'snafu',
        'object_name': 'valcred',
        'config': {
            'CryptoValCred' : {
                'name':'valcred'
            }
        },
        'overwrite': True,
        'state': 'present',
        'object_field': 'Certificate',
        'recursive':True,
        'state':True,
        'depth': 3
    }
    options = {
        'view': True,
        'state': 1,
        'depth' : 3
    }
    dp_mgmt_conf = DPManageConfigObject(**get_task_args)
    dp_req = DPGetConfigRequest(dp_mgmt_conf)
    assert dp_req.options == {
        'view': True,
        'state': 1,
        'depth' : 3
    }
    dp_mgmt_conf.depth = None
    dp_req = DPGetConfigRequest(dp_mgmt_conf)
    assert dp_req.options == {
        'view': True,
        'state': 1,
        'depth': 2
    }
    dp_mgmt_conf.recursive = False

    dp_req = DPGetConfigRequest(dp_mgmt_conf)
    assert dp_req.options == {
        'state': 1
    }
    assert 'state=1' in dp_req.path