#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import base64
import os
import sys
import re
import shutil
from glob import glob
from difflib import context_diff
from filecmp import dircmp
from datetime import datetime, timezone

WORK_DIR = '/var/tmp/.ansible_community_datapower_workdir'


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False


def file_mtime(path):
    t = datetime.fromtimestamp(os.stat(path).st_mtime,
                               timezone.utc)
    return t.astimezone().isoformat()


class LocalFile:
    def __init__(self, path:str, content:str=None):
        # set content if you are creating the file via base64 encoding.
        if content:
            self.content = content
        if os.path.isfile(path):
            self.path = path
        else:
            raise FileNotFoundError
        self.mod_time = file_mtime(self.path)

    def get_base64(self):
        with open(self.path, 'rb') as fb:
            data = fb.read()
        return base64.b64encode(data).decode()

    def get_lines(self):
        with open(self.path, 'r') as fb:
            lines = fb.readlines()
        return lines

    def __str__(self):
        return self.path


class LocalDirectory:
    def __init__(self, path):
        if os.path.isdir(path):
            self.path = path
            self.root = path.rstrip('/').split('/')[-1]
        else:
            raise NotADirectoryError

    def list_sub_dirs(self):
        for r, d, f in os.walk(self.path):
            yield r,

    def get_local_files(self):
        for r, d, files in os.walk(self.path):
            for file_ in files:
                yield LocalFile(os.path.join(r, file_))


class DirectoryComparitor:
    def __init__(self, ld_from:LocalDirectory, ld_to:LocalDirectory):
        self.ld_from = ld_from
        self.ld_to = ld_to
        self.dircmp = dircmp(self.ld_from.path, self.ld_to.path)

    def get_diff_files(self):
        def gen_diff_files(files, dcmp):
            for name in dcmp.diff_files:
                from_local_file = LocalFile(os.path.join(dcmp.left, name))
                to_local_file = LocalFile(os.path.join(dcmp.right, name))
                files.append(FileDiff(from_local_file, to_local_file))
            for sub_dcmp in dcmp.subdirs.values():
                gen_diff_files(files, sub_dcmp)
        files = []
        gen_diff_files(files, self.dircmp)
        return files


class FileDiff:

    def __init__(self, from_local_file:LocalFile, to_local_file:LocalFile):
        self.from_local_file = from_local_file
        self.to_local_file = to_local_file

    def get_context_diff(self):
        return context_diff(
            a=self.from_local_file.get_lines(),
            b=self.to_local_file.get_lines(),
            fromfile=self.from_local_file.path,
            tofile=self.to_local_file.path,
            n=3
        )

    def __str__(self):
        return "".join(self.get_context_diff())


class DPDirectory:
    # attributes needed for creating a directory on DataPower.
    def __init__(self):
        pass



if __name__ == '__main__':

    dir_path_from = '/Users/anthonyschneider/DEV/ansible-datapower-playbooks/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/test/from/'
    dir_path_to = '/Users/anthonyschneider/DEV/ansible-datapower-playbooks/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/test/to/'

    ld_from = LocalDirectory(dir_path_from)
    ld_to = LocalDirectory(dir_path_to)

    dcmp = DirectoryComparitor(ld_from, ld_to)
    fc = list(dcmp.get_diff_files())[0]

    assert isinstance(fc, FileDiff)

    print(fc)

    '''
    file_diffs = []
    print(list(dcmp.get_diff_files()))
    for lf in dcmp.get_diff_files():
        print(type(lf))
    for files in dcmp.get_diff_files():
        #print('comparing: ', files[0],files[1])
        local_file_from = files[0]
        local_file_to = files[1]
        file_cmp = FileComparitor(
            local_file_from,
            local_file_to
        )
        
        file_diff = file_cmp.get_diff()
       # print(file_diff)
        sys.stdout.writelines(file_diff)
        '''
