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
        if to_key in from_dict[pri_key]:
            if type(to_val) == type(from_dict[pri_key][to_key]) and isinstance(to_val, list):
                try:
                    if sorted(to_val, key = lambda i: i['value']) != sorted(from_dict[pri_key][to_key],  key = lambda i: i['value']):
                        change_dict[to_key] = to_val
                except KeyError:
                    raise AttributeError('Did you mean "value"')
            elif type(to_val) == type(from_dict[pri_key][to_key]):
                if to_val != from_dict[pri_key][to_key]:
                    change_dict[to_key] = to_val
            else:
                prop = schema.get_prop(to_key)
                if hasattr(prop, 'array') and prop.array:
                    
                    if len(to_val) == 1:
                        if 'value' not in to_val[0]:
                            raise AttributeError('Did you mean "value"')
                        if to_val[0] != from_dict[pri_key][to_key]:
                            change_dict[to_key] = to_val
                    else:
                        for i in to_val:
                            if 'value' not in i:
                                raise AttributeError('Did you mean "value"')
                        change_dict[to_key] = to_val
                    
        else:#Should check the schema to ensure it is a valid option
            prop = schema.get_prop(to_key)
            if hasattr(prop, 'array') and prop.array:
                for i in to_val:
                    if 'value' not in i:
                        raise AttributeError('Did you mean "value"')
                change_dict[to_key] = to_val
            else:
                raise AttributeError('Invalid key passed to DataPower config object.')

    return {pri_key: change_dict}
    

def get_prim_key(from_dict, to_dict):
    if list(from_dict.keys())[0] == list(to_dict.keys())[0]:
        return list(from_dict.keys())[0]
    else:
        raise AttributeError('Cannot compare dictionaries without matching primary keys.')
     
   