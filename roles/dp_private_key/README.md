# Ansible Role - dp_private_key
=========

Create a RSA Private Key on IBM DataPowers.

Requirements
------------

[Ansible Community DataPower Collection](https://github.com/tony-schndr/ansible-datapower)

Role Variables
--------------
```yaml
domain_name: datapower_domain_name
key_path: path/to/private_key.pem
password: "$ecureP@$$word"
password_alias_name: "priv_key_pw_alias"
```

Dependencies
------------
None

Example Playbook
----------------
```yaml
- name: Execute role
  include_role:
    name: dp_private_key
  vars:
    domain_name: "foo"
    key_path:  "~/datapowerguru.com_privkey.pem"
    password: "$ecureP@$$word"
    password_alias_name: "priv_key_pw_alias"
```

License
-------

GNU GPLv3

Author Information
------------------

tonyschndr@gmail.com
