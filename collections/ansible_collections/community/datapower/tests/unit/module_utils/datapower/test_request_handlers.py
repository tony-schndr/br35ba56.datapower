from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.dp_mgmt_conf import (
    DPManageConfigObject,
    DPManageConfigSchema,
    DPProperty
)
