from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest


from ansible_collections.community.datapower.plugins.module_utils.datapower.filestore import (
    DPFileStore,
    isBase64
)


class TestDPFileStore():

    def test_DPFileStore_state_is_absent(self):
        params = {
            'domain': 'default',
            'dest': '/local/demo.txt',
            'state': 'absent'
        }

        fs = DPFileStore(params)
        assert fs.dest == 'local/demo.txt'

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
    
    def test_DPFileStore_set_file_init_dest_root(self):
        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/test.txt',
            'dest': '/local/',
            'overwrite': True,
            'state': 'file'
        }
        fs = DPFileStore(params)
        assert fs.file_name == 'test.txt'
        assert fs.dest == 'local/test.txt'

    def test_DPFileStore_set_filepath_dest_is_dir(self):
        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/test.txt',
            'dest': 'local/GetStat',
            'overwrite': True,
            'state': 'file'
        }
        fs = DPFileStore(params)
        assert fs.dest == 'local/GetStat/test.txt'
    
    def test_DPFileStore_set_filepath_dest_is_file(self):
        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/test.txt',
            'dest': 'local/GetStat/test_5.txt',
            'overwrite': True,
            'state': 'file'
        }
        fs = DPFileStore(params)
        assert fs.file_name == 'test_5.txt'
        #assert fs.dest == 'local/GetStat/test_5.txt'

    def test_DPFileStore_state_is_dir_dest(self):
        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
            'dest': '/local/GetStat',
            'overwrite': True,
            'state': 'directory'
        }
        filestore = DPFileStore(params)
        assert filestore.dest == 'GetStat'


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
                'GetStat',
                'GetStat/Route',
                'GetStat/Processing',
                'GetStat/Processing/Route'
            ]
        )

    def test_DPFileStore_files(self):
        # Tests generating files, specifically index 0,1 of each tuple, index 2 is 
        # Base64 so not practical to test here.
        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
            'dest': '/local/GetStat',
            'overwrite': True,
            'state': 'directory'
        }
        filestore = DPFileStore(params)
        files = list((file[0], file[1]) for file in filestore.files())
        assert sorted(files) == sorted([
            ('GetStat/getDomainMemStatus.js','getDomainMemStatus.js'), 
            ('GetStat/setDeviceName.xsl', 'setDeviceName.xsl'), 
            ('GetStat/getMem.js', 'getMem.js'), 
            ('GetStat/getServicesMemStatus.js', 'getServicesMemStatus.js'), 
            ('GetStat/getCPU.js', 'getCPU.js'), 
            ('GetStat/callGetStat.xsl', 'callGetStat.xsl'), 
            ('GetStat/Route/getDomainMemStatus.js', 'getDomainMemStatus.js'),
            ('GetStat/Route/setDeviceName.xsl', 'setDeviceName.xsl'),
            ('GetStat/Route/getMem.js', 'getMem.js'), 
            ('GetStat/Route/getServicesMemStatus.js', 'getServicesMemStatus.js'),
            ('GetStat/Route/getCPU.js', 'getCPU.js'),
            ('GetStat/Route/callGetStat.xsl', 'callGetStat.xsl'),
            ('GetStat/Processing/getDomainMemStatus.js', 'getDomainMemStatus.js'), 
            ('GetStat/Processing/setDeviceName.xsl', 'setDeviceName.xsl'), 
            ('GetStat/Processing/getMem.js', 'getMem.js'), 
            ('GetStat/Processing/getServicesMemStatus.js', 'getServicesMemStatus.js'),
            ('GetStat/Processing/getCPU.js', 'getCPU.js'), 
            ('GetStat/Processing/callGetStat.xsl', 'callGetStat.xsl'),
            ('GetStat/Processing/Route/getDomainMemStatus.js', 'getDomainMemStatus.js'), 
            ('GetStat/Processing/Route/setDeviceName.xsl', 'setDeviceName.xsl'), 
            ('GetStat/Processing/Route/getMem.js', 'getMem.js'), 
            ('GetStat/Processing/Route/getServicesMemStatus.js', 'getServicesMemStatus.js'), 
            ('GetStat/Processing/Route/getCPU.js', 'getCPU.js'), 
            ('GetStat/Processing/Route/callGetStat.xsl', 'callGetStat.xsl')
        ])

    def test_DPFileStore_root_dir(self):
        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
            'dest': '/local/GetStat',
            'overwrite': True,
            'state': 'directory'
        }
        filestore = DPFileStore(params)
        assert filestore.root_dir == 'local'
        params = {
            'domain': 'default',
            'content': None,
            'src': './tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
            'dest': '/ll/GetStat', # malformed root dir
            'overwrite': True,
            'state': 'directory'
        }
        try:
            filestore = DPFileStore(params)
        except:
            assert True


'''#Used for testing this in python idle
from requests import DPFileStoreRequest
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
req = DPFileStoreRequest(filestore)


for r in req.dir_reqs():
    print(r)
'''
