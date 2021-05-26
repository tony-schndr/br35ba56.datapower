#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import base64
import os
from difflib import context_diff
from filecmp import dircmp
import hashlib


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False


def get_file_md5(path, block_size=2**20):
    md5 = hashlib.md5()
    with open (path,'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5


class LocalFile:
    def __init__(self, path:str, content:str=None):
        # set content if you are creating the file using a base64 encoded string from DataPower REST Mgmt Interface.
        if os.path.isfile(path) and content == None:
            self.md5 = get_file_md5(path)
        elif not os.path.isfile(path) and content:
            self.md5 = self.create_file_from_base64(path, content)
        elif os.path.isfile(path) and content:
            raise FileNotFoundError('content was provided and {path} already exists.'.format(path=path))
        elif not os.path.isfile(path) and content == None:
            raise Exception('no content provided and {path} does not exist'.format(path=path))
        else:
            raise NotImplementedError
        self.path = path

    def create_file_from_base64(self, path, content):
        md5 = hashlib.md5()
        if not os.path.exists(os.path.dirname(path)):
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




if __name__ == '__main__':

    dir_path_from = '/Users/anthonyschneider/DEV/ansible-datapower-playbooks/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/test/from/'
    dir_path_to = '/Users/anthonyschneider/DEV/ansible-datapower-playbooks/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/test/to/'

    ld_from = LocalDirectory(dir_path_from)
    ld_to = LocalDirectory(dir_path_to)

    dcmp = DirectoryComparitor(ld_from, ld_to)
    fc = list(dcmp.get_diff_files())[0]

    assert isinstance(fc, FileDiff)

    #print(fc)
    content = 'LyoKICAgICBTY3JpcHQgTmFtZTogZ2V0Q1BVLmpzCiAgICAgUHVycG9zZTogR2V0IFN0YXRpc3RpY3MgdGhhdCBjYW5ub3QgYmUgcHJvZHVjZWQgYnkgdGhlIGxvZyB0YXJnZXQgb24gRGF0YVBvd2VyLgogICAgIFJldmlzaW9uczoJVmVyc2lvbgkJRGF0ZQkJQXV0aG9yCQlEZXNjcmlwdGlvbgoJCQkJMS4wLjAgICAgIAkyMDE5CQlXaWxsIExpYW8JSW5pdGlhbCBSZXZpc2lvbgogKi8KCnZhciBzbSA9IHJlcXVpcmUoJ3NlcnZpY2UtbWV0YWRhdGEnKTsKdmFyIGhtID0gcmVxdWlyZSgnaGVhZGVyLW1ldGFkYXRhJyk7CnZhciB1cmxvcGVuID0gcmVxdWlyZSgndXJsb3BlbicpOwp2YXIgY3QgPSBobS5jdXJyZW50LmdldCgnQ29udGVudC1UeXBlJyk7CnZhciBjdHggPSBzZXNzaW9uLm5hbWUoJ2dldHN0YXQnKSB8fCBzZXNzaW9uLmNyZWF0ZUNvbnRleHQoJ2dldHN0YXQnKTsKdmFyIHZBcHBsaWFuY2UgPSBjdHguZ2V0VmFyKCdkZXZpY2VuYW1lJykucmVwbGFjZSgnPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4nLCcnKSB8fCAwOwp2YXIgdkRvbWFpbk5hbWUgPSBzbS5nZXRWYXIoInZhcjovL3NlcnZpY2UvZG9tYWluLW5hbWUiKTsKdmFyIHZMb2dDYXRlZ29yeSA9IHsnY2F0ZWdvcnknOidHZXRTdGF0Q2F0ZWdvcnknfTsKdmFyIHZIb3N0ID0gImh0dHBzOi8vTUdNVDo1NTU0L21nbXQvc3RhdHVzL2RlZmF1bHQvQ1BVVXNhZ2UiOwp2YXIgdlhNTENvbnRlbnRUeXBlID0gImFwcGxpY2F0aW9uL2pzb24iOwoJLy8gZGVmaW5lIHRoZSB1cmxvcGVuIG9wdGlvbnMKCXZhciBvcHRpb25zID0gewoJdGFyZ2V0IDogdkhvc3QsCgltZXRob2QgOiAnR0VUJywKCWNvbnRlbnRUeXBlIDogdlhNTENvbnRlbnRUeXBlLAoJdGltZW91dCA6IDIKfTsKCi8vIG9wZW4gY29ubmVjdGlvbiB0byB0YXJnZXQgYW5kIHNlbmQgZGF0YSBvdmVyCnVybG9wZW4ub3BlbihvcHRpb25zLCBmdW5jdGlvbiAoZXJyb3IsIHJlc3BvbnNlKSB7CglpZiAoZXJyb3IpIHsKCQkvLyBhbiBlcnJvciBvY2N1cnJlZCBkdXJpbmcgcmVxdWVzdCBzZW5kaW5nIG9yIHJlc3BvbnNlIGhlYWRlciBwYXJzaW5nCgkJY29uc29sZS5sb2coJ3VybG9wZW4gZXJyb3I6ICcgKyBlcnJvcik7CgkJc2Vzc2lvbi5vdXRwdXQud3JpdGUoInVybG9wZW4gY29ubmVjdCBlcnJvcjogIiArIGVycm9yKTsKCX0gZWxzZSB7CgkJLy8gcmVhZCByZXNwb25zZSBkYXRhCgkJLy8gZ2V0IHRoZSByZXNwb25zZSBzdGF0dXMgY29kZQoJCXZhciByZXNwb25zZVN0YXR1c0NvZGUgPSByZXNwb25zZS5zdGF0dXNDb2RlOwoJCWlmIChyZXNwb25zZVN0YXR1c0NvZGUgPT0gMjAwKSB7CgkJCXJlc3BvbnNlLnJlYWRBc0pTT04oZnVuY3Rpb24oZXJyLCByZWFkQXNKU09OUmVzcG9uc2UpIHsKCQkJCWlmIChlcnIpIHsKCQkJCQlzZXNzaW9uLnJlamVjdCgicmVhZEFzSlNPTiBlcnJvcjogIiArIEpTT04uc3RyaW5naWZ5KGVycikpOwoJCQkJfSBlbHNlIHsKCQkJCQlzZXNzaW9uLm91dHB1dC53cml0ZSgiIFN1Y2Nlc3MgIik7CgkJCQkJCgkJCQkJY29uc29sZS5vcHRpb25zKHZMb2dDYXRlZ29yeSkubG9nKCJBcHBsaWFuY2U6ICIgKyB2QXBwbGlhbmNlICsgIiwgQ1BVVXNhZ2U6ICIgKyBKU09OLnN0cmluZ2lmeShyZWFkQXNKU09OUmVzcG9uc2UuQ1BVVXNhZ2UudGVuU2Vjb25kcykpOwoJCQkJfQoJCQl9KTsKCQkJfTsKCQl9Cgl9KTsK'
    lf = LocalFile(path='/Users/anthonyschneider/DEV/ansible-datapower-playbooks/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/files/test.js')#, content=content)
    print(lf.md5.hexdigest(), lf.md5.hexdigest())
    lf1 = LocalFile(path='/Users/anthonyschneider/DEV/ansible-datapower-playbooks/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/files/same_file_as_test.js')

    print(lf == lf1)
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
