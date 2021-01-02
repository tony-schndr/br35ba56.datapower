from __future__ import absolute_import, division, print_function

__metaclass__ = type

import base64
import os

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False


class DPFileStore:
    def __init__(self, params):
        self.set_dest(params['dest'])
        self.set_src(params['src'])
        if params['state'] == 'file':
            self.set_content(params)
            self.set_filename(params)
        
    

    def set_src(self, src):
        if src:
            self.src = src.rstrip('/')


    def dirs(self):
        for r, d, f in os.walk(self.src):
            dir = r[len(self.src):].lstrip('/').rstrip('/')
            if len(dir) != 0:
                yield self.dest + '/' + dir 


    def set_dest(self, dest):
        root_dir = dest.lstrip('/').rstrip('/').split('/')[0]
        if root_dir not in ['local', 'sharedcert', 'cert']:
            raise AttributeError('dest path must specify one of (local | sharecert | cert) as the root of the path')

        self.dest = '/' + dest.lstrip('/').rstrip('/')

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
            with open(params['src'], 'rb') as f:
                file_content = f.read()
                self.content = base64.b64encode(file_content).decode()