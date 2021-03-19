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
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.actionqueue import (
    DPActionQueue
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPActionQueueRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPActionQueueRequestHandler
)

def run_module():
    module_args = dict(
        domain = dict(type='str', required=True),
        parameters = dict(type='dict', required=False)
    )
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    result = {}
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()