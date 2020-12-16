from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPActionQueueRequestHandler
)

def test_action_process_request():
    resp = {
        "_links": {
            "self": {
                "href": "/mgmt/actionqueue/snafu"
            },
            "doc": {
                "href": "/mgmt/docs/actionqueue"
            },
            "location": {
                "href": "/mgmt/actionqueue/snafu/pending/ResetThisDomain-20201215T210541Z-10"
            }
        },
        "ResetThisDomain": {
            "status": "Action request accepted."
        }
    }
    connection = {}
    req_handler = DPActionQueueRequestHandler(connection)
    assert req_handler.is_completed(resp) == False
    resp = {
        "_links": {
            "self": {
                "href": "/mgmt/actionqueue/snafu"
            },
            "doc": {
                "href": "/mgmt/docs/actionqueue"
            }
        },
        "SaveConfig": "Operation completed.",
        "script-log": ""
    }
    assert req_handler.is_completed(resp) == True
    resp = {
        "_links": {
            "self": {
                "href": "/mgmt/actionqueue/snafu/pending/ResetThisDomain-20201215T212048Z-11"
            }
        },
        "status": "completed"
    }
    assert req_handler.is_completed(resp) == True
    resp = {
        "SaveConfig": "Operation completed.",
        "_links": {
            "doc": {
                "href": "/mgmt/docs/actionqueue"
            },
            "self": {
                "href": "/mgmt/actionqueue/snafu"
            }
        },
        "script-log": ""
    }
    assert req_handler.is_completed(resp) == True
    