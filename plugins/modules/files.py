#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: files

short_description: Manage files in a DataPower Application Domain's filestore.

version_added: "1.0.0"

description: Manage files in a DataPower Application Domain's filestore.

options:
    domain:
        description: The Application Domain to upload the file to.
        required: true
        type: str
    content:
        description: >
                Base64 encoded file string.
        required: false
        type: str
    src:
        description: >
            The path to the file on the ansible controller.
            Currently only files can be uploaded.
        required: false
        type: path
    dest:
        description: >
            The filestore destination of the file or directory upload.
            You must specify the top directory within the path. ie local, cert, sharedcert, etc...
            For example: local/subdir/example.txt or cert/privkey.pem
            If the destination subdirectory does not exist it is created prior to uploading the file.
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

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import (
    ConnectionError,
    Connection
)
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    ensure_file
)


def run_module():
    module_args = dict(
        domain=dict(type='str', required=True),
        content=dict(type='str', required=False),
        src=dict(type='path', required=False),
        dest=dict(type='path', required=True),
        state=dict(type='str', required=True, choices=['absent', 'present'])
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_one_of=(
            ['src', 'content'],
        ),
        mutually_exclusive=(
            ['src', 'content'],
        ),
    )

    domain = module.params['domain']
    dest = module.params['dest']
    state = module.params['state']

    if module.params['content'] is not None:
        data = module.params['content'].encode('utf-8')
    else:
        try:
            with open(module.params['src'], 'rb') as f:
                data = f.read()
        except (IOError, OSError) as e:
            module.fail_json(msg='Error while reading file from disk: {0}'.format(e))

    result = ensure_file(module, domain, dest, data, state)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
