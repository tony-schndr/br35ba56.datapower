from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import os

import pytest
from faker.factory import Factory
from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.utils import (
    normalize_config_data,
    file_diff
)
from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueRequest
)
from ansible.module_utils.common.dict_transformations import (
    recursive_diff
)


def test_dict_diff_with_no_diff():
    to_dict = {
        'string': 'bar',
        'number': 4,
        'dict': {
            'a': 'z',
            'b': 'y'
        },
        'foo_list': [
            1,
            2,
            3,
            4
        ]
    }
    from_dict = {
        'string': 'bar',
        'number': 4,
        'dict': {
            'a': 'z',
            'b': 'y'
        },
        'foo_list': [
            1,
            2,
            3,
            4
        ]
    }
    assert recursive_diff(to_dict, from_dict) is None


def test_dict_diff_with_diff():
    from_dict = {
        'string': 'foo',
        'number': 4,
        'dict': {
            'a': 'z',
            'c': 'x'
        },
        'foo_list': [
            1,
            2,
        ]
    }
    to_dict = {
        'string': 'bar',
        'number': '4',
        'dict': {
            'a': 'z',
            'b': 'y'
        },
        'foo_list': [
            1,
            2,
            3,
            4
        ]
    }
    assert recursive_diff(from_dict, to_dict) == ({'string': 'foo', 'dict': {'c': 'x'}, 'foo_list': [
        1, 2], 'number': 4}, {'string': 'bar', 'dict': {'b': 'y'}, 'foo_list': [1, 2, 3, 4], 'number': '4'})


def test_diff_between_dict_and_list():
    from_dict = {
        'CryptoValCred': {
            'name': 'PKIX-CertAuthorityRootCA_ValCred',
            'mAdminState': 'enabled',
            'Certificate': {'value': 'cert_1'},
            'CertValidationMode': 'pkix',
            'UseCRL': 'on',
            'RequireCRL': 'off',
            'CRLDPHandling': 'ignore',
            'InitialPolicySet': '2.5.29.32.0',
            'ExplicitPolicy': 'off',
            'CheckDates': 'on'
        }
    }
    to_dict = {
        'CryptoValCred': {
            'CRLDPHandling': 'ignore',
            'CertValidationMode': 'pkix',
            'Certificate': [
                {'value': 'cert_1'},
                {'value': 'cert_2'},
                {'value': 'cert_3'}
            ],
            'CheckDates': 'on',
            'ExplicitPolicy': 'off',
            'InitialPolicySet': '2.5.29.32.0',
            'RequireCRL': 'off',
            'UseCRL': 'on',
            'mAdminState': 'enabled',
            'name': 'PKIX-CertAuthorityRootCA_ValCred'
        }
    }
    diff = recursive_diff(from_dict, to_dict)
    assert diff == ({'CryptoValCred': {'Certificate': {'value': 'cert_1'}}}, {'CryptoValCred': {
                    'Certificate': [{'value': 'cert_1'}, {'value': 'cert_2'}, {'value': 'cert_3'}]}})


def get_multiline_str():
    '''
    Helper function to create a multiline string for testing.
    '''
    Faker = Factory.create
    fake = Faker()
    s = ''
    for i in range(5):
        s += fake.paragraph(nb_sentences=1, variable_nb_sentences=False) + '\n'
    return s.encode('utf-8')


def test_get_file_diff_when_from_and_to_are_equal():
    from_data = get_multiline_str()
    assert file_diff(
        from_data,
        from_data,
        '/some/other/path/file.txt',
    ) == []


def test_get_file_diff_when_from_and_to_are_different():
    from_data = get_multiline_str()
    to_data = get_multiline_str()

    assert file_diff(
        from_data,
        to_data,
        '/some/other/path/file.txt',
    )[0:2] == ['*** before: /some/other/path/file.txt\n', '--- after: /some/other/path/file.txt\n']


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
