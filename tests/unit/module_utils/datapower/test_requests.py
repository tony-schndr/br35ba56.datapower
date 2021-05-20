from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPConfigRequest,
    #DPGetConfigRequest,
    DPRequest,
    DPFileRequest,
    DPDirectoryRequest,
    DPActionQueueRequest,
    DPActionQueueSchemaRequest
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
        req = DPFileRequest(self.connection)
        req.set_path(domain, top_directory, file_path)
        req.set_body(file_path, content)
        assert req.path == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.body == {'file':{'name':'get.js', 'content': content}}

    def test_DPFileRequest_create(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = DPFileRequest(self.connection)
        req.set_path(domain, top_directory, file_path)
        req.set_body(file_path, content)
        assert req.create()['path'] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.create()['method'] == 'POST'
        assert req.create()['body'] == {'file':{'name':'get.js', 'content': content}}
    
    def test_DPFileRequest_update(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = DPFileRequest(self.connection)
        req.set_path(domain, top_directory, file_path)
        req.set_body(file_path, content)
        assert req.update()['path'] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.update()['method'] == 'PUT'
        assert req.update()['body'] == {'file':{'name':'get.js', 'content': content}}

    def test_DPFileRequest_get(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = DPFileRequest(self.connection)
        req.set_path(domain, top_directory, file_path)
        req.set_body(file_path, content)
        assert req.get()['path'] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.get()['method'] == 'GET'
        assert req.get()['body'] == None

    def test_DPFileRequest_delete(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = DPFileRequest(self.connection)
        req.set_path(domain, top_directory, file_path)
        req.set_body(file_path, content)
        assert req.delete()['path'] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.delete()['method'] == 'DELETE'
        assert req.delete()['body'] == None


class TestDPDirectoryRequest:
    #Need a few more tests with potentially invalid input if handled incorrectly
    connection = MockConnection()

    def test_DPDirectoryRequest__init__(self):
        domain = 'default'
        top_directory = 'local'
        dir_path = 'dir/subdir/'
        
        req = DPDirectoryRequest(self.connection)
        req.set_body(dir_path)
        req.set_path(domain, top_directory, dir_path)

        assert req
        assert req.path == '/mgmt/filestore/default/local/dir/subdir'
        assert req.body == {'directory':{'name': dir_path}}

    def test_DPDirectoryRequest_create(self):
        domain = 'default'
        top_directory = 'local'
        dir_path = 'dir/subdir/'
        req = DPDirectoryRequest(self.connection)
        req.set_body(dir_path)
        req.set_path(domain, top_directory, dir_path)
        assert req.create()['path'] == '/mgmt/filestore/default/local'
        assert req.create()['method'] == 'POST'
        assert req.create()['body'] == {'directory':{'name': dir_path}}

    def test_DPDirectoryRequest_update(self):
        domain = 'default'
        top_directory = 'local'
        dir_path = 'dir/subdir/' 
        req = DPDirectoryRequest(self.connection)
        req.set_body(dir_path)
        req.set_path(domain, top_directory, dir_path)
        try:
            req.update()
            assert False
        except: #No update request for a directory, see class.
            assert True

    def test_DPDirectoryRequest_get(self):
        domain = 'default'
        top_directory = 'local'
        dir_path = 'dir/subdir/'
        req = DPDirectoryRequest(self.connection)
        req.set_body(dir_path)
        req.set_path(domain, top_directory, dir_path)
        assert req.get()['path'] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.get()['method'] == 'GET'
        assert req.get()['body'] == None

    def test_DPDirectoryRequest_delete(self):
        domain = 'default'
        top_directory = 'local'
        dir_path = 'dir/subdir/'
        req = DPDirectoryRequest(self.connection)
        req.set_body(dir_path)
        req.set_path(domain, top_directory, dir_path)
        assert req.delete()['path'] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.delete()['method'] == 'DELETE'
        assert req.delete()['body'] == None


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

    def test_action_process_request_transition(self):
        task_args = {
            'domain':'default',
            'action': 'TraceRoute',
            'parameters': {
                'RemoteHost': 'www.google.com'
            }
        }

        dp_action = DPActionQueue(**task_args)
        resp = {
            "_links": {
                "self": {
                    "href": "/mgmt/actionqueue/snafu"
                },
                "doc": {
                    "href": "/mgmt/docs/actionqueue"
                },
                "location": {
                    "href": "/mgmt/actionqueue/snafu/pending/ResetThisDomain-20201215T210541Z-10"
                }
            },
            "ResetThisDomain": {
                "status": "Action request accepted."
            }
        }
        req_handler = DPActionQueueRequest(self.connection, dp_action)
        assert req_handler.is_completed(resp) == False
        resp = {
            "_links": {
                "self": {
                    "href": "/mgmt/actionqueue/snafu"
                },
                "doc": {
                    "href": "/mgmt/docs/actionqueue"
                }
            },
            "SaveConfig": "Operation completed.",
            "script-log": ""
        }
        assert req_handler.is_completed(resp) == True
        resp = {
            "_links": {
                "self": {
                    "href": "/mgmt/actionqueue/snafu/pending/ResetThisDomain-20201215T212048Z-11"
                }
            },
            "status": "completed"
        }
        assert req_handler.is_completed(resp) == True
        resp = {
            "SaveConfig": "Operation completed.",
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/actionqueue"
                },
                "self": {
                    "href": "/mgmt/actionqueue/snafu"
                }
            },
            "script-log": ""
        }
        assert req_handler.is_completed(resp) == True
    

class TestDPConfigRequest:
    connection = MockConnection()
    kwargs = {
        "domain": "default",
        "name": 'valcred',
        "class_name": 'CryptoValCred',
        "config": {
            "CryptoValCred": {
                "mAdminState": "enabled",
                "name": "valcred"
            }
        }
    }

    def test_DPConfigRequest__init__(self):
        dp_req = DPConfigRequest(self.connection)
        dp_req.set_path(
            self.kwargs['domain'],
            self.kwargs['class_name'],
            self.kwargs['name'],
            )
        dp_req.set_body(self.kwargs['config'])
        assert dp_req.path ==  '/mgmt/config/default/CryptoValCred/valcred'
        assert dp_req.body == {
                "CryptoValCred": {
                    "mAdminState": "enabled",
                    "name": "valcred"
                }
            }

    def test_DPConfigRequest_set_options_all_options(self):
        options = {
            'recursive':True,
            'state': True,
            'depth': 3
        }
        dp_req = DPConfigRequest(self.connection)
        dp_req.set_options(**options)
        assert 'state=1' in dp_req.options and 'depth=3' in dp_req.options and 'view=recursive' in dp_req.options
        
    def test_DPConfigRequest_set_options_only_recursive(self):
        options = {
            'recursive':True
        }
        dp_req = DPConfigRequest(self.connection)
        dp_req.set_path(
            self.kwargs['domain'],
            self.kwargs['class_name'],
            self.kwargs['name'],
            )
        dp_req.set_options(**options)
        assert  'view=recursive' in dp_req.options
        assert  'depth=3' in dp_req.options

