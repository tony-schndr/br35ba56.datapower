# Ansible Role - dp_private_key
=========

Create a RSA Private Key on IBM DataPowers.

Requirements
------------

[Ansible Community DataPower Collection](https://github.com/tony-schndr/ansible-datapower)

Role Variables
--------------
```yaml
# Domain to upload / create private key (Crypto Key) object in
domain_name: datapower_domain_name
# Local path to the private key
key_src: path/to/private_key.pem
# Remote path to where the private key should be uploaded to
# For security reasons this should be in the /cert/ or /sharedcert/ directory
key_dest: /cert/private_key.pem
# The name of the Password Map Alias, this is needed if the private key is password protected.
password_alias_name: "priv_key_pw_alias"
# Password for decrypting the private key, this will be applied to the Password Map Alais object.
password: "$ecureP@$$word"
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
    key_src:  "~/datapowerguru.com_privkey.pem"
    key_dest:  "/cert/datapowerguru.com_privkey.pem"
    password: "$ecureP@$$word"
    password_alias_name: "priv_key_pw_alias"
```

License
-------

GNU GPLv3

Author Information
------------------

tonyschndr@gmail.com
