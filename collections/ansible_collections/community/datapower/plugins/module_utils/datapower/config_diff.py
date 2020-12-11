from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Helper functions for comparing dictionairies.

# When using this to determine what will be changed on a DataPower the 
# from dict should always be DataPower config, to dict should always be ansible.  
 
def get_duplicate_keys(from_dict, to_dict):
    return to_dict.keys() & from_dict.keys()

def get_diff_keys(from_dict, to_dict):
    return { key for key in to_dict.keys() & from_dict if to_dict[key] != from_dict[key] }

def dict_diff(from_dict, to_dict):
    diff_ = dict()
    # sort lists for compare later
    for k in get_duplicate_keys(to_dict, from_dict):
        if isinstance(from_dict[k], list):
            print(k)
            from_dict[k] = sorted(from_dict[k], key = lambda i: i['value'])
            to_dict[k] = sorted(to_dict[k], key = lambda i: i['value'])
    for k in get_diff_keys(to_dict, from_dict):
        diff_[k] = {'from' : from_dict[k], 'to' : to_dict[k]}
    return diff_

def matching_prim_keys(from_dict, to_dict):
    return list(from_dict.keys())[0] == list(to_dict.keys())[0]
   