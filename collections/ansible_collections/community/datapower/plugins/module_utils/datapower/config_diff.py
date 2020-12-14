from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Helper functions for comparing dictionairies.

# When using this to determine what will be changed on a DataPower the 
# from dict should always be DataPower config, to dict should always be ansible.  
 
def get_duplicate_keys(from_dict, to_dict):
    common_keys = set()
    for k in from_dict.keys():
        if k in to_dict:
            common_keys.add(k)
    return common_keys

def get_diff_keys(from_dict, to_dict):
    from_set = set(from_dict.items())
    to_set = set(to_dict.items())
    diff_keys = set()
    for item in from_set ^ to_set:
        diff_keys.add(item[0])
    return diff_keys


def dict_diff(from_dict, to_dict):
    diff_ = dict()
    # sort lists for compare later
    for k in get_duplicate_keys(to_dict, from_dict):
        if isinstance(from_dict[k], list):
            from_dict[k] = sorted(from_dict[k], key = lambda i: i['value'])
            to_dict[k] = sorted(to_dict[k], key = lambda i: i['value'])
    for k in get_diff_keys(to_dict, from_dict):
        diff_[k] = {'from' : from_dict[k], 'to' : to_dict[k]}
    return diff_

def matching_prim_keys(from_dict, to_dict):
    return list(from_dict.keys())[0] == list(to_dict.keys())[0]
   