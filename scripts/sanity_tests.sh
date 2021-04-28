#!/bin/bash

ansible-test sanity --test validate-modules config
#ansible-test sanity --test validate-modules files
ansible-test sanity --test validate-modules get_config
ansible-test sanity --test validate-modules list_objects
ansible-test sanity --test validate-modules action
ansible-test sanity --test validate-modules list_actions
ansible-test sanity --test validate-modules get_action_schema