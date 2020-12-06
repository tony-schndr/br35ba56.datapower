from __future__ import absolute_import, division, print_function
__metaclass__ = type

import ssl
import sys


from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    DPGetConfigRequest
)

def test_always_passes():
    assert True