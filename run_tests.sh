#!/bin/bash

rm -rf tests/output/
ansible-test units --python 3.7 --docker -v tests/unit/module_utils/datapower/
ansible-test network-integration
ansible-test sanity --test validate-modules config