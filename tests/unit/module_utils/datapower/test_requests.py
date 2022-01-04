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
    join_path
)

from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    class_name_from_config,
    name_from_config
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
        assert join_path(
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
        except Exception:
            assert True


class TestFileRequest:
    def test_FileRequest__init__(self):
        domain = 'default'
        file_path = 'local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest()
        req.set_path(domain=domain, file_path=file_path)
        req.set_body(file_path=file_path, content=content)
        assert req.path == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.body == {'file': {'name': 'get.js', 'content': content}}

    def test_FileRequest_create(self):
        domain = 'default'
        file_path = 'local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest()
        req.set_path(domain=domain, file_path=file_path)
        req.set_body(file_path=file_path, content=content)

        assert req.post()['path'] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.post()['method'] == 'POST'
        assert req.post()['data'] == {
            'file': {'name': 'get.js', 'content': content}}

    def test_FileRequest_update(self):
        domain = 'default'
        file_path = 'local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest()
        req.set_path(domain=domain, file_path=file_path)
        req.set_body(file_path=file_path, content=content)
        assert req.put()[
            'path'] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.put()['method'] == 'PUT'
        assert req.put()['data'] == {
            'file': {'name': 'get.js', 'content': content}}

    def test_FileRequest_get(self):
        domain = 'default'
        file_path = 'local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest()
        req.set_path(domain=domain, file_path=file_path)
        req.set_body(file_path=file_path, content=content)
        assert req.get()[
            'path'] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.get()['method'] == 'GET'
        assert not req.get()['data']

    def test_FileRequest_delete(self):
        domain = 'default'
        file_path = 'local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest()
        req.set_path(domain=domain, file_path=file_path)
        req.set_body(file_path=file_path, content=content)
        assert req.delete()[
            'path'] == '/mgmt/filestore/default/local/dir/subdir/get.js'
        assert req.delete()['method'] == 'DELETE'
        assert not req.delete()['data']

    def test_FileRequest_set_path_strips_leading_forward_path(self):
        domain = 'default'
        file_path = '/local/dir/subdir/get.js'
        content = 'aGVsbG8gd29ybGQK'
        req = FileRequest()
        req.set_path(domain=domain, file_path=file_path)
        req.set_body(file_path=file_path, content=content)

        assert req.post()['path'] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.post()['method'] == 'POST'
        assert req.post()['data'] == {
            'file': {'name': 'get.js', 'content': content}}


class TestDirectoryRequest:
    # Need a few more tests with potentially invalid input if handled incorrectly

    def test_DirectoryRequest__init__(self):
        domain = 'default'
        dir_path = 'local/dir/subdir/'

        req = DirectoryRequest()
        req.set_body(dir_path=dir_path)
        req.set_path(domain=domain, dir_path=dir_path)

        assert req
        assert req.path == '/mgmt/filestore/default/local/dir/subdir'
        assert req.body == {'directory': {'name': 'dir/subdir/'}}

    def test_DirectoryRequest_create(self):
        domain = 'default'
        dir_path = 'local/dir/subdir/'
        req = DirectoryRequest()
        req.set_body(dir_path=dir_path)
        req.set_path(domain=domain, dir_path=dir_path)
        assert req.post()['path'] == '/mgmt/filestore/default/local'
        assert req.post()['method'] == 'POST'
        assert req.post()['data'] == {'directory': {'name': 'dir/subdir/'}}

    def test_DirectoryRequest_update(self):
        domain = 'default'
        dir_path = 'local/dir/subdir/'
        req = DirectoryRequest()
        req.set_body(dir_path=dir_path)
        req.set_path(domain=domain, dir_path=dir_path)
        try:
            req.put()
            assert False
        except Exception:  # Put not implemented
            assert True

    def test_DirectoryRequest_get(self):
        domain = 'default'
        dir_path = 'local/dir/subdir/'
        req = DirectoryRequest()
        req.set_body(dir_path=dir_path)
        req.set_path(domain=domain, dir_path=dir_path)
        assert req.get()['path'] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.get()['method'] == 'GET'
        assert not req.get()['data']

    def test_DirectoryRequest_delete(self):
        domain = 'default'
        dir_path = 'local/dir/subdir/'
        req = DirectoryRequest()
        req.set_body(dir_path=dir_path)
        req.set_path(domain=domain, dir_path=dir_path)
        assert req.delete()[
            'path'] == '/mgmt/filestore/default/local/dir/subdir'
        assert req.delete()['method'] == 'DELETE'
        assert not req.delete()['data']


class TestConfigRequest:

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
        dp_req = ConfigRequest()
        dp_req.set_path(
            domain=self.kwargs['domain'],
            class_name=self.kwargs['class_name'],
            name=self.kwargs['name'],
        )
        dp_req.set_body(body=self.kwargs['config'])
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
        dp_req = ConfigRequest()
        dp_req.set_options(**options)
        assert 'state=1' in dp_req.options \
            and 'depth=3' in dp_req.options \
            and 'view=recursive' in dp_req.options

    def test_ConfigRequest_set_options_only_recursive(self):
        options = {
            'recursive': True
        }
        dp_req = ConfigRequest()
        dp_req.set_path(
            domain=self.kwargs['domain'],
            class_name=self.kwargs['class_name'],
            name=self.kwargs['name'],
        )
        dp_req.set_options(**options)
        assert 'view=recursive' in dp_req.options
        assert 'depth=3' in dp_req.options

    def test_ConfigRequest_mod_args(self):
        task_args = {
            "config": {
                "CryptoValCred": {
                    "mAdminState": "enabled",
                    "name": "valcred"
                }
            },
            "domain": "default",
        }
        domain = task_args['domain']
        config = task_args['config']
        class_name = class_name_from_config(task_args['config'])
        name = name_from_config(task_args['config'], class_name)
        dp_req = ConfigRequest()
        dp_req.set_path(domain=domain, class_name=class_name, name=name)
        dp_req.set_body(body=config)

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

        domain = task_args['domain']
        config = task_args['config']
        class_name = class_name_from_config(task_args['config'])
        name = name_from_config(task_args['config'], class_name)
        dp_req = ConfigRequest()
        dp_req.set_path(domain=domain, class_name=class_name, name=name)
        dp_req.set_body(body=config)

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
        domain = task_args['domain']
        config = task_args['config']
        class_name = class_name_from_config(task_args['config'])
        name = name_from_config(task_args['config'], class_name)

        dp_req = ConfigRequest()
        dp_req.set_path(domain=domain, class_name=class_name, name=name)
        dp_req.set_body(body=config)
        assert dp_req.path == '/mgmt/config/snafu/CryptoValCred/valcred'


class TestActionRequest:

    def test_DPActionQueueRequest_1(self):
        task_args = {
            'domain': 'default',
            'action_name': 'SaveConfig',
            'parameters': None
        }

        req = ActionQueueRequest(**task_args)
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

        req = ActionQueueRequest(**task_args)
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
        req = ActionQueueSchemaRequest(task_args['domain'], task_args['action_name'])
        assert req.path == '/mgmt/actionqueue/default/operations/SaveConfig?schema-format=datapower'
