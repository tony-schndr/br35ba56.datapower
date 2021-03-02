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



def test_DPManageConfigObject_int():
    task_args =  {
        "class_name": None,
        "config": {
            "CryptoValCred": {
                "mAdminState": "enabled",
                "name": "valcred",
                "port": 9090
            }
        },
        "domain": "default",
        "name": None,
        "overwrite": False
    }
    
    dp_mgmt_conf = DPManageConfigObject(**task_args)
    assert isinstance(dp_mgmt_conf.config['port'], int)






    
            


