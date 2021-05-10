from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import os

import pytest


from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    LocalFile,
    LocalDirectory,
    DirectoryComparitor,
    FileDiff
)


class TestLocalFile():

    def test_LocalFile_with_src(self):
        file_path = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/getCPU.js'
        try:
            LocalFile(file_path)
            created = True
        except:
            created = False
        assert created == True

    def test_LocalFile_with_src_and_content(self):
        file_path = '/tmp/getMemory.js'
        content = 'aGVsbG8gd29ybGQK'
        try:
            LocalFile(file_path, content)
            created = True
        except:
            created = False
        assert created == True

    def test_LocalFile_with_src_and_content_file_already_exists(self):
        file_path = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/getCPU.js'
        content = 'aGVsbG8gd29ybGQK'
        try:
            LocalFile(file_path, content)
            assert False
        except:
            assert True

    def test_LocalFile_with_good_file_path(self):
        file_path = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/getCPU.js'
        try:
            LocalFile(file_path)
            created = True
        except:
            created = False
        assert created == True

    def test_LocalFile_with_bad_file_path(self):
        bad_file_path = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/not-a-file.txt'
        try:
            LocalFile(bad_file_path)
            assert False
        except:
            assert True

    def test_LocalFile_equal(self):
        file_path_1 = './tests/unit/module_utils/test_data/files/test.js'
        file_path_2 = './tests/unit/module_utils/test_data/files/same_file_as_test.js'

        lf1 = LocalFile(file_path_1)
        lf2 = LocalFile(file_path_2)

        assert lf1 == lf2

    def test_LocalFile_not_equal(self):
        file_path_1 = './tests/unit/module_utils/test_data/files/test.js'
        file_path_2 = './tests/unit/module_utils/test_data/files/diff_from_test.js'

        lf1 = LocalFile(file_path_1)
        lf2 = LocalFile(file_path_2)

        assert lf1 != lf2

    def test_LocalFile_get_lines_returns_list_len_gr_zero(self):
        file_path = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/getCPU.js'
        lf = LocalFile(file_path)
        assert len(lf.get_lines()) > 0

    def test_LocalFile_get_lines_returns_list_of_str(self):
        file_path = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/getCPU.js'
        lf = LocalFile(file_path)
        for line in lf.get_lines():
            assert isinstance(line, str)

    def test_LocalFile_md5(self):
        file_path = './tests/unit/module_utils/test_data/copy/test/from/GetStat/new/getCPU.js'
        lf = LocalFile(file_path)
        assert lf.md5

class TestLocalDirectory():

    def test_LocalDirectory_good_path(self):
        dir_path = './tests/unit/module_utils/test_data/copy/test/from/GetStat'
        try:
            LocalDirectory(dir_path)
            created = True
        except:
            created = False
        assert created == True

    def test_LocalDirectory_bad_path(self):
        dir_path = './tests/unit/module_utils/test_data/copy/test/from/GetStat/bad_path'
        try:
            LocalDirectory(dir_path)
            created = True
        except:
            created = False
        assert created == False

    def test_LocalDirectory_get_local_files(self):
        dir_path = './tests/unit/module_utils/test_data/copy/test/from/GetStat/'
        ld = LocalDirectory(dir_path)
        for lf in ld.get_local_files():
            assert isinstance(lf, LocalFile)


class TestDirectoryComparitor:

    def test_DirectoryComparitor_to_from_assignment(self):
        dir_path_from = './tests/unit/module_utils/test_data/copy/test/from/'
        dir_path_to = './tests/unit/module_utils/test_data/copy/test/to/'
        ld_from = LocalDirectory(dir_path_from)
        ld_to = LocalDirectory(dir_path_to)

        dcmp = DirectoryComparitor(ld_from, ld_to)
        assert dcmp.ld_from == ld_from
        assert dcmp.ld_to == ld_to

    def test_DirectoryComparitor_get_diff_files(self):
        dir_path_from = './tests/unit/module_utils/test_data/copy/test/from/'
        dir_path_to = './tests/unit/module_utils/test_data/copy/test/to/'
        ld_from = LocalDirectory(dir_path_from)
        ld_to = LocalDirectory(dir_path_to)

        dcmp = DirectoryComparitor(ld_from, ld_to)
        assert len(list(dcmp.get_diff_files())) > 0
        for fc in dcmp.get_diff_files():
            assert isinstance(fc, FileDiff)


class TestFileDiff:

    def test_FileDiff(self):
        dir_path_from = './tests/unit/module_utils/test_data/copy/test/from/'
        dir_path_to = './tests/unit/module_utils/test_data/copy/test/to/'
        ld_from = LocalDirectory(dir_path_from)
        ld_to = LocalDirectory(dir_path_to)

        dcmp = DirectoryComparitor(ld_from, ld_to)
        fc = list(dcmp.get_diff_files())[0]

        assert isinstance(fc, FileDiff)

    def test_FileDiff_context_dict(self):
        dir_path_from = './tests/unit/module_utils/test_data/copy/test/from/'
        dir_path_to = './tests/unit/module_utils/test_data/copy/test/to/'
        ld_from = LocalDirectory(dir_path_from)
        ld_to = LocalDirectory(dir_path_to)

        dcmp = DirectoryComparitor(ld_from, ld_to)
        fc = list(dcmp.get_diff_files())[0]

        assert fc.get_context_diff()
