#!/bin/bash


rm -rf tests/output/
ansible-test units --python 3.7 --docker -v tests/unit/module_utils/datapower/test_dp_diff.py
#ansible-test units --python 3.7 --venv -v tests/unit/module_utils/datapower/ 