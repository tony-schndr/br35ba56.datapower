from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    Request,
    ConfigRequest,
    FileRequest,
    DirectoryRequest,
    ActionQueueRequest,
    ActionQueueSchemaRequest,
    get_request_func
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    Config
)


class MockConnection():
    @staticmethod
    def send_request(path, method, body):
        return path, method, body


class TestRequest:

    def test_Request_join_path(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        assert Request.join_path(
            domain,
            top_directory,
            file_path,
            base_path='/mgmt/filestore/'
        ) == '/mgmt/filestore/default/local/dir/subdir/get.js'

    def test_Request_join_path_no_base_path(self):
        domain = 'default'
        top_directory = 'local'
        file_path = 'dir/subdir/get.js'
        try:
            Request.join_path(domain, top_directory, file_path)
            assert False
        except:
            assert True


class TestFileRequest:
    # Need a few more tests with potentially invalid input if handled incorrectly
    connection = MockConnection()

    def test_FileRequest__init__(self):
        domain = 'default'
        file_path = 'local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest(self.connection)
        req.set_path(domain,  file_path)
        req.set_body(file_path, content)
        assert req.path == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.body == {'file': {'name': 'get.js', 'content': content}}


    def test_FileRequest_create(self):
        domain = 'default'
        file_path = 'local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest(self.connection)
        req.set_path(domain,file_path)
        req.set_body(file_path, content)
        #raise Exception(req.post())
        assert req.post()[0] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.post()[1] == 'POST'
        assert req.post()[2] == {'file': {'name': 'get.js', 'content': content}}


    def test_FileRequest_update(self):
        domain = 'default'
        file_path = 'local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest(self.connection)
        req.set_path(domain, file_path)
        req.set_body(file_path, content)
        assert req.put()[0] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.put()[1] == 'PUT'
        assert req.put()[2] == {'file': {'name': 'get.js', 'content': content}}

    def test_FileRequest_get(self):
        domain = 'default'
        file_path = 'local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest(self.connection)
        req.set_path(domain, file_path)
        req.set_body(file_path, content)
        assert req.get()[0] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.get()[1] == 'GET'
        assert req.get()[2] == None

    def test_FileRequest_delete(self):
        domain = 'default'
        file_path = 'local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest(self.connection)
        req.set_path(domain, file_path)
        req.set_body(file_path, content)
        assert req.delete()[0] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.delete()[1] == 'DELETE'
        assert req.delete()[2] == None


class TestDirectoryRequest:
    # Need a few more tests with potentially invalid input if handled incorrectly
    connection = MockConnection()

    def test_DirectoryRequest__init__(self):
        domain = 'default'
        dir_path = 'local/dir/subdir/'

        req = DirectoryRequest(self.connection)
        req.set_body(dir_path)
        req.set_path(domain, dir_path)

        assert req
        assert req.path == '/mgmt/filestore/default/local/dir/subdir'
        assert req.body == {'directory': {'name': 'dir/subdir/'}}

    def test_DirectoryRequest_create(self):
        domain = 'default'
        dir_path = 'local/dir/subdir/'
        req = DirectoryRequest(self.connection)
        req.set_body(dir_path)
        req.set_path(domain, dir_path)
        assert req.post()[0] == '/mgmt/filestore/default/local'
        assert req.post()[1] == 'POST'
        assert req.post()[2] == {'directory': {'name': 'dir/subdir/'}}

    def test_DirectoryRequest_update(self):
        domain = 'default'
        dir_path = 'local/dir/subdir/'
        req = DirectoryRequest(self.connection)
        req.set_body(dir_path)
        req.set_path(domain, dir_path)
        try:
            req.put()
            assert False
        except:  # Put not implemented
            assert True

    def test_DirectoryRequest_get(self):
        domain = 'default'
        dir_path = 'local/dir/subdir/'
        req = DirectoryRequest(self.connection)
        req.set_body(dir_path)
        req.set_path(domain, dir_path)
        assert req.get()[0] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.get()[1] == 'GET'
        assert req.get()[2] == None

    def test_DirectoryRequest_delete(self):
        domain = 'default'
        dir_path = 'local/dir/subdir/'
        req = DirectoryRequest(self.connection)
        req.set_body(dir_path)
        req.set_path(domain, dir_path)
        assert req.delete()[0] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.delete()[1] == 'DELETE'
        assert req.delete()[2] == None


class TestConfigRequest:
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

    def test_ConfigRequest__init__(self):
        dp_req = ConfigRequest(self.connection)
        dp_req.set_path(
            self.kwargs['domain'],
            self.kwargs['class_name'],
            self.kwargs['name'],
        )
        dp_req.set_body(self.kwargs['config'])
        assert dp_req.path == '/mgmt/config/default/CryptoValCred/valcred'
        assert dp_req.body == {
            "CryptoValCred": {
                "mAdminState": "enabled",
                "name": "valcred"
            }
        }

    def test_ConfigRequest_set_options_all_options(self):
        options = {
            'recursive': True,
            'status': True,
            'depth': 3
        }
        dp_req = ConfigRequest(self.connection)
        dp_req.set_options(**options)
        assert 'state=1' in dp_req.options \
            and 'depth=3' in dp_req.options \
            and 'view=recursive' in dp_req.options

    def test_ConfigRequest_set_options_only_recursive(self):
        options = {
            'recursive': True
        }
        dp_req = ConfigRequest(self.connection)
        dp_req.set_path(
            self.kwargs['domain'],
            self.kwargs['class_name'],
            self.kwargs['name'],
        )
        dp_req.set_options(**options)
        assert 'view=recursive' in dp_req.options
        assert 'depth=3' in dp_req.options

    def test_ConfigRequest_mod_args(self):
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
        }
        dp = Config(**task_args)
        dp_req = ConfigRequest(self.connection)
        dp_req.set_path(dp.domain, dp.class_name, dp.name)
        dp_req.set_body(dp.config)
        assert dp_req.path == '/mgmt/config/default/CryptoValCred/valcred'
        assert dp_req.body == {
            "CryptoValCred": {
                "mAdminState": "enabled",
                "name": "valcred"
            }
        }

    def test_ConfigRequest_min(self):
        task_args = {
            'domain': 'snafu',
            'config': {
                'CryptoValCred': {
                    'name': 'valcred',
                    'mAdminState': 'disabled'
                }
            }
        }

        dp = Config(**task_args)
        dp_req = ConfigRequest(self.connection)
        dp_req.set_path(dp.domain, dp.class_name, dp.name)
        dp_req.set_body(dp.config)
        assert dp_req.path == '/mgmt/config/snafu/CryptoValCred/valcred'
        assert dp_req.body == {
            'CryptoValCred': {
                'name': 'valcred',
                'mAdminState': 'disabled'
            }
        }

    def test_ManageConfigRequest_w_name(self):
        task_args = {
            'domain': 'snafu',
            'config': {
                'CryptoValCred': {
                    'name': 'valcred'
                }
            }
        }
        dp = Config(**task_args)
        dp_req = ConfigRequest(self.connection)
        dp_req.set_path(dp.domain, dp.class_name, dp.name)
        dp_req.set_body(dp.config)
        assert dp_req.path == '/mgmt/config/snafu/CryptoValCred/valcred'

    def test_ManageConfigRequest_invalid_class(self):
        task_args_w_invalid_class = {
            'domain': 'snafu',
            'config': {
                'ValidationCredential': {
                    'name': 'valcred'
                }
            }
        }
        try:
            Config(**task_args_w_invalid_class)
        except ValueError:
            assert True


class TestActionRequest:

    connection = MockConnection()

    def test_DPActionQueueRequest_1(self):
        task_args = {
            'domain': 'default',
            'action_name': 'SaveConfig',
            'parameters': None
        }

        req = ActionQueueRequest(self.connection, **task_args)
        assert req.path == '/mgmt/actionqueue/default'
        assert req.body == {'SaveConfig': {}}

    def test_ActionQueueRequest_2(self):
        task_args = {
            'domain': 'default',
            'action_name': 'TraceRoute',
            'parameters': {
                'RemoteHost': 'www.google.com'
            }

        }

        req = ActionQueueRequest(self.connection, **task_args)
        assert req.path == '/mgmt/actionqueue/default'
        assert req.body == {
            'TraceRoute': {
                'RemoteHost': 'www.google.com'
            }
        }

    def test_ActionQueueSchemaRequest(self):
        task_args = {
            'domain': 'default',
            'action_name': 'SaveConfig'
        }

        req = ActionQueueSchemaRequest(
            self.connection, task_args['domain'], task_args['action_name'])
        assert req.path == '/mgmt/actionqueue/default/operations/SaveConfig?schema-format=datapower'


def test_action_transitions():
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
    connection = MockConnection
    req = ActionQueueRequest(connection, 'default', 'SaveConfig')
    assert req.is_completed(resp) == False
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
    assert req.is_completed(resp) == True
    resp = {
        "_links": {
            "self": {
                "href": "/mgmt/actionqueue/snafu/pending/ResetThisDomain-20201215T212048Z-11"
            }
        },
        "status": "completed"
    }
    assert req.is_completed(resp) == True
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
    assert req.is_completed(resp) == True


def test_get_request_func_returns_none_when_data_is_equal():
    before = 'equal'
    after = 'equal'
    connection = MockConnection()
    req = Request(connection)

    func = get_request_func(req, before, after, 'present')
    assert func == None


def test_get_request_func_returns_put_when_data_is_not_equal():
    before = 'equal'
    after = 'not equal'
    connection = MockConnection()
    req = Request(connection)

    func = get_request_func(req, before, after, 'present')
    assert func.__name__ == 'put'


def test_get_request_func_returns_post_when_data_does_not_exist_on_remote():
    after = 'not equal'
    before = None
    connection = MockConnection()
    req = Request(connection)

    func = get_request_func(req, before, after, 'present')
    assert func.__name__ == 'post'


def test_get_request_func_returns_none_when_data_does_not_exist_on_remote():
    after = 'not equal'
    before = None
    connection = MockConnection()
    req = Request(connection)

    func = get_request_func(req, before, after, 'absent')
    assert func == None


def test_get_request_func_returns_delete_when_data_exists_on_remote():
    before = 'equal'
    after = None
    connection = MockConnection()
    req = Request(connection)

    func = get_request_func(req, before, after, 'absent')
    assert func.__name__ == 'delete'
