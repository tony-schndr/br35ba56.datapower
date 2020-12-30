from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Helper functions for comparing dictionairies.

# When using this to determine what will be changed on a DataPower the 
# from_dict should always be DataPower config, to_dict should always be ansible.
 
def get_duplicate_keys(from_dict, to_dict):
    common_keys = set()
    for k in from_dict.keys():
        if k in to_dict:
            common_keys.add(k)
    return common_keys

def get_diff_keys(from_dict, to_dict):
    diff_keys = set()
    for k,v in to_dict.items():
        if k in from_dict and k in to_dict:
            if v != from_dict[k]:
                diff_keys.add(k)
    return diff_keys


def get_change_dict(from_dict, to_dict, schema):
    pri_key = get_prim_key(from_dict, to_dict)
    change_dict = dict({'name': from_dict[pri_key]['name']})
    for to_key,to_val in to_dict[pri_key].items():
        if to_val is None:
            raise AttributeError(to_key + ' cannot be null')
        
    return {pri_key: change_dict}
    

def get_prim_key(from_dict, to_dict):
    if list(from_dict.keys())[0] == list(to_dict.keys())[0]:
        return list(from_dict.keys())[0]
    else:
        raise AttributeError('Cannot compare dictionaries without matching primary keys.')
     
    