from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.actionqueue import (
    DPActionQueue
)

def test_DPActionQueue():
    task_args =  {
        "domain": "default",
        "action": "SaveConfig"
    }
    
    dp_action = DPActionQueue(**task_args)
    assert dp_action.action == 'SaveConfig'
    assert dp_action.domain == 'default'
