from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import os

import pytest


from ansible_collections.community.datapower.plugins.module_utils.datapower import filestore
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import LocalFile


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

