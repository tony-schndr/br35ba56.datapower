from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import os

import pytest
from faker.factory import Factory


from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.mgmt import (
    normalize_config_data
)
from ansible_collections.br35ba56.datapower.plugins.module_utils.datapower.mgmt import file_diff


def get_multiline_str():
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


# def test_get_files_from_filestore_single_file():
#     filestore_resp = {
#         "_links": {
#             "self": {
#                 "href": "/mgmt/filestore/default/local"
#             },
#             "doc": {
#                 "href": "/mgmt/docs/filestore"
#             }
#         },
#         "filestore": {
#             "location": {
#                 "name": "local:",
#                 "file": {
#                     "name": "demo.txt",
#                     "size": 12,
#                     "modified": "2021-07-13 13:07:41",
#                     "href": "/mgmt/filestore/default/local/demo.txt"
#                 },
#                 "directory": [
#                     {
#                         "name": "local:/snafu",
#                         "href": "/mgmt/filestore/default/local/snafu"
#                     },
#                     {
#                         "name": "local:/subdir",
#                         "href": "/mgmt/filestore/default/local/subdir"
#                     },
#                     {
#                         "name": "local:/foo",
#                         "href": "/mgmt/filestore/default/local/foo"
#                     },
#                     {
#                         "name": "local:/local",
#                         "href": "/mgmt/filestore/default/local/local"
#                     }
#                 ],
#                 "href": "/mgmt/filestore/default/local"
#             }
#         }
#     }

#     files_from_filestore = files.get_files_from_filestore(filestore_resp)
#     assert files_from_filestore == ['/mgmt/filestore/default/local/demo.txt']


# def test_get_files_from_filestore_multiple_files():
#     filestore_resp = {
#         "_links": {
#             "self": {
#                 "href": "/mgmt/filestore/default/local"
#             },
#             "doc": {
#                 "href": "/mgmt/docs/filestore"
#             }
#         },
#         "filestore": {
#             "location": {
#                 "name": "local:",
#                 "file": [
#                     {
#                         "name": "demo.txt",
#                         "size": 12,
#                         "modified": "2021-07-13 13:07:41",
#                         "href": "/mgmt/filestore/default/local/demo.txt"
#                     },
#                     {
#                         "name": "demo2.txt",
#                         "size": 12,
#                         "modified": "2021-07-13 13:07:41",
#                         "href": "/mgmt/filestore/default/local/demo2.txt"
#                     },
#                     {
#                         "name": "demo3.txt",
#                         "size": 12,
#                         "modified": "2021-07-13 13:07:41",
#                         "href": "/mgmt/filestore/default/local/demo3.txt"
#                     }
#                 ],
#                 "directory": [
#                     {
#                         "name": "local:/snafu",
#                         "href": "/mgmt/filestore/default/local/snafu"
#                     },
#                     {
#                         "name": "local:/subdir",
#                         "href": "/mgmt/filestore/default/local/subdir"
#                     },
#                     {
#                         "name": "local:/foo",
#                         "href": "/mgmt/filestore/default/local/foo"
#                     },
#                     {
#                         "name": "local:/local",
#                         "href": "/mgmt/filestore/default/local/local"
#                     }
#                 ],
#                 "href": "/mgmt/filestore/default/local"
#             }
#         }
#     }

#     files_from_filestore = files.get_files_from_filestore(filestore_resp)
#     assert files_from_filestore == [
#         '/mgmt/filestore/default/local/demo.txt',
#         '/mgmt/filestore/default/local/demo2.txt',
#         '/mgmt/filestore/default/local/demo3.txt',
#     ]


# def test_get_parent_dir():
#     path = '/some/test/path/file.txt'
#     assert files.get_parent_dir(path) == '/some/test/path'
