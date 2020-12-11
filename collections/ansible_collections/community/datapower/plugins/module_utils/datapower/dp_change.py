from __future__ import absolute_import, division, print_function

__metaclass__ = type

#from urllib.parse import quote

import time
from ansible.module_utils._text import to_text
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_text
from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    config_diff,
    dp_mgmt_conf
)
#import config_diff
class DPChange():

    def __init__(self, current_state, proposed_state):
        pass

    @staticmethod
    def state_diff(current_state, proposed_state):
        if config_diff.matching_prim_keys(current_state, proposed_state) and dp_mgmt_conf.is_valid_class(list(current_state.keys())[0]):
            root_key = list(current_state.keys())[0]
            compared_state = {root_key : {}}
            diff_dict = config_diff.dict_diff(current_state[root_key], proposed_state[root_key])
            for k, v in diff_dict.items():
                compared_state[root_key][k] = v
            compared_state[root_key]['name'] = current_state[root_key]['name']
            return compared_state
        else:
            raise TypeError('cannot compare, dictionary types do not match.')