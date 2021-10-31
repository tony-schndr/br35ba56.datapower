from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import os

import pytest

from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    normalize_config_data
)


raw_out_list = {
    "_links": {
        "self": {
            "href": "/mgmt/config/default/CryptoCertificate"
        },
        "doc": {
            "href": "/mgmt/docs/config/CryptoCertificate"
        }
    },
    "CryptoCertificate": [
        {
            "name": "ansible",
            "_links": {
                "self": {
                    "href": "/mgmt/config/default/CryptoCertificate/ansible"
                },
                "doc": {
                    "href": "/mgmt/docs/config/CryptoCertificate"
                }
            },
            "mAdminState": "enabled",
            "Filename": "cert:///ansible-sscert.pem",
            "PasswordAlias": "off",
            "IgnoreExpiration": "off"
        },
        {
            "name": "boo",
            "_links": {
                "self": {
                    "href": "/mgmt/config/default/CryptoCertificate/boo"
                },
                "doc": {
                    "href": "/mgmt/docs/config/CryptoCertificate"
                }
            },
            "mAdminState": "enabled",
            "Filename": "cert:///datapowerguru.com_exp_20311021015228Z.pem",
            "PasswordAlias": "off",
            "IgnoreExpiration": "off"
        },
        {
            "name": "datapowerguru.com_exp_20311021015228Z",
            "_links": {
                "self": {
                    "href": "/mgmt/config/default/CryptoCertificate/datapowerguru.com_exp_20311021015228Z"
                },
                "doc": {
                    "href": "/mgmt/docs/config/CryptoCertificate"
                }
            },
            "mAdminState": "enabled",
            "Filename": "cert:///datapowerguru.com_exp_20311021015228Z.pem",
            "PasswordAlias": "off",
            "IgnoreExpiration": "off"
        },
        {
            "name": "test",
            "_links": {
                "self": {
                    "href": "/mgmt/config/default/CryptoCertificate/test"
                },
                "doc": {
                    "href": "/mgmt/docs/config/CryptoCertificate"
                }
            },
            "mAdminState": "enabled",
            "Filename": "cert:///webgui-sscert.pem",
            "PasswordAlias": "off",
            "IgnoreExpiration": "off"
        }
    ]
}


raw_out_dict = {
    "_links": {
        "self": {
            "href": "/mgmt/config/default/CryptoCertificate"
        },
        "doc": {
            "href": "/mgmt/docs/config/CryptoCertificate"
        }
    },
    "CryptoCertificate": {
        "name": "ansible",
        "_links": {
            "self": {
                "href": "/mgmt/config/default/CryptoCertificate/ansible"
            },
            "doc": {
                "href": "/mgmt/docs/config/CryptoCertificate"
            }
        },
        "mAdminState": "enabled",
        "Filename": "cert:///ansible-sscert.pem",
        "PasswordAlias": "off",
        "IgnoreExpiration": "off"
    }
}


raw_out_no_config_retreived = {
    "_links": {
        "self": {
            "href": "/mgmt/config/snafu/CryptoCertificate"
        },
        "doc": {
            "href": "/mgmt/docs/config/CryptoCertificate"
        }
    },
    "result": "No configuration retrieved."
}


def test_normalize_config_data_list():
    assert normalize_config_data(raw_out_list) == [
        {
            'CryptoCertificate': {
                'name': 'ansible',
                'mAdminState': 'enabled',
                'Filename': 'cert:///ansible-sscert.pem',
                'PasswordAlias': 'off',
                'IgnoreExpiration': 'off'
            }
        },
        {
            'CryptoCertificate': {
                'name': 'boo',
                'mAdminState': 'enabled',
                'Filename': 'cert:///datapowerguru.com_exp_20311021015228Z.pem',
                'PasswordAlias': 'off',
                'IgnoreExpiration': 'off'
            }
        },
        {
            'CryptoCertificate': {
                'name': 'datapowerguru.com_exp_20311021015228Z',
                'mAdminState': 'enabled',
                'Filename': 'cert:///datapowerguru.com_exp_20311021015228Z.pem',
                'PasswordAlias': 'off',
                'IgnoreExpiration': 'off'}
        },
        {
            'CryptoCertificate': {
                'name': 'test',
                'mAdminState': 'enabled',
                'Filename': 'cert:///webgui-sscert.pem',
                'PasswordAlias': 'off',
                'IgnoreExpiration': 'off'
            }
        }
    ]


def test_normalize_config_data_dict():
    assert normalize_config_data(raw_out_dict) == [{"CryptoCertificate": {
        "name": "ansible", "mAdminState": "enabled", "Filename": "cert:///ansible-sscert.pem", "PasswordAlias": "off", "IgnoreExpiration": "off"}}]


def test_normalize_config_data_no_config_retrieved():
    assert normalize_config_data(raw_out_no_config_retreived) is None
