from __future__ import absolute_import, division, print_function

__metaclass__ = type

import base64
import os
import re
from glob import glob


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False


class DPFileStore:
    def __init__(self, params=None):
        if params:
            self.domain = params['domain']

            if params['state'] == 'directory':
                self.set_dirs(params['dest'])
                self.set_src(params['src'])
            elif params['state'] == 'file':
                self.set_content(params)
                if self.is_dest_valid_file_path(params['dest']):
                    self.set_file_name(params['dest'])
                    self.dest = params['dest'].lstrip('/')
                else:
                    self.set_file_name(params['src'])
                    self.dest = params['dest'].lstrip('/').rstrip('/') + '/' + self.file_name
            elif params['state'] == 'absent':
                self.dest = params['dest'].lstrip('/').rstrip('/')

    def set_file_name(self, file_name):
        self.file_name = file_name.split('/')[-1]
        
    # Need to determine if the destination is a valid file path.
    # This is not valid /local/GetStat
    # This is valid /local/GetStat/CPU.xsl
    @staticmethod  
    def is_dest_valid_file_path(dest):
        return re.match(r'[\w,\s-]+\.[A-Za-z]{1,4}', dest.split('/')[-1])
    
    def set_src(self, src):
        self.src = src.rstrip('/')

    @staticmethod
    def has_valid_root_dir(root_dir):
        if root_dir not in ['local', 'sharedcert', 'cert']:
             raise AttributeError('dest path must specify one of (local | sharecert | cert) as the root of the path')
        else:
            return True
           
    def set_dirs(self, dest):
        root_dir = dest.lstrip('/').rstrip('/').split('/')[0]
        if self.has_valid_root_dir(root_dir):
            self.root_dir = root_dir
            self.dest = '/'.join(dest.lstrip('/').rstrip('/').split('/')[1:])

    def set_content(self, params):
        content = params['content']
        if content is not None:
            if isBase64(content):
                self.content = content
            else:
                self.content = base64.b64encode(str.encode(content)).decode()
        else:
            self.content = self.get_local_content(params['src'])

    def dirs(self):
        for r, d, f in os.walk(self.src):
            dir = self.dest + '/' + r[len(self.src):].strip('/')
            if len(dir) != 0:
                yield dir.lstrip('/').rstrip('/')

    def files(self):
        for g in glob(self.src + '/**/*', recursive=True):
            if os.path.isfile(g):
                path = self.dest + '/' + g[len(self.src):].strip('/').rstrip('/')
                file_name = g.split('/')[-1]
                content = self.get_local_content(g)
                yield path, file_name, content,

    def get_local_content(self, f):
        if os.path.isfile(f):
            with open(f, 'rb') as fb:
                data = fb.read()
            return base64.b64encode(data).decode()
        else:
            raise FileNotFoundError
            