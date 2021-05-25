
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import (
    ConnectionError,
) 

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    clean_dp_dict
)


def get_state(req):
    resp = dict()
    try:
        resp = req.get()
    except ConnectionError as e:
        err = to_text(e)
        if 'Resource not found' in err:        
            return None # Checked by dp_diff....
        else:
            raise e
    #Deletes keys we don't care about (_links, href, state) 
    clean_dp_dict(resp)
    return resp


def update_remote_state(obj, req, remote_state):
   #patched_body = dp_diff.get_patched_dict(remote_state, obj.config)
    req.set_body(obj.config)
    if remote_state == None:
        return req.create()
    else:
        return req.update()