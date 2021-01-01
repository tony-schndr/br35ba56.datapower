from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.filestore import (
    DPFileStore,
    isBase64
)

class TestDPFileStore():

    def test_build_params_validate_file_content_from_rel_path(self):
        params = {
            'domain': 'default',
            'content': None,
            'src' : './tests/unit/module_utils/test_data/copy/test.txt',
            'dest' : '/local/',
            'overwrite' : True,
            'state' : 'file'
        }
        filestore =  DPFileStore(params)
        assert filestore.content == 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE='

    def test_build_params_validate_file_name_from_rel_path(self):
        params = {
            'domain': 'default',
            'content': None,
            'src' : './tests/unit/module_utils/test_data/copy/test.txt',
            'dest' : '/local/',
            'overwrite' : True,
            'state' : 'file'
        }
        filestore =  DPFileStore(params)
        assert filestore.file_name == 'test.txt'

    def test_isBase64(self):
        assert isBase64('SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE=')

    def test_build_params_validate_content_passed_as_base64(self):
        params = {
            'domain': 'default',
            'content': 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE=',
            'src' : None,
            'dest' : '/local/test.txt',
            'overwrite' : True,
            'state' : 'file'
        }
        filestore =  DPFileStore(params)
        assert filestore.content == 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE='
        assert filestore.file_name == 'test.txt'

    def test_build_params_validate_content_passed_as_str(self):
        params = {
            'domain': 'default',
            'content': 'Hello world from Ansible DataPower!',
            'src' : None,
            'dest' : '/local/test.txt',
            'overwrite' : True,
            'state' : 'file'
        }
        filestore =  DPFileStore(params)
        assert filestore.content == 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE='

    def test_build_params_validate_content_passed_as_all_methods_are_equivalent(self):
        params = {
            'domain': 'default',
            'content': 'Hello world from Ansible DataPower!',
            'src' : None,
            'dest' : '/local/test.txt',
            'overwrite' : True,
            'state' : 'file'
        }
        filestore_str =  DPFileStore(params)

        params = {
            'domain': 'default',
            'content': 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE=',
            'src' : None,
            'dest' : '/local/test.txt',
            'overwrite' : True,
            'state' : 'file'
        }
        filestore_base64 =  DPFileStore(params)

        params = {
            'domain': 'default',
            'content': None,
            'src' : './tests/unit/module_utils/test_data/copy/test.txt',
            'dest' : '/local/',
            'overwrite' : True,
            'state' : 'file'
        }
        filestore_abspath =  DPFileStore(params)
        
        assert filestore_abspath.content == filestore_base64.content and filestore_base64.content == filestore_str.content

    def test_build_params_validate_directory_file_upload_generator(self):
        params = {
            'domain': 'default',
            'content': None,
            'src' : './tests/unit/module_utils/test_data/copy/test.txt',
            'dest' : '/local/',
            'overwrite' : True,
            'state' : 'directory'
        }
