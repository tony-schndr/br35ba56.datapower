#!/usr/bin/env python

import filestore
from filestore import DPFileStore
params = {
    'domain': 'default',
    'content': None,
    'src' : '/Users/anthonyschneider/DEV/ansible-datapower/collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/copy/recurse_test/local/GetStat',
    'dest' : '/local/GetStat',
    'overwrite' : True,
    'state' : 'directory'
}
filestore = DPFileStore(params)

for f in filestore.files():
    print(f)
