from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPManageConfigObject
)

from ansible_collections.community.datapower.tests.unit.module_utils.test_data import (
    dp_mgmt_test_data as test_data
)
# Tests building requests objects from the DPManageConfigObject.  Request objects are 
# passed to the request handlers



def test_DPManageConfigObject():
    task_args =  {
        "class_name": None,
        "config": {
            "CryptoValCred": {
                "mAdminState": "enabled",
                "name": "valcred"
            }
        },
        "domain": "default",
        "name": None,
        "overwrite": False
    }
    
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    assert dp_mgmt_conf.class_name == 'CryptoValCred'
    assert dp_mgmt_conf.name == 'valcred'
    assert dp_mgmt_conf.config == task_args['config']
    assert dp_mgmt_conf.domain == task_args['domain']
    assert dp_mgmt_conf.overwrite == task_args['overwrite']




    
            


