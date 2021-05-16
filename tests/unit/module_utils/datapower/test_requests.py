from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPConfigRequest,
    DPGetConfigRequest,
    DPRequest,
    DPFileRequest,
    DPDirectoryRequest,
    DPActionQueueRequest,
    DPActionQueueSchemaRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPConfigObject
)

from ansible_collections.community.datapower.plugins.module_utils.datapower.actionqueue import (
    DPActionQueue
)
from ansible_collections.community.datapower.tests.unit.module_utils.test_data import (
    dp_actionq_test_data as action_test_data,
)

class MockConnection():
    @staticmethod
    def send_request(path,method,body):
        return path, method, body


class TestDPRequest:

    def test_DPRequest_join_path(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        assert DPRequest.join_path(domain, top_directory,file_path, base_path='/mgmt/filestore/') == '/mgmt/filestore/default/local/dir/subdir/get.js'
        
    def test_DPRequest_join_path_no_base_path(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        try:
            DPRequest.join_path(domain, top_directory,file_path)
            assert False
        except:
            assert True


class TestDPFileRequest:
    #Need a few more tests with potentially invalid input if handled incorrectly
    connection = MockConnection()

    def test_DPFileRequest__init__(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = DPFileRequest(self.connection, domain, top_directory, file_path, content)
        assert req
        assert req.path == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.body == {'file':{'name':'get.js', 'content': content}}

    def test_DPFileRequest_create(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = DPFileRequest(self.connection, domain, top_directory, file_path, content)
        
        assert req.create()[0] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.create()[1] == 'POST'
        assert req.create()[2] == {'file':{'name':'get.js', 'content': content}}
    
    def test_DPFileRequest_update(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = DPFileRequest(self.connection, domain, top_directory, file_path, content)
        
        assert req.update()[0] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.update()[1] == 'PUT'
        assert req.update()[2] == {'file':{'name':'get.js', 'content': content}}

    def test_DPFileRequest_get(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = DPFileRequest(self.connection, domain, top_directory, file_path, content)
        
        assert req.get()[0] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.get()[1] == 'GET'
        assert req.get()[2] == None

    def test_DPFileRequest_delete(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = DPFileRequest(self.connection, domain, top_directory, file_path, content)
        
        assert req.delete()[0] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.delete()[1] == 'DELETE'
        assert req.delete()[2] == None

class TestDPDirectoryRequest:
    #Need a few more tests with potentially invalid input if handled incorrectly
    connection = MockConnection()

    def test_DPDirectoryRequest__init__(self):
        domain = 'default'
        top_directory = 'local'
        dir_path = 'dir/subdir/'
        req = DPDirectoryRequest(self.connection, domain, top_directory, dir_path)
        assert req
        assert req.path == '/mgmt/filestore/default/local/dir/subdir'
        assert req.body == {'directory':{'name': dir_path}}


    def test_DPDirectoryRequest_create(self):
        domain = 'default'
        top_directory = 'local'
        dir_path = 'dir/subdir/'
        req = DPDirectoryRequest(self.connection, domain, top_directory, dir_path)
        assert req.create()[0] == '/mgmt/filestore/default/local'
        assert req.create()[1] == 'POST'
        assert req.create()[2] == {'directory':{'name': dir_path}}


    def test_DPDirectoryRequest_update(self):
        domain = 'default'
        top_directory = 'local'
        dir_path = 'dir/subdir/' 
        req = DPDirectoryRequest(self.connection, domain, top_directory, dir_path)
        try:
            req.update()
            assert False
        except: #No update request for a directory, see class.
            assert True

    def test_DPDirectoryRequest_get(self):
        domain = 'default'
        top_directory = 'local'
        dir_path = 'dir/subdir/'
        req = DPDirectoryRequest(self.connection, domain, top_directory, dir_path)
        
        assert req.get()[0] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.get()[1] == 'GET'
        assert req.get()[2] == None

    def test_DPDirectoryRequest_delete(self):
        domain = 'default'
        top_directory = 'local'
        dir_path = 'dir/subdir/'
        req = DPDirectoryRequest(self.connection, domain, top_directory, dir_path)
        assert req.delete()[0] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.delete()[1] == 'DELETE'
        assert req.delete()[2] == None

class TestDPActionQueueSchemaRequest:
    connection = MockConnection()

    def test_DPActionQueueSchemaRequest(self):
        task_args = {
            'domain':'default',
            'action': 'SaveConfig'
        }

        dp_action = DPActionQueue(**task_args)
        dp_action_req = DPActionQueueSchemaRequest(self.connection, dp_action)
        assert dp_action_req.path == '/mgmt/actionqueue/default/operations/SaveConfig?schema-format=datapower'

class TestDPActionQueueRequest:
    connection = MockConnection()
    def test_DPActionQueueRequest_1(self):
        task_args = {
            'domain':'default',
            'action': 'SaveConfig',
            'parameters': None
        }
        dp_action = DPActionQueue(**task_args)
        dp_action_req = DPActionQueueRequest(self.connection, dp_action)
        assert dp_action_req.path == '/mgmt/actionqueue/default'
        assert dp_action_req.body == {
                'SaveConfig' : {}
            }
    


    def test_DPActionQueueRequest_2(self):
        task_args = {
            'domain':'default',
            'action': 'TraceRoute',
            'parameters': {
                'RemoteHost': 'www.google.com'
            }
        }

        dp_action = DPActionQueue(**task_args)
        dp_action_req = DPActionQueueRequest(self.connection, dp_action)
        assert dp_action_req.path == '/mgmt/actionqueue/default'
        assert dp_action_req.body == {
                'TraceRoute' : {'RemoteHost': 'www.google.com'}
            }



class TestDPConfigRequest:
    connection = MockConnection()
    def test_DPConfigRequest_mod_args(self):
        kwargs = {
            "class_name": None,
            "config": {
                "CryptoValCred": {
                    "mAdminState": "enabled",
                    "name": "valcred"
                }
            },
            "domain": "default",
            "name": None,
        }
        dp_mgmt_conf = DPConfigObject(**kwargs)
        dp_req = DPConfigRequest(self.connection, dp_mgmt_conf)
        assert dp_req.path ==  '/mgmt/config/default/CryptoValCred/valcred'
       
       
        assert dp_req.body == {
                "CryptoValCred": {
                    "mAdminState": "enabled",
                    "name": "valcred"
                }
            }

    def test_DPConfigRequest_min(self):
        kwargs = {
            'domain':'snafu',
            'config': {
                'CryptoValCred' : {
                    'name':'valcred',
                    'mAdminState':'disabled'
                }
            },
            'state': 'present'
        }

        dp_mgmt_conf = DPConfigObject(**kwargs)
        dp_req = DPConfigRequest(self.connection, dp_mgmt_conf)
        assert dp_req.path ==  '/mgmt/config/snafu/CryptoValCred/valcred'
        
    def test_DPConfigRequest_w_name(self):
        kwargs = {
            'domain':'snafu',
            'config': {
                'CryptoValCred' : {
                    'name':'valcred'
                }
            },
            'state': 'present'
        }
        dp_mgmt_conf = DPConfigObject(**kwargs)
        dp_req = DPConfigRequest(self.connection, dp_mgmt_conf)
        assert dp_req.path ==  '/mgmt/config/snafu/CryptoValCred/valcred'

    def test_DPConfigRequest_invalid_class(self):
        kwargs = {
            'domain':'snafu',
            'config': {
                'ValidationCredential' : {
                    'name':'valcred'
                }
            },
            'state': 'present'
        }
        try:
            DPConfigObject(**kwargs)
        except ValueError:
            assert True
'''
    def test_DPGetConfigRequest_1():
        kwargs = {
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

        dp_mgmt_conf = DPManageConfigObject(**kwargs)
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
'''