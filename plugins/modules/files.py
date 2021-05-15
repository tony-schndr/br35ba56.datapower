#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)


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

import os, shutil
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPFileStoreRequests
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPRequestHandler
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    LocalFile
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPFile,
    DPDirectory
)
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import (
    ConnectionError,
    Connection
)
from ansible.module_utils._text import to_text

__metaclass__ = type



WORK_DIR = '/tmp/community.datapower.workdir/'


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
        supports_check_mode=False,
        mutually_exclusive=[['content', 'src']]
    )

    # module.params['']
    # Setup the working directory
    if not os.path.exists(WORK_DIR):
        os.mkdir(WORK_DIR)
    '''
    if src is a directory, dest must also be directory
    if src and dest are files the parent directory of dest is not created 
    and the task fails if it does not already exist.
    '''

    connection = Connection(module._socket_path)
    req_handler = DPRequestHandler(connection)
    result = {}
    domain = module.params['domain']
    src = module.params['src']
    dest = module.params['dest']
    state = module.params['state']

    if state == 'present':
        if os.path.isfile(src):
            dp_file_to = DPFile(domain, src, dest, request_handler=req_handler)
            get_file_request = DPFileStoreRequests.get_file_request(
                domain=dp_file_to.domain,
                top_directory=dp_file_to.top_directory,
                file_path=dp_file_to.remote_path
            )
            try:
                get_req_result = req_handler.process_request(*get_file_request)
            except ConnectionError as gfce:
                gfce_text = to_text(gfce)
                if 'Resource not found' in gfce_text:
                    #Create file, nothing to compare
                    create_file_request = DPFileStoreRequests.create_file_request(
                        domain=dp_file_to.domain,
                        top_directory=dp_file_to.top_directory,
                        file_path=dp_file_to.remote_path,
                        content=dp_file_to.local_file.get_base64()
                    )
                    try:
                        create_file_result = req_handler.process_request(*create_file_request)
                    except ConnectionError as cfce:
                        result['changed'] = False
                        result['create_file_request'] = create_file_request
                        exit_module(module, result, fail=True, msg=to_text(cfce))
                    result['changed'] = True
                    result['create_file_result'] = create_file_result
                    exit_module(module, result, fail=False)
                else:
                    result['changed'] = False
                    result['get_file_request'] = get_file_request
                    exit_module(module, result, fail=True, msg=gfce_text)
            
            dp_file_content = get_req_result['file']
            dp_file_path = get_req_result['_links']['self']['href'].split(domain, 1)[1]
            dp_file_local_path = WORK_DIR.rstrip('/') + os.sep + dp_file_path.lstrip('/')

            dp_file_from = DPFile(domain, local_path=dp_file_local_path, remote_path=dp_file_path, content=get_req_result['file'])

            if dp_file_from.local_file == dp_file_to.local_file:
                result['changed'] = False
                exit_module(module, result, fail=False)
            else:
                update_file_request = DPFileStoreRequests.update_file_request(
                    domain=dp_file_to.domain,
                    top_directory=dp_file_to.top_directory,
                    file_path=dp_file_to.remote_path,
                    content=dp_file_to.local_file.get_base64()
                )
                try:
                    update_file_result = req_handler.process_request(*update_file_request)
                except ConnectionError as ufece:
                    result['changed'] = False
                    shutil.rmtree(WORK_DIR)
                    module.exit_json(**result)
                result['changed'] = True
                result['result'] = update_file_result
                exit_module(module, result, fail=False)
            
            

            
def exit_module(module, result, fail, msg=''):
    shutil.rmtree(WORK_DIR)
    if fail:
        module.fail_json(msg=msg, **result)
    else:
        module.exit_json(**result)

def main():
    run_module()


if __name__ == '__main__':
    main()
    


'''
        elif os.path.isdir(src):
            if src.endswith('/'):
                pass #If dest is a non-existent path and if either dest ends with "/" or src is a directory, dest is created.
            else:
                pass # 
'''