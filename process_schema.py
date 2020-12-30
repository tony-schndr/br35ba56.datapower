#!/usr/bin/env python
import json

with open('all_dp_obj_schema.json') as f:
    data = json.loads(f.read())
    path = './collections/ansible_collections/community/datapower/tests/unit/module_utils/test_data/schema/'
    if 'results' in data: 
        for result in data['results']:
            if result['invocation']['module_args']['class_name'] == 'self':
                continue
            filename = result['invocation']['module_args']['class_name'] + '.json'
            data = result['result']
            with open(path + filename, 'w') as fp:
                json.dump(data, fp, indent=4)