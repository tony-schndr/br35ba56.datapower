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
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import (
    ConnectionError, 
    Connection
) 
from ansible.module_utils.basic import AnsibleModule

#from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
   # DPFileStoreRequest
#)
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    LocalFile
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPRequestHandler
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPFileStoreRequests
)

TOP_DIRS = ['local', 'cert', 'sharedcert' ]


def get_top_dir(dest):
    top_dir = dest.split('/')[0]
    if top_dir in TOP_DIRS:
        return top_dir
    else:
        raise Exception('Invalid top directory, must be one of ', ' '.join(TOP_DIRS))

def get_file_path(dest):
    if get_top_dir(dest):
        #if dest.endswith('/')
            
        file_path = '/'.join(dest.split('/')[1:-1])
        return file_path
    raise Exception('Invalid path, top directory incorrect.')

def run_module():
    module_args = dict(
        domain = dict(type='str', required=True),
        content = dict(type='str', required=False),
        src = dict(type='str', required=False),
        dest = dict(type='path', required=True),
        #backup = dict(type='bool', required=False),
        recurse = dict(type='bool', required=False, default=False),
        state = dict(type='str', required=True, choices=['absent', 'directory', 'file'])
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[['content', 'src']]
    )
    
    #module.params['']
'''
if src is a directory, dest must also be directory

'''
    connection = Connection(module._socket_path)
    dp_handler = DPRequestHandler(connection)
    result = {}
    if module.params['state'] == 'file':
        src_lf = LocalFile(module.params['src'])
        top_directory = get_top_dir(module.params['dest'])
        # Try to GET the destination file and save
        # Check if the files are equal
        # Change if src_lf not equal to dest_lf or dest_lf not present
        get_file_request = DPFileStoreRequests.get_file_request(
            domain = 'default',
            top_directory=top_directory, 
            file_path = 'get.js')
        result['local_file'] = str(src_lf)
        result['get_file_request'] = get_file_request
        module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()