from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.filestore import (
    DPFileStore,
    isBase64
)

class TestDPFileStore():

    def test_build_params_validate_file_passed_as_rel_path(self):
        params = {
            'domain': 'default',
            'content': None,
            'src' : './tests/unit/module_utils/test_data/copy/test.txt',
            'dest' : '/local/',
            'overwrite' : True
        }
        filestore =  DPFileStore(params)
        assert filestore.content == 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE='
        assert filestore.file_name == 'test.txt'

    def test_isBase64(self):
        assert isBase64('SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE=')

    def test_build_params_validate_content_passed_as_base64(self):
        params = {
            'domain': 'default',
            'content': 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE=',
            'src' : None,
            'dest' : '/local/test.txt',
            'overwrite' : True
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
            'overwrite' : True
        }
        filestore =  DPFileStore(params)
        assert filestore.content == 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE='