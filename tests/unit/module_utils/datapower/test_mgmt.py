from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import os

import pytest


from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPDirectory,
    DPFile,
    InvalidDPDirectoryException
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    LocalFile
)

def test_get_top_dir():
    pass



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


