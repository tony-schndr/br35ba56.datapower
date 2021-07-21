from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import os

import pytest


from ansible_collections.community.datapower.plugins.module_utils.datapower import filestore
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import LocalFile
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    Request
)


class Connection():
    pass



def test_get_files_from_filestore_single_file():
    filestore_resp = {
        "_links": {
            "self": {
                "href": "/mgmt/filestore/default/local"
            },
            "doc": {
                "href": "/mgmt/docs/filestore"
            }
        },
        "filestore": {
            "location": {
                "name": "local:",
                "file": {
                    "name": "demo.txt",
                    "size": 12,
                    "modified": "2021-07-13 13:07:41",
                    "href": "/mgmt/filestore/default/local/demo.txt"
                },
                "directory": [
                    {
                        "name": "local:/snafu",
                        "href": "/mgmt/filestore/default/local/snafu"
                    },
                    {
                        "name": "local:/subdir",
                        "href": "/mgmt/filestore/default/local/subdir"
                    },
                    {
                        "name": "local:/foo",
                        "href": "/mgmt/filestore/default/local/foo"
                    },
                    {
                        "name": "local:/local",
                        "href": "/mgmt/filestore/default/local/local"
                    }
                ],
                "href": "/mgmt/filestore/default/local"
            }
        }
    }
    
    files = filestore.get_files_from_filestore(filestore_resp)
    assert files == ['/mgmt/filestore/default/local/demo.txt']


def test_get_files_from_filestore_multiple_files():
    filestore_resp = {
        "_links": {
            "self": {
                "href": "/mgmt/filestore/default/local"
            },
            "doc": {
                "href": "/mgmt/docs/filestore"
            }
        },
        "filestore": {
            "location": {
                "name": "local:",
                "file": [
                    {
                        "name": "demo.txt",
                        "size": 12,
                        "modified": "2021-07-13 13:07:41",
                        "href": "/mgmt/filestore/default/local/demo.txt"
                    },
                    {
                        "name": "demo2.txt",
                        "size": 12,
                        "modified": "2021-07-13 13:07:41",
                        "href": "/mgmt/filestore/default/local/demo2.txt"
                    },
                        {
                        "name": "demo3.txt",
                        "size": 12,
                        "modified": "2021-07-13 13:07:41",
                        "href": "/mgmt/filestore/default/local/demo3.txt"
                    }
                ],
                "directory": [
                    {
                        "name": "local:/snafu",
                        "href": "/mgmt/filestore/default/local/snafu"
                    },
                    {
                        "name": "local:/subdir",
                        "href": "/mgmt/filestore/default/local/subdir"
                    },
                    {
                        "name": "local:/foo",
                        "href": "/mgmt/filestore/default/local/foo"
                    },
                    {
                        "name": "local:/local",
                        "href": "/mgmt/filestore/default/local/local"
                    }
                ],
                "href": "/mgmt/filestore/default/local"
            }
        }
    }
    
    files = filestore.get_files_from_filestore(filestore_resp)
    assert files == [
        '/mgmt/filestore/default/local/demo.txt',
        '/mgmt/filestore/default/local/demo2.txt',
        '/mgmt/filestore/default/local/demo3.txt',
    ]


def test_get_parent_dir():
    path = '/some/test/path/file.txt'
    assert filestore.get_parent_dir(path) == '/some/test/path'


def test_get_request_func_files_equal():
    to_file_path = '/tmp/to/getMemory.js'
    from_file_path = '/tmp/from/getMemory.js'
    content = 'aGVsbG8gd29ybGQK'
    to_lf = LocalFile(to_file_path, content)
    from_lf = LocalFile(from_file_path, content)

    connection = Connection()
    req = Request(connection)

    func = filestore.get_request_func(req, from_lf, to_lf, 'present')
    assert func == None 


def test_get_request_func_files_not_equal():
    to_file_path = '/tmp/to/test.txt'
    from_file_path = '/tmp/from/test.txt'
    to_lf = LocalFile(to_file_path, 'aGVsbG8gd29ybGQK')
    from_lf = LocalFile(from_file_path, 'YmFsb2duYQo=')

    connection = Connection()
    req = Request(connection)

    func = filestore.get_request_func(req, from_lf, to_lf, 'present')
    assert func.__name__ == 'put'


def test_get_request_func_file_does_not_exist_on_remote():
    to_file_path = '/tmp/to/test1.txt'
    to_lf = LocalFile(to_file_path, 'aGVsbG8gd29ybGQK')

    connection = Connection()
    req = Request(connection)

    func = filestore.get_request_func(req, None, to_lf, 'present')
    assert func.__name__ == 'post'


def test_get_request_func_delete_file_that_does_not_exist():
    to_file_path = '/tmp/to/test2.txt'
    to_lf = LocalFile(to_file_path, 'aGVsbG8gd29ybGQK')

    connection = Connection()
    req = Request(connection)

    func = filestore.get_request_func(req, None, to_lf, 'absent')
    assert func == None


def test_get_request_func_delete_file_that_exists():
    from_file_path = '/tmp/to/test3.txt'
    from_lf = LocalFile(from_file_path, 'aGVsbG8gd29ybGQK')

    connection = Connection()
    req = Request(connection)

    func = filestore.get_request_func(req, from_lf, None, 'absent')
    assert func.__name__ == 'delete'