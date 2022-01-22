# Ansible Role - dp_crypto_id_cred
=========

Create a Crypto Identity Credential on IBM DataPowers.

Requirements
------------

[Ansible Community DataPower Collection](https://github.com/tony-schndr/ansible-datapower)

Role Variables
--------------
```yaml
domain_name: datapower_domain_name
cert_path: path/to/certificate.pem
key_path: path/to/private_key.pem
crypto_id_cred_name: name_of_resource
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
    cert_path: "~/datapowerguru.com_cert.pem"
    key_path:  "~/datapowerguru.com_privkey.pem"
    crypto_id_cred_name: "datapowerguru_idcred"
```

License
-------

GNU GPLv3

Author Information
------------------

tonyschndr@gmail.com
