from __future__ import absolute_import, division, print_function

__metaclass__ = type

import base64
import os
import hashlib
import posixpath
from difflib import context_diff


def copy_file_to_tmp_directory(module, tmpdir, src, dest, content):
    tmp_path = os.path.join(tmpdir, dest.lstrip('/'))
    os.makedirs(os.path.split(tmp_path)[0])

    if src and os.path.isfile(src):
        module.preserved_copy(src, tmp_path)

    return LocalFile(path=tmp_path, content=content)


def get_file_diff(from_local_file, to_local_file, dest, state):
    if state == 'present':
        if from_local_file and to_local_file:
            return list(context_diff(
                a=from_local_file.get_lines(),
                b=to_local_file.get_lines(),
                fromfile='before: ' + dest,
                tofile='after: ' + dest,
                n=3
            ))
        elif to_local_file and from_local_file is None:
            return {
                'before': None,
                'after': dest
            }
    elif from_local_file:
        return {
            'before': dest,
            'after': None
        }
    else:
        return {'before': None, 'after': None}


def get_files_from_filestore(filestore):
    if isinstance(filestore['filestore']['location']['file'], dict):
        return [filestore['filestore']['location']['file']['href']]
    else:
        return [file['href'] for file in filestore['filestore']['location']['file']]


def get_parent_dir(path):
    # Get the parent directory
    return posixpath.split(path)[0]


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False


def get_file_md5(path, block_size=2**20):
    md5 = hashlib.md5()
    with open(path, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5


class LocalFile:
    def __init__(self, path, content=None):

        if content:
            self.md5 = self.create_file_from_base64(path, content)
        elif os.path.isfile(path):
            self.md5 = get_file_md5(path)
        else:
            raise Exception('No content provided and {path} is not a file'.format(path=path))

        self.path = path

    def create_file_from_base64(self, path, content):
        md5 = hashlib.md5()
        if not os.path.exists(os.path.dirname(path)) and os.path.dirname(path) != '':
            os.makedirs(os.path.dirname(path))

        with open(path, 'wb') as f:
            data = base64.b64decode(content)
            f.write(data)
            md5.update(data)
        return md5

    def get_base64(self):
        with open(self.path, 'rb') as fb:
            data = fb.read()
        return base64.b64encode(data).decode()

    def get_lines(self):
        with open(self.path, 'r', encoding='utf-8') as fb:
            lines = fb.readlines()
        return lines

    def __eq__(self, o):
        if isinstance(o, LocalFile):
            return self.md5.hexdigest() == o.md5.hexdigest()
        return False

    def __str__(self):
        return self.path
