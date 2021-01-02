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
            'src': './tests/unit/module_utils/test_data/copy/test.txt',
            'dest': '/local/',
            'overwrite': True,
            'state': 'file'
        }
        filestore = DPFileStore(params)
        assert filestore.content == 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE='

    def test_build_params_validate_file_name_from_rel_path(self):
        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/test.txt',
            'dest': '/local/',
            'overwrite': True,
            'state': 'file'
        }
        filestore = DPFileStore(params)
        assert filestore.file_name == 'test.txt'

    def test_isBase64(self):
        assert isBase64('SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE=')

    def test_build_params_validate_content_passed_as_base64(self):
        params = {
            'domain': 'default',
            'content': 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE=',
            'src': None,
            'dest': '/local/test.txt',
            'overwrite': True,
            'state': 'file'
        }
        filestore = DPFileStore(params)
        assert filestore.content == 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE='
        assert filestore.file_name == 'test.txt'

    def test_build_params_validate_content_passed_as_str(self):
        params = {
            'domain': 'default',
            'content': 'Hello world from Ansible DataPower!',
            'src': None,
            'dest': '/local/test.txt',
            'overwrite': True,
            'state': 'file'
        }
        filestore = DPFileStore(params)
        assert filestore.content == 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE='

    def test_build_params_validate_content_passed_as_all_methods_are_equivalent(self):
        params = {
            'domain': 'default',
            'content': 'Hello world from Ansible DataPower!',
            'src': None,
            'dest': '/local/test.txt',
            'overwrite': True,
            'state': 'file'
        }
        filestore_str = DPFileStore(params)

        params = {
            'domain': 'default',
            'content': 'SGVsbG8gd29ybGQgZnJvbSBBbnNpYmxlIERhdGFQb3dlciE=',
            'src': None,
            'dest': '/local/test.txt',
            'overwrite': True,
            'state': 'file'
        }
        filestore_base64 = DPFileStore(params)

        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/test.txt',
            'dest': '/local/',
            'overwrite': True,
            'state': 'file'
        }
        filestore_abspath = DPFileStore(params)

        assert filestore_abspath.content == filestore_base64.content and filestore_base64.content == filestore_str.content

    def test_DPFileStore_dest(self):
        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
            'dest': '/local/GetStat',
            'overwrite': True,
            'state': 'directory'
        }
        filestore = DPFileStore(params)
        assert filestore.dest == '/local/GetStat'

    def test_DPFileStore_dirs(self):
        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
            'dest': '/local/GetStat',
            'overwrite': True,
            'state': 'directory'
        }
        filestore = DPFileStore(params)
        assert sorted(list(filestore.dirs())) == sorted(
            [
                '/local/GetStat/Route',
                '/local/GetStat/Processing',
                '/local/GetStat/Processing/Route'
            ]
        )

    def test_DPFileStore_files(self):


        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
            'dest': '/local/GetStat',
            'overwrite': True,
            'state': 'directory'
        }
        filestore = DPFileStore(params)
        assert sorted(filestore.files()) == sorted(['/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/getDomainMemStatus.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/setDeviceName.xsl', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/getMem.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/getServicesMemStatus.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/getCPU.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/callGetStat.xsl', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Route/getDomainMemStatus.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Route/setDeviceName.xsl', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Route/getMem.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Route/getServicesMemStatus.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Route/getCPU.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Route/callGetStat.xsl', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/getDomainMemStatus.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/setDeviceName.xsl', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/getMem.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/getServicesMemStatus.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/getCPU.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/callGetStat.xsl', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/Route/getDomainMemStatus.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/Route/setDeviceName.xsl', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/Route/getMem.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/Route/getServicesMemStatus.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/Route/getCPU.js', '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat/Processing/Route/callGetStat.xsl'])
'''
import filestore
from filestore import DPFileStore
from glob import glob
params = {
    'domain': 'default',
    'content': None,
    'src' : '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
    'dest' : '/local/GetStat',
    'overwrite' : True,
    'state' : 'directory'
}
filestore = DPFileStore(params)

for f in filestore.files():
    print(f)

list(glob(filestore.src +'/**/*', recursive=True))
'''
