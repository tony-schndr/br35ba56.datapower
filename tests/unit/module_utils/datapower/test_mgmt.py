from __future__ import absolute_import, division, print_function
from typing import DefaultDict

__metaclass__ = type

import re
import os

import pytest


from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPDirectory,
    DPFile,
    DPActionQueue,
    DPConfig,
    InvalidDPDirectoryException
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    LocalFile
) 

class TestDPActionQueue:

    def test_DPActionQueue(self):
        
        domain = "default"
        action = "SaveConfig"
        
        dp_action = DPActionQueue(domain, action)
        assert dp_action.action == 'SaveConfig'
        assert dp_action.domain == 'default'

class TestDPConfig:

    def test_DPConfig__init__min_args_required(self):
        kwargs = {
            'domain' : 'default',
            'class_name' : 'CryptoValCred',
            'name' : 'test',
            'config' : None
        }


        dp_config = DPConfig(**kwargs)
        assert dp_config

    def test_DPConfig__init__class_name_and_name_in_config(self):
        kwargs = {
            'domain':'snafu',
            'config': {
                'CryptoValCred' : {
                    'name':'valcred'
                }
            }
        }

        dp_config = DPConfig(**kwargs)
        assert dp_config.name == 'valcred'
        assert dp_config.class_name == 'CryptoValCred'

    def test_DPConfig__init__set_config(self):
        kwargs = {
            'domain':'snafu',
            'class_name':'CryptoValCred',
            'name':'valcred',
            'config': {
                'Certificate' : [
                    {'name':'valcred'}
                ]   
            }
        }

        dp_config = DPConfig(**kwargs)
        assert dp_config.name == 'valcred'
        assert dp_config.class_name == 'CryptoValCred'
        assert dp_config.config == {
                'CryptoValCred' : {
                    'name':'valcred',
                    'Certificate' : [
                        {
                            'name':'valcred'
                        }
                    ]
                }
            }

    def test_DPConfig_invalid_class(self):
        kwargs = {
            'domain':'snafu',
            'config': {
                'ValidationCredential' : {
                    'name':'valcred'
                }
            }
        }
        try:
            DPConfig(**kwargs)
        except ValueError:
            assert True
            

class TestDPDirectory():

    def test_DPDirectory_init_file_at_root_of_top_dir(self):
        domain = 'default'
        src = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/getCPU.js'
        dest = 'local/getCPU.js'
        dp_file = DPFile(domain, src, dest)

        assert dp_file.remote_path == 'getCPU.js'
        assert dp_file.top_directory == 'local'

    def test_DPDirectory_init_local_file_in_subdir(self):
        domain = 'default'
        src = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/getCPU.js'
        dest = 'local/GetStat/getCPU.js'
        dp_file = DPFile(domain, src, dest)

        assert dp_file.remote_path == 'GetStat/getCPU.js'
        assert dp_file.top_directory == 'local'
        
    def test_DPDirectory_init_file_not_at_root_of_top_dir(self):
        domain = 'default'
        src = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/getCPU.js'
        dest = 'local/subdir/getCPU.js'

        dp_file = DPFile(domain, src, dest)

        assert dp_file.remote_path == 'subdir/getCPU.js'
        assert dp_file.top_directory == 'local'

    def test_DPDirectory_init_LocalFile(self):
        domain = 'default'
        src = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/getCPU.js'
        dest = 'local/subdir/getCPU.js'

        dp_file = DPFile(domain, src, dest)

        assert dp_file.local_file == LocalFile(src)


