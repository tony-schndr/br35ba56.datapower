#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The datapower domain fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
import re
from copy import deepcopy
from ansible.module_utils.connection import exec_command

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.community.datapower.plugins.module_utils.network.datapower.argspec.domain.domain import DomainArgs


class DomainFacts(object):
    """ The datapower domain fact class
    """

    def __init__(self, module, subspec='config', options='options'):
        raise Exception()
        self._module = module
        self.argument_spec = DomainArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)


    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for domain
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """

        if not data:
            # data is populated from the current device configuration
            data = connection.get_config('default', 'Domain')


        # split the config into instances of the resource
        objs = []

        if isinstance(data['Domain'], list):
            for resource in data['Domain']:
                if resource['name'] != 'default':
                    objs.append(resource)
        else:
            if data['Domain']['name'] != 'default':
                objs.append(data['Domain'])

        for obj in objs:
            clean_dp_dict(obj)


        ansible_facts['ansible_network_resources'].pop('domain', None)

        facts = {}

        if objs:
            params = utils.validate_config(self.argument_spec, {'config': objs})
            facts['domain'] = params['config']

        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts



def _scrub(obj, bad_key):
    """
    Removes specified key from the dictionary in place.
    :param obj: dict, dictionary from DataPowers get object config rest call
    :param bad_key: str, key to remove from the dictionary
    """
    if isinstance(obj, dict):
        for key in list(obj.keys()):
            if key == bad_key:
                del obj[key]
            else:
                _scrub(obj[key], bad_key)
    elif isinstance(obj, list):
        for i in reversed(range(len(obj))):
            if obj[i] == bad_key:
                del obj[i]
            else:
                _scrub(obj[i], bad_key)
    else:
        # neither a dict nor a list, do nothing
        pass


def clean_dp_dict(dict_):
    _scrub(dict_, '_links')
    _scrub(dict_, 'href')
    _scrub(dict_, 'state')