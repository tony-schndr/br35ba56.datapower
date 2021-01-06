from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPManageConfigRequest,
    DPGetConfigRequest,
    DPActionQueueRequest,
    DPFileStoreRequest,
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPManageConfigObject
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.filestore import (
    DPFileStore
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.actionqueue import (
    DPActionQueue
)
from ansible_collections.community.datapower.tests.unit.module_utils.test_data import (
    dp_mgmt_test_data as test_data,
    dp_actionq_test_data as action_test_data,
    files_data
)
# Tests building requests objects from the DPManageConfigObject.


def test_DPFileStoreRequest_get_body():
    dir = '/local/test1/'
    assert DPFileStoreRequest.get_body(dir) == { 
        'directory': {
            'name' : dir
        }
    }

def test_DPFileStoreRequest_get_path_type_dir():
    params = {
        'domain': 'default',
        'content': None,
        'src': './tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
        'dest': '/local/GetStat',
        'overwrite': True,
        'state': 'directory'
    }
    fs = DPFileStore(params)
    fs_req = DPFileStoreRequest(fs)
    assert fs_req.get_dir_path('default', 'local') == '/mgmt/filestore/default/local'

def test_DPFileStoreRequest_get_dir_reqs():
    params = {
        'domain': 'default',
        'content': None,
        'src': './tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
        'dest': '/local/GetStat',
        'overwrite': True,
        'state': 'directory'
    }
    fs = DPFileStore(params)
    fs_req = DPFileStoreRequest(fs)
    requests = [
        ('/mgmt/filestore/default/local', 'GET', {'directory': {'name': 'GetStat/'}}),
        ('/mgmt/filestore/default/local', 'GET', {'directory': {'name': 'GetStat/Route'}}),
        ('/mgmt/filestore/default/local', 'GET', {'directory': {'name': 'GetStat/Processing'}}),
        ('/mgmt/filestore/default/local', 'GET', {'directory': {'name': 'GetStat/Processing/Route'}})
    ]

    assert list(fs_req.dir_reqs()) == requests

def test_DPFileStoreRequest_get_file_reqs():
    params = {
        'domain': 'default',
        'content': None,
        'src': './tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
        'dest': '/local/GetStat',
        'overwrite': True,
        'state': 'directory'
    }
    fs = DPFileStore(params)
    fs_req = DPFileStoreRequest(fs)
    assert sorted(list(fs_req.file_reqs())) == sorted(files_data.file_reqs)

def test_DPFileStoreRequest_get_file_req_root_dest():
    params = {
        'domain': 'default',
        'content': None,
        'src': './tests/unit/module_utils/test_data/copy/test.txt',
        'dest': '/local/',
        'overwrite': True,
        'state': 'file'
    }
    fs = DPFileStore(params)
    fs_req = DPFileStoreRequest(fs)
    
    file_req = fs_req.file_req()
    assert file_req[0] == '/mgmt/filestore/default/local/test.txt'
    assert file_req[1] == 'GET'
    assert file_req[2]['file']['name'] == 'test.txt'

def test_DPFileStoreRequest_get_file_req():

    params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/test.txt',
            'dest': '/local/GetStats',
            'overwrite': True,
            'state': 'file'
        }
    fs = DPFileStore(params)
    fs_req = DPFileStoreRequest(fs)
    
    file_req = fs_req.file_req()
    assert file_req[0] == '/mgmt/filestore/default/local/GetStats/test.txt'
    assert file_req[1] == 'GET'
    assert file_req[2]['file']['name'] == 'test.txt'

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
    assert dp_action_req.info_path == '/mgmt/actionqueue/default/operations/TraceRoute?schema-format=datapower'
    
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

