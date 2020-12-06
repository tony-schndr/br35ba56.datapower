from __future__ import absolute_import, division, print_function

__metaclass__ = type

class DPConfigObject:
    # domain and class_name are the bare minimum required to get a valid
    # response from DataPower
    # kwargs consisting of the arguments defined in the Ansible Modules
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)
