# Ansible Role - dp_crypto_id_cred
=========

Create a Crypto Identity Credential on IBM DataPowers.

Requirements
------------
Requires certificate and key pair files uploaded to DataPower and associated objects created; recommend to use the roles `br35ba56.datapower.dp_certificate` and `br35ba56.datapower.dp_private_key` roles included within this collection.
[Ansible Community DataPower Collection](https://github.com/tony-schndr/ansible-datapower)

Role Variables
--------------
```yaml
domain_name: datapower_domain_name
cert_name: crypto_certificate_object_name
key_name: crypto_key_object_name
crypto_id_cred_name: crypto_id_cred_name
```

Dependencies
------------
None

Example Playbook
----------------
```yaml
- name: Execute role
  include_role:
    name: dp_crypto_id_cred
  vars:
    domain_name: "foo"
    cert_name: "datapowerguru.com_cert"
    key_name:  "datapowerguru.com_privkey"
    crypto_id_cred_name: "datapowerguru_idcred"
```

License
-------

GNU GPLv3

Author Information
------------------

tonyschndr@gmail.com
