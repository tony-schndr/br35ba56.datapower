#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: fetch_file

short_description: Download a file from DataPower file system

version_added: "1.0.0"

description: Download a file from DataPower file system

options:
    domain:
        description: Target domain
        required: True
        type: str
    src:
        description: DataPower File System path
        required: true
        type: path
    dest:
        description: Path to a directory in which to write the fetched file to.
        required: true
        type: path
author:
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: Download a file from the /temporary/ directory
  community.datapower.fetch_file:
    domain: default
    path: /temporary/error-report.txt.gz
    dest: /var/tmp/
'''

RETURN = r'''
path:
    description: The full path to the error report on the local filesystem
    type: str
    returned: always
    sample: /var/tmp/error-report.txt.gz
md5:
    description: md5 hexdigest
    type: str
    returned: always
    sample: e59ff97941044f85df5297e1c302d260
'''

import posixpath
import os
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import (
    ConnectionError,
    Connection
)
from ansible.module_utils._text import to_text
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    FileRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.files import (
    create_file_from_base64
)


def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            domain=dict(type='str', required=True),
            src=dict(type='path', required=True),
            dest=dict(type='path', required=True),
        ),
        supports_check_mode=True
    )
    connection = Connection(module._socket_path)
    result = {}

    domain = module.params.get('domain')
    src = module.params.get('src')
    dest = module.params.get('dest')

    file_name = posixpath.split(src)[1]

    if os.path.isdir(dest):
        full_path = posixpath.join(dest, file_name)
    else:
        module.fail_json(msg='dest should be an existing directory')

    dp_req = FileRequest(connection)
    dp_req.set_path(domain=domain, file_path=src)

    try:
        dp_resp = dp_req.get()
    except ConnectionError as e:
        module.fail_json(msg=to_text(e))

    path, md5 = create_file_from_base64(full_path, dp_resp['file'])
    result['path'] = path
    result['md5'] = md5.hexdigest()

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
