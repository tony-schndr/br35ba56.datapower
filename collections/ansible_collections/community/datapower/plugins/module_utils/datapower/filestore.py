from __future__ import absolute_import, division, print_function

__metaclass__ = type

import base64
import os
from glob import glob


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False


class DPFileStore:
    def __init__(self, params):
        self.domain = params['domain']
        self.set_dirs(params['dest'])
        self.set_src(params['src'])
        if params['state'] == 'file':
            self.set_content(params)
            self.set_filename(params)
            self.set_filepath_dest(params)

    def set_filepath_dest(self, params):
        self.dest = self.dest + '/' + self.file_name
        self.dest = self.dest.lstrip('/')
    
    def set_dirs(self, dest):
        root_dir = dest.lstrip('/').rstrip('/').split('/')[0]
        if root_dir in ['local', 'sharedcert', 'cert']:
            self.root_dir = root_dir
        else:
            raise AttributeError('dest path must specify one of (local | sharecert | cert) as the root of the path')            
        self.dest = '/'.join(dest.lstrip('/').rstrip('/').split('/')[1:])

    def set_filename(self, params):
        if params['src']:
            self.file_name = params['src'].split('/')[-1]
        else:
            self.file_name = params['dest'].split('/')[-1]

    def set_content(self, params):
        content = params['content']
        if content is not None:
            if isBase64(content):
                self.content = content
            else:
                self.content = base64.b64encode(str.encode(content)).decode()
        else:
            self.content = self.get_local_content(params['src'])

    def set_src(self, src):
            if src:
                self.src = src.rstrip('/')

    def dirs(self):
        #yield self.dest
        for r, d, f in os.walk(self.src):
            dir = self.dest + '/' + r[len(self.src):].strip('/')
            if len(dir) != 0:
                yield dir

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
            