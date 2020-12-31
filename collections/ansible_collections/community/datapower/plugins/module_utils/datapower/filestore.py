from __future__ import absolute_import, division, print_function

__metaclass__ = type

import base64

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode('ascii') == s
    except Exception:
        return False

class DPFileStore:
    def __init__(self, params):
        self.set_content(params)
        self.set_filename(params)
        self.set_dest(params)
        self.src = params['src']
        self.root_dir = self.dest.split('/')[0]
        
        if self.root_dir not in ['local', 'sharedcert', 'cert']:
            raise AttributeError('dest path must specify one of (local | sharecert | cert) as the root of the path')
        

    def set_dest(self, params):
        self.dest = params['dest'].lstrip('/').rstrip('/')

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
                self.content = base64.b64encode(content)
        else:
            with open(params['src'], 'rb') as f:
                file_content = f.read()
                self.content = base64.b64encode(file_content).decode('ascii')