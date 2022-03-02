# Ansible Role - dp_private_key
=========

Create x509 Certificates on IBM DataPowers.

Requirements
------------

[Ansible Community DataPower Collection](https://github.com/tony-schndr/ansible-datapower)

Role Variables
--------------
```yaml
domain_name: "foo"
cert_src: path/to/datapowerguru.com.pem
cert_dest: "/cert/datapowerguru.com.pem"
cert_name: "datapowerguru.com"
```

Dependencies
------------
None

Example Playbook
----------------
```yaml
- name: Execute role
  include_role:
    name: dp_certificate
  vars:
    domain_name: "foo"
    cert_src: path/to/datapowerguru.com.pem
    cert_dest: "/cert/datapowerguru.com.pem"
    cert_name: "datapowerguru.com"
```

License
-------

GNU GPLv3

Author Information
------------------

tonyschndr@gmail.com
