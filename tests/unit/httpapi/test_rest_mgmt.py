from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import pytest
import json
from collections import OrderedDict

from ansible_collections.community.datapower.plugins.httpapi.rest_mgmt import (
    is_action_completed,
    reorder_name_key
)


def validate_data_name_key_is_first(data):
    '''
    Recursively traverse a dictionary and validate the key 'name' is the first key in each dictionary
    '''

    if 'name' in data:
        assert next(iter(data)) == 'name'

    for k, v in data.items():
        if isinstance(v, dict):
            validate_data_name_key_is_first(v)
        elif isinstance(v, list):
            for elem in v:
                if isinstance(elem, dict):
                    validate_data_name_key_is_first(elem)


def test_validate_data_name_key_is_first():
    pass


def test_reorder_name_key_export_with_one_domain_element():
    data = {"Export": {
        "Domain": [
            {"include-debug": None, "name": "all-domains",
                "ref-files": True, "ref-objects": False}
        ], "Format": "ZIP", "IncludeInternalFiles": "on", "ref-files": "on"}}

    modified_data = reorder_name_key(data)
    validate_data_name_key_is_first(modified_data)


def test_reorder_name_key_export_with_multiple_domain_elements():
    data = {"Export": {"Domain": [
        {"include-debug": None, "name": "foo", "ref-files": True, "ref-objects": False},
        {"include-debug": None, "name": "bar", "ref-files": True, "ref-objects": False},
        {"include-debug": None, "name": "snafu", "ref-files": True, "ref-objects": False}],
        "Format": "ZIP", "IncludeInternalFiles": "on", "ref-files": "on"}}

    modified_data = reorder_name_key(data)
    validate_data_name_key_is_first(modified_data)


def test_action_is_action_completed():
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
    assert not is_action_completed(resp)
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
    assert is_action_completed(resp)
    resp = {
        "_links": {
            "self": {
                "href": "/mgmt/actionqueue/snafu/pending/ResetThisDomain-20201215T212048Z-11"
            }
        },
        "status": "completed"
    }
    assert is_action_completed(resp)
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
    assert is_action_completed(resp)
