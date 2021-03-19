#!/usr/bin/env python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''

'''

EXAMPLES = r'''
    
'''

RETURN = r'''

'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower import DPDownloadFile

def run_module():
    module_args = dict(
        domain = dict(type='str', required=True),
        body = dict(type='dict', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    
    if module.check_mode:
        # Check if the file exists
        module.exit_json(**result)

    result = dict(
        changed=False
    )

    dp_mod = DPDownloadFile(module)
    
    try:
        result = dp_mod.send_request()
    except ConnectionError as ce:
        result = dict()
        result['changed'] = False
        module.fail_json(msg=to_text(ce), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()