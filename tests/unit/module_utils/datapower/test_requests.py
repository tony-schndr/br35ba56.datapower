from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPManageConfigRequest,
    DPGetConfigRequest,
    DPActionQueueRequest,
    DPActionQueueSchemaRequest,
    DPFileStoreRequests,
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPManageConfigObject
)

from ansible_collections.community.datapower.plugins.module_utils.datapower.actionqueue import (
    DPActionQueue
)
from ansible_collections.community.datapower.tests.unit.module_utils.test_data import (
    dp_mgmt_test_data as test_data,
    dp_actionq_test_data as action_test_data,
    files_data
)

def test_DPFileStoreRequests_create_dir_request():
    domain = 'default'
    top_directory = 'local'
    dir_path = 'dir/subdir'
    req = DPFileStoreRequests.create_dir_request(domain, top_directory, dir_path)
    assert req == ('/mgmt/filestore/default/local', 'POST', {"directory": { "name": 'dir/subdir' }})

def test_DPFileStoreRequests_get_dir_request():
    domain = 'default'
    top_directory = 'local'
    dir_path = 'dir/subdir'
    
    req = DPFileStoreRequests.get_dir_request(domain, top_directory, dir_path)
    assert req == ('/mgmt/filestore/default/local/dir/subdir', 'GET', None)


def test_DPFileStoreRequests_create_file_request():
    
    domain = 'default'
    top_directory = 'local'
    file_path = 'dir/subdir/get.js'
    content = 'aGVsbG8gd29ybGQK'
    req = DPFileStoreRequests.create_file_request(domain, top_directory, file_path, content)
    assert req == ('/mgmt/filestore/default/local/dir/subdir', 'POST', {'file':{'name':'get.js', 'content': content}})


def test_DPFileStoreRequests_update_file_request():
    domain = 'default'
    top_directory = 'local'
    file_path = 'dir/subdir/get.js'
    content = 'aGVsbG8gd29ybGQK'
    req = DPFileStoreRequests.update_file_request(domain, top_directory, file_path, content)
    assert req == ('/mgmt/filestore/default/local/dir/subdir/get.js', 'PUT', {'file':{'name':'get.js', 'content': content}})


def test_DPFileStoreRequests_delete_file_request():
    domain = 'default'
    top_directory = 'local'
    file_path = 'dir/subdir/get.js'
    req = DPFileStoreRequests.delete_file_request(domain, top_directory, file_path)
    assert req == ('/mgmt/filestore/default/local/dir/subdir/get.js', 'DELETE', None)


def test_DPFileStoreRequests_get_file_request():
    domain = 'default'
    top_directory = 'local'
    file_path = 'dir/subdir/get.js'
    req = DPFileStoreRequests.get_file_request(domain, top_directory, file_path)
    assert req == ('/mgmt/filestore/default/local/dir/subdir/get.js', 'GET', None)



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
 
def test_DPActionQueueSchemaRequest():
    task_args = {
        'domain':'default',
        'action': 'SaveConfig'
    }

    dp_action = DPActionQueue(**task_args)
    dp_action_req = DPActionQueueSchemaRequest(dp_action)
    assert dp_action_req.path == '/mgmt/actionqueue/default/operations/SaveConfig?schema-format=datapower'
    

def test_DPActionQueueRequest_2():
    task_args = {
        'domain':'default',
        'action': 'TraceRoute',
        'parameters': {
            'RemoteHost': 'www.google.com'
        }
    }

    dp_action = DPActionQueue(**task_args)
    dp_action_req = DPActionQueueRequest(dp_action)
    assert dp_action_req.path == '/mgmt/actionqueue/default'
    assert dp_action_req.body == {
            'TraceRoute' : {'RemoteHost': 'www.google.com'}
        }

    #ACTION_QUEUE_SCHEMA_URI = '/mgmt/actionqueue/{0}/{1}?schema-format=datapower'
    #ACTION_QUEUE_OPERATIONS_URI = '/mgmt/actionqueue/{0}/operations'

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

