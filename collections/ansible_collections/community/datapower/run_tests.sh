#!/bin/bash


rm -rf tests/output/
ansible-test units --python 3.6 --docker -v tests/unit/module_utils/datapower/*