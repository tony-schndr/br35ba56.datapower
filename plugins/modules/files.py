#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
import shutil
import os
import random
import string

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import (
    ConnectionError,
    Connection
)
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPFile,
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    FileDiff
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    FileRequest,
    DirectoryRequest
)



DOCUMENTATION = r'''
---
module: files

short_description: Manipulate DataPower's file system.

version_added: "1.0.0"

description: Use for uploading a single file or an entire directory recursively.

options:
    domain:
        description: Domain to upload the file to
        required: true
        type: str
    content:
        description: String or Base64 representation of a file.
        required: false
        type: str
    src:
        description: The location of the file on the local ansible host.
        required: false
        type: str
    dest:
        description: The destination of the file or directory upload.  You must specify the top_directory within the path, ie local, sharedcert, cert
            
        required: true
        type: str
    recurse:
        description: If the src is a directory and this is set to True the directory, sub directories, and all files
            will be copied to DataPower
        required: false
        default: false
        type: bool
    state:
        description: State of the file or directory on DataPower
        required: true
        type: str
        choices:
          - absent
          - directory
          - file

author: 
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
# Modify a datapower object.  This example simply disables test_domain1.  
  
  - name: Create a datapower domain(s)
    community.datapower.files:
      domains:
      - default
      definitions:
      - Domain:
          name: test_domain1
          mAdminState: disabled
      
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
my_useful_info:
    description: The dictionary containing information about your system.
    type: dict
    returned: always
    sample: {
        'foo': 'bar',
        'answer': 42,
    }
'''


__metaclass__ = type


def get_remote_directory(req, to_file):
    req.set_path(to_file.domain, to_file.top_directory, to_file.parent_dir)
    try:
        res = req.get()
    except ConnectionError as ce:
        err = to_text(ce)
        if 'Resource not found' in err:
            return None
        else:
            raise ce
    if 'filestore' in res:
        return res
    else:
        raise Exception('Not a directory error')


def get_remote_file(domain, req):
    try:
        resp = req.get()
    except ConnectionError as ce:
        err = to_text(ce)
        if 'Resource not found' in err:
            return None
        else:
            raise ce

    if 'file' in resp:
        content = resp['file']
        path = resp['_links']['self']['href'].split(domain, 1)[1]
        local_path = WORK_DIR.rstrip('/') + os.sep + path.lstrip('/')
        return DPFile(domain, local_path=local_path, remote_path=path, content=content)
    else:
        raise Exception('Not a file error')  # TODO: Raise a better exception


def get_request_func(req, remote_file, local_file, state):
    resp = None
    if state == 'present':
        if remote_file is None:
            return req.create
        else:
            if remote_file.local_file != local_file.local_file:
                return req.update
            else:
                return None
    else:
        if remote_file is None:
            return None
        else:
            return req.delete


def get_file_diff(from_file, to_file, state):
    if state == 'present':
        if from_file and to_file:
            return list(FileDiff(from_file.local_file, to_file.local_file).get_context_diff())
        elif to_file and from_file is None:
            return {
                'before': None,
                'after': to_file.remote_path
            }
    else:
        if from_file:
            return {
                'before': from_file.remote_path,
                'after': None
            }
        else:
            return {'before': None, 'after': None}


def execute_request(module, req_func, result):
    try:
        response = req_func()
    except ConnectionError as ce:
        result['changed'] = False
        module.fail_json(msg=to_text(ce), **result)
    return response

WORK_DIR = '/tmp/community.datapower.workdir/' #+ ''.join(random.choice(string.ascii_letters) for x in range(5))

def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        content=dict(type='str', required=False),
        src=dict(type='str', required=False),
        dest=dict(type='path', required=True),
        #backup = dict(type='bool', required=False),
        state=dict(type='str', required=True, choices=['absent', 'present'])
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=[['content', 'src']]
    )
    
    
    # module.params['']
    # Setup the working directory
    if not os.path.exists(WORK_DIR):
        os.makedirs(WORK_DIR)
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


    if content or os.path.isfile(src):
        #copy the src file to tmp
        #if content was supplied, create the file using dest
        random_chars = ''.join(random.choice(string.ascii_letters) for x in range(5))
        if src:
            safe_src = os.path.join(WORK_DIR, random_chars, src.lstrip('./'))
            os.makedirs(os.path.split(safe_src)[0])
            module.preserved_copy(src, safe_src)
        else:
            # Create the source from the destination
            # Source will be created from content
            safe_src = os.path.join(WORK_DIR, random_chars, dest)

        file = DPFile(domain, safe_src, dest, content)
        req = FileRequest(connection)
        req.set_path(domain, file.top_directory, file.remote_path)
        req.set_body(file.remote_path, file.local_file.get_base64())
        dir_req = DirectoryRequest(connection)
        dir_req.set_body(file.parent_dir)
        
        try:
            remote_file = get_remote_file(domain, req)
        except ConnectionError as ce:
            result['changed'] = False
            module.fail_json(msg=to_text(ce), **result)
        
        try:
            parent_dir = get_remote_directory(dir_req, file)
        except ConnectionError as ce:
            result['changed'] = False
            module.fail_json(msg=to_text(ce), **result)

        if parent_dir is None:
            execute_request(module, dir_req.create, result)

        diff = get_file_diff(remote_file, file, state)
        request = get_request_func(req, remote_file, file, state)

        if module._diff:
            result['diff'] = diff

        if module.check_mode:
            if request is not None:
                result['changed'] = True
            else:
                result['changed'] = False
            module.exit_json(**result)

        if request:
            try:
                result['response'] = request()
            except ConnectionError as ce:
                result['changed'] = False
                module.fail_json(msg=to_text(ce), **result)
            result['changed'] = True
        else:
            result['changed'] = False
        module.exit_json(**result)

    elif os.path.isdir(src):
        
        module.fail_json(msg='directory uploads are not supported at this time.')
def main():
    try:
        run_module()
    except Exception as e:
        raise e
    finally:
        shutil.rmtree(WORK_DIR)
    

if __name__ == '__main__':
    main()

