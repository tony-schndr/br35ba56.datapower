from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.filestore import (
    DPFileStore,
    isBase64
)

class TestDPFileStore():

    def test_build_params_validate_file_content(self):
        params = {
            'domain': 'default',
            'content': None,
            'src' : './tests/unit/module_utils/test_data/copy/test.txt',
            'dest' : '/local/',
            'overwrite' : True
        }
        filestore_req =  DPFileStore(params)
        assert filestore_req.content == 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE='
        assert filestore_req.file_name == 'test.txt'

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
        filestore_req =  DPFileStore(params)
        assert filestore_req.content == 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE='
        assert filestore_req.file_name == 'test.txt'


