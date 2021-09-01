from __future__ import absolute_import, division, print_function

__metaclass__ = type

import base64
import os
import hashlib


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
    def __init__(self, path: str, content: str = None):
        # set content if you are creating the file using a base64 encoded string from DataPower REST Mgmt Interface.
        if os.path.isfile(path) and content is None:
            self.md5 = get_file_md5(path)
        elif not os.path.isfile(path) and content:
            self.md5 = self.create_file_from_base64(path, content)
        elif os.path.isfile(path) and content:
            raise FileNotFoundError(
                'content was provided and {path} already exists.'.format(path=path))
        elif not os.path.isfile(path) and content is None:
            raise Exception(
                'no content provided and {path} does not exist'.format(path=path))
        else:
            raise NotImplementedError
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
        with open(self.path, 'r') as fb:
            lines = fb.readlines()
        return lines

    def __eq__(self, o):
        if isinstance(o, LocalFile):
            return self.md5.hexdigest() == o.md5.hexdigest()
        return False

    def __str__(self):
        return self.path
