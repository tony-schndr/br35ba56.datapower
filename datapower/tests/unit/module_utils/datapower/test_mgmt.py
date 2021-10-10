from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re
import os

import pytest


from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    Config
)


def test_get_top_dir():
    pass


class TestConfig:

    def test_DPConfig__init__min_args_required(self):
        kwargs = {
            'domain': 'default',
            'class_name': 'CryptoValCred',
            'name': 'test',
            'config': None
        }

        dp_config = Config(**kwargs)
        assert dp_config

    def test_DPConfig__init__class_name_and_name_in_config(self):
        kwargs = {
            'domain': 'snafu',
            'config': {
                'CryptoValCred': {
                    'name': 'valcred'
                }
            }
        }

        dp_config = Config(**kwargs)
        assert dp_config.name == 'valcred'
        assert dp_config.class_name == 'CryptoValCred'

    def test_DPConfig__init__set_config(self):
        kwargs = {
            'domain': 'snafu',
            'class_name': 'CryptoValCred',
            'name': 'valcred',
            'config': {
                'Certificate': [
                    {'name': 'valcred'}
                ]
            }
        }

        dp_config = Config(**kwargs)
        assert dp_config.name == 'valcred'
        assert dp_config.class_name == 'CryptoValCred'
        assert dp_config.config == {
            'CryptoValCred': {
                'name': 'valcred',
                'Certificate': [
                        {
                            'name': 'valcred'
                        }
                ]
            }
        }

    def test_DPConfig_invalid_class(self):
        kwargs = {
            'domain': 'snafu',
            'config': {
                'ValidationCredential': {
                    'name': 'valcred'
                }
            }
        }
        try:
            Config(**kwargs)
        except ValueError:
            assert True

    def test_DPConfig__init__only_name_in_config(self):
        kwargs = {
            'domain': 'snafu',
            'class_name': 'Domain',
            'config': {
                'name': 'foo'
            }
        }

        dp_config = Config(**kwargs)
        assert dp_config.name == 'foo'
        assert dp_config.class_name == 'Domain'
