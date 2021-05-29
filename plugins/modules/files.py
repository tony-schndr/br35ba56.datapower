#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: files

short_description: Upload files to a DataPower domains filestore

version_added: "1.0.0"

description: Use for uploading a single file.

options:
    domain:
        description: Target domain
        required: true
        type: str
    content:
        description: String or Base64 representation of a file.
        required: false
        type: str
    src:
        description: The location of the file on the local ansible host.
        required: false
        type: path
    dest:
        description: The destination of the file or directory upload.  You must specify the top directory within the path, ie local, sharedcert, cert
        required: true
        type: path
    state:
        description: State of the file or directory on DataPower
        required: true
        type: str
        choices:
          - absent
          - present

author: 
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
# Modify a datapower object.  This example simply disables test_domain1.  
---
- name: Upload a local file called example.txt to local/subdir
  community.datapower.files:
    domain: default
    src: example.txt
    dest: local/subdir/example.txt
    state: present
      
- name: Create a local/subdir/example.txt from base64 content. 
  community.datapower.files:
    domain: default
    content: "aGVsbG8gd29ybGQK"
    dest: local/subdir/example.txt
    state: present      
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.

response:
    description: The response returned from DataPowers Rest MGMT Interface.
    type: dict
    returned: on success
    sample: {
        "_links": {
            "doc": {
                "href": "/mgmt/docs/filestore"
            },
            "self": {
                "href": "/mgmt/filestore/default/local/subdir/example.txt"
            }
        },
        "result": "File was updated."
    }
'''

import os
import random
import string
from difflib import context_diff
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import (
    ConnectionError,
    Connection
)
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    get_parent_dir,
    get_top_dir
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    LocalFile,
    LocalDirectory
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    FileRequest,
    DirectoryRequest
)

TOP_DIRS = ['local', 'cert', 'sharedcert']

def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        content=dict(type='str', required=False),
        src=dict(type='path', required=False),
        dest=dict(type='path', required=True),
        #backup = dict(type='bool', required=False),
        state=dict(type='str', required=True, choices=['absent', 'present'])
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=[['content', 'src']]
    )
    
    '''
    if src is a directory, dest must also be directory
    if src and dest are files the parent directory of dest is not created 
    and the task fails if it does not already exist.
    '''

    connection = Connection(module._socket_path)
    result = {}

    domain = module.params['domain']
    src = module.params.get('src', None)
    content = module.params.get('content', None)
    dest = module.params['dest']
    state = module.params['state']
    tmpdir = module.tmpdir

    if (src and os.path.isfile(src)) or content:
        local_after_file = copy_file_to_tmp_directory(module, tmpdir, src, dest, content)
        remote_after_file_path = dest#get_dest_file_path(dest)
        remote_after_file_parent_dir = get_parent_dir(remote_after_file_path)
        
        file_req = FileRequest(connection)
        file_req.set_path(domain, remote_after_file_path)
        file_req.set_body(remote_after_file_path, local_after_file.get_base64())
        result['local_after_file'] = str(local_after_file)
        result['remote_after_file_path'] = remote_after_file_path
        result['remote_after_file_parent_dir'] = remote_after_file_parent_dir
        dir_req = DirectoryRequest(connection)
        dir_req.set_body(remote_after_file_parent_dir)
        dir_req.set_path(domain, remote_after_file_parent_dir)


        try:
            remote_parent_dir = get_remote_filestore_resources(dir_req)
            result['remote_parent_dir'] = remote_parent_dir
        except ConnectionError as ce:
            result['changed'] = False
            module.fail_json(msg=to_text(ce), **result)
        
        try:
            remote_before_file = get_remote_filestore_resources(file_req)
            result['remote_before_file'] = remote_before_file
        except ConnectionError as ce:
            result['changed'] = False
            module.fail_json(msg=to_text(ce), **result)

        if remote_before_file:
            remote_before_file_dest = get_dest_path_from_href(domain, href=remote_before_file['_links']['self']['href'])
            local_before_file = copy_file_to_tmp_directory(module, tmpdir, src=None, dest=remote_before_file_dest, content=remote_before_file['file'])
            result['local_before_file'] = str(local_before_file)
        else:
            local_before_file = None
        diff = get_file_diff(local_before_file, local_after_file, dest, state)
        
       
        if module._diff:
            result['diff'] = diff

        request = get_request_func(file_req, local_before_file, local_after_file, state)
        
        if module.check_mode:
            if request is not None:
                result['changed'] = True
            else:
                result['changed'] = False
            module.exit_json(**result)

        if request:
            try:
                response = dict()
                if remote_parent_dir is None:
                    result['create_dir_response'] = dir_req.create()
                result['response'] = request()
            except ConnectionError as ce:
                result['changed'] = False
                module.fail_json(msg=to_text(ce), **result)
            result['changed'] = True
        else:
            result['changed'] = False
        module.exit_json(**result)

    else:
        module.fail_json(msg='Directories are not yet supported.')
def copy_file_to_tmp_directory(module, tmpdir, src, dest, content):
    random_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    safe_src = os.path.join(tmpdir, random_string, dest.lstrip('/'))
    if src and os.path.isfile(src):
        os.makedirs(os.path.split(safe_src)[0])
        module.preserved_copy(src, safe_src)
        return LocalFile(path=safe_src)
    elif not src and content:
        # Create the source from the destination
        # Source will be created from content
        return LocalFile(path=safe_src, content=content)


def get_remote_filestore_resources(req):
    try:
        res = req.get()
    except ConnectionError as ce:
        err = to_text(ce)
        if 'Resource not found' in err:
            return None
        else:
            raise ce
    if 'filestore' in res or 'file' in res:
        return res
    else:
        raise Exception('Not a filestore resources error')


def get_dest_path_from_href(domain, href):
    return href.split(domain, 1)[1]      


def get_file_diff(from_local_file, to_local_file,dest,  state):
    if state == 'present':
        if from_local_file and to_local_file:
            return list(context_diff(
                a=from_local_file.get_lines(),
                b=to_local_file.get_lines(),
                fromfile=os.path.join('before', dest),
                tofile=os.path.join('after', dest),
                n=3
            ))
        elif to_local_file and from_local_file is None:
            return {
                'before': None,
                'after': dest
            }
    else:
        if from_local_file:
            return {
                'before': dest,
                'after': None
            }
        else:
            return {'before': None, 'after': None}


def get_request_func(req, before_file, after_file, state):
    if state == 'present':
        if before_file is None:
            return req.create
        else:
            if before_file != after_file:
                return req.update
            else:
                return None
    else:
        if before_file is None:
            return None
        else:
            return req.delete

def execute_request(module, req_func, result):
    try:
        response = req_func()
    except ConnectionError as ce:
        result['changed'] = False
        module.fail_json(msg=to_text(ce), **result)
    return response

def main():
    run_module()
    

if __name__ == '__main__':
    main()
