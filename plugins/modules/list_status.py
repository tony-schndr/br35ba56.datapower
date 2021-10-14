#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: list_status

short_description: List status types that can be retrieved from DataPower.

version_added: "1.0.0"

description:  List status types that can be retrieved from DataPower.
    This module would be used to determine a valid status object for the "status" module.

author:
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
- name: List all status objects.
  community.datapower.list_status:
'''

RETURN = r'''
statuses:
    description: A list of all valid status objects in datapower.
        Use the values for determine what is a valid status to fetch in the status module.
    type: list
    returned: on success
    sample: [
        "...",
        "ConfigSequenceStatus",
        "ConnectionsAccepted",
        "CountLimitAssemblyStatus",
        "CPUUsage",
        "CryptoEngineStatus2",
        "CryptoHwDisableStatus",
        "CryptoModeStatus",
        "CurrentSensors",
        "DateTimeStatus",
        "DateTimeStatus2",
        "DebugActionStatus",
        "DNSCacheHostStatus4",
        "DNSNameServerStatus2",
        "DNSSearchDomainStatus",
        "DNSStaticHostStatus",
        "DocumentCachingSummary",
        "DocumentStatusSimpleIndex",
        "DomainCheckpointStatus",
        "DomainsMemoryStatus2",
        "DomainStatus",
        "DynamicQueueManager",
        "EnvironmentalFanSensors",
        "EthernetInterfaceStatus",
        "FailureNotificationStatus2",
        "FilePollerStatus",
        "FilesystemStatus",
        "FirmwareStatus2",
        "FirmwareVersion3",
        "GatewayPeeringCacheStatus",
        "GatewayPeeringKeyStatus",
        "GatewayPeeringStatus",
        "GatewayTransactions",
        "..."
    ]
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError, Connection
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ListStatusObjectsRequest
)


def run_module():
    module_args = {}
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    connection = Connection(module._socket_path)

    dp_req = ListStatusObjectsRequest(connection)

    result = {}

    try:
        response = dp_req.get()
    except ConnectionError as e:
        response = to_text(e)
        module.fail_json(msg=response, **result)

    statuses = [key for key in response['_links'].keys() if key != 'self']
    result['statuses'] = statuses
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
