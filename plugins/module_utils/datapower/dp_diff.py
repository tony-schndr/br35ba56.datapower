from __future__ import absolute_import, division, print_function

__metaclass__ = type

from dictdiffer import diff, patch
# Helper functions for comparing dictionaries.

# When using this to determine what will be changed on a DataPower the 
# from_dict should always be DataPower config, to_dict should always be ansible.


def get_patched_dict(from_dict, to_dict):
    result = diff(from_dict, to_dict)
    return patch(result, from_dict)


def is_changed(from_dict, to_dict):
    return len(
        get_change_list(from_dict, to_dict)
    ) > 0


def get_change_list(from_dict, to_dict):
    return list(get_changes(from_dict, to_dict))


# Returns an iterator of dictionaries based off dictdiffer.diff
def get_changes(from_dict, to_dict):
    for diff_ in diff(from_dict, to_dict):
        # DataPower REST MGMT interface does not care if a parameter is present
        # if a parameter is not present it will remain unchanged on DataPower
        # therefore we do not consider it when yielding diffs
        if diff_[0] == 'remove':
            continue
        elif diff_[0] == 'change':
            if check_if_dict_to_list_compare(diff_):
                if check_if_dict_and_list_are_equal(diff_):
                    continue
                else:
                    yield _change_dict(diff_) 
            elif check_if_str_to_int_compare(diff_):
                if check_if_str_and_int_equal(diff_):
                    continue
                else:
                    yield _change_dict(diff_)
            else:
                yield _change_dict(diff_)
        elif diff_[0] == 'add':
            yield _change_dict(diff_)
        else:
            raise NotImplementedError('Only remove, change, and add are supported diff checks.')
        
        
def _change_dict(diff_):

    if diff_[0] == 'add':
        return {
            'path' : diff_[1],
            'diff': {
                'from' : 'not defined',
                'to' : diff_[2][0]
            }
        }

    return {
        'path' : diff_[1],
        'diff': {
            'from' : diff_[2][0],
            'to' : diff_[2][1]
        }
    }

'''
Ansible Jinja2 template expressions "{{ int_type_var }}" always return strings to the ansible modules. 
This causes false positive changes when comparing strings (from ansible) to integers (from datapower).
'''
def check_if_str_to_int_compare(diff_):
    return isinstance(diff_[2][0], int) and isinstance(diff_[2][1], str)


def check_if_str_and_int_equal(diff_):
    return str(diff_[2][0]) == str(diff_[2][1])


'''
If a DataPower field is of type list and only contains 1 item DataPower 
returns that item in a dictionary.  The DataPower Mgmt REST interface will
allow the user to pass the values in as a list with 1 item or a dictionary.
To prevent false positive changes because the dict / list are not equal 
(BUT contain the same values) we first check if we have met the condition,
then compare the values.

For example:

"Certificate": [
    {
        "value": "Test1"
    }
]

is equivalent to:

"Certificate": {
    "value": "Test1"
}
'''
def check_if_dict_to_list_compare(diff_):
    return isinstance(diff_[2][0], dict) and isinstance(diff_[2][1], list) and len(diff_[2][1]) == 1


def check_if_dict_and_list_are_equal(diff_):
    if len(diff_[2][1]) == 1:
        return diff_[2][0] == diff_[2][1][0]
    else:
        raise TypeError('cannot compare single element to a list other than len(<list>) == 1')
