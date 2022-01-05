[![CI](https://github.com/Br35Ba56/datapower-crypto-id-cred/actions/workflows/ci.yml/badge.svg)](https://github.com/Br35Ba56/datapower-crypto-id-cred/actions/workflows/ci.yml)

# Ansible Role - datapower_crypto_id_cred
=========

Create a Crypto Identity Credential on IBM DataPowers.

Requirements
------------

[Ansible Community DataPower Collection](https://github.com/Br35Ba56/ansible-datapower)

Role Variables
--------------
```yaml
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
    name: br35ba56.datapower_crypto_id_cred
  vars:
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
