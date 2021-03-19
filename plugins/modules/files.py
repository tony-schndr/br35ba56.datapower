#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: files

short_description: Manipulate DataPower's file system.


version_added: "1.0.0"

description: Use for uploading singular files or an entire directory recursively.  Behavior of this module is similar 
    to the ansible builtin file/copy modules.

options:
    domain:
        description: Domain to upload the file too
        required: true
        type: str
    content:
        description: String or Base64 representation of a file.
        required: false
        type: str
    src:
        description: The location of the file on the machine executing this module.
        required: false
        type: str
    dest:
        description: The destination of the file or directory upload.
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
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import (
    ConnectionError, 
    Connection
) 
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPFileStoreRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.filestore import (
    DPFileStore
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPRequestHandler
)
def run_module():
    
    module_args = dict(
        domain = dict(type='str', required=True),
        content = dict(type='str', required=False),
        src = dict(type='str', required=False),
        dest = dict(type='str', required=True),
        #backup = dict(type='bool', required=False),
        recurse = dict(type='bool', required=False, default=False),
        state = dict(type='str', required=True, choices=['absent', 'directory', 'file'])
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[['content', 'src']]
    )

    fs = DPFileStore(module.params)
    req = DPFileStoreRequest(fs)
    connection = Connection(module._socket_path)
    dp_handler = DPRequestHandler(connection)
    result = {}
    
    if module.params['state'] == 'file':
        fs_req = req.file_req('PUT')
        try:
            result['request'] = {'path': fs_req[0],'method': fs_req[1],'body': fs_req[2]}
            response = dp_handler.process_request(fs_req[0], fs_req[1], fs_req[2])
            result['response'] = response
            result['changed'] = True
            module.exit_json(**result)
        except ConnectionError as ce:
            response = to_text(ce)
            result['request'] = {'path': fs_req[0],'method': fs_req[1],'body': fs_req[2]}
            result['changed'] = False
            result['response'] = response
            module.fail_json(msg=response, **result)
        
    elif module.params['state'] == 'directory':
        responses = {}
        responses['directories'] = []
        responses['files'] = []
        requests = {}
        requests['directories'] = []
        requests['files'] = []

        # Create Directories
        for dir_req in req.dir_reqs():
            requests['directories'].append(dir_req)
            try:
                #Check if the directroy exists
                response = dp_handler.process_request(dir_req[0][0], dir_req[0][1], dir_req[0][2])
                responses['directories'].append(response)
            except ConnectionError as ce:
                if 'Resource not found.' in to_text(ce):
                    try:
                        response = dp_handler.process_request(dir_req[1][0], dir_req[1][1], dir_req[1][2])
                        responses['directories'].append(response)
                        result['changed'] = True
                    except ConnectionError as ce:
                        responses['directories'].append(to_text(ce))
                        result['requests'] = requests
                        result['responses'] = responses
                        module.fail_json(msg=to_text(ce), result=result)
                else:
                    module.fail_json(msg=to_text(ce), result=result)
        # Create Files
        for file_req in req.file_reqs('PUT'):
            requests['files'].append(file_req)
            try:
                response = dp_handler.process_request(file_req[0], file_req[1], file_req[2])
                responses['files'].append(response)
                result['changed'] = True
            except ConnectionError as ce:
                responses['files'].append(to_text(ce))
                result['responses'] = responses
                module.fail_json(msg=to_text(ce), result=result)

        result['requests'] = requests
        result['responses'] = responses
        module.exit_json(**result)

    else: #module.params['state'] == 'absent'
        try:
            fs_req = req.del_req()
            result['request'] = {'path': fs_req[0],'method': fs_req[1],'body': fs_req[2]}
            response = dp_handler.process_request(fs_req[0], fs_req[1], fs_req[2])
            result['response'] = response
            result['changed'] = True
            module.exit_json(**result)
        except ConnectionError as ce:
            response = to_text(ce)
            result['response'] = response
            result['changed'] = False
            module.fail_json(msg=response, **result)


def main():
    run_module()


if __name__ == '__main__':
    main()