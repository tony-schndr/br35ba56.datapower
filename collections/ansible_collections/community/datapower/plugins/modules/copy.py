#!/usr/bin/env python

# Copyright: (c) 2020, YAnthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: community.datapower.upload_file

short_description: Use for uploading a file to DataPower


version_added: "1.0.0"

description: Use for uploading a file to DataPower

options:
    domain:
        description: Domain to upload the file too
        required: true
        type: list
    content:
        description: Base64 encoded string represenation of the file.
        required: false
        type: str
    src:
        description: The location of the file on the machine executing this module.
        required: false
        type: str
    dest:
        description: The location of the file in the DataPower Domain
        required: true
        type: str
    


author:
    - Anthony Schneider
'''

EXAMPLES = r'''
# Modify a datapower object.  This example simply disables test_domain1.  
  
  - name: Create a datapower domain(s)
    community.datapower.upload_file:
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
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPRequestHandler
)
def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        domain = dict(type='str', required=True),
        content = dict(type='str', required=False),
        src = dict(type='str', required=False),
        dest = dict(type='str', required=True),
        backup = dict(type='bool', required=False),
        overwrite = dict(type='bool', required=False, default=False)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=['content', 'src']
    )

    connection = Connection(module._socket_path)
    dp_handler = DPRequestHandler(connection)
    dp_req = DPFileStoreRequest(module.params)
    result = {}
    

    try:# put check code here, we can get the file, then determine if we need to 
        # update it.  Hopefully coding here will allow the ability to recursively upload
        # files
        response = dp_handler.process_request(dp_req.path, dp_req.method, dp_req.body)
    except ConnectionError as ce:
        response = to_text(ce)
        result['request'] = {'path': dp_req.path,'method': dp_req.method,'body': dp_req.body}
        result['changed'] = False
        module.fail_json(msg=response, **result)

    result['request'] = {'path': dp_req.path,'method': dp_req.method,'body': dp_req.body}    
    result['response'] = response
    result['changed'] = True
    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()