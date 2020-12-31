#!/bin/bash


rm -rf tests/output/
ansible-test units --python 3.7 --docker -v tests/unit/module_utils/datapower/
#ansible-test units --python 3.7 --venv -v tests/unit/module_utils/datapower/ 