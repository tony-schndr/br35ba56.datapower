#!/bin/bash

ansible-test sanity --test validate-modules config
ansible-test sanity --test validate-modules files
ansible-test sanity --test validate-modules get_config
ansible-test sanity --test validate-modules list_objects
ansible-test sanity --test validate-modules action
ansible-test sanity --test validate-modules list_actions
ansible-test sanity --test validate-modules get_action_schema
ansible-test sanity --test validate-modules export_objects
ansible-test sanity --test validate-modules export_domains
ansible-test sanity --test validate-modules import_domains
ansible-test sanity --test validate-modules load_objects
ansible-test sanity --test validate-modules status
ansible-test sanity --test validate-modules list_status