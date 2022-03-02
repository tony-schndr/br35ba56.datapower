# Ansible Role - dp_certificate
=========

Create x509 Certificates on IBM DataPowers.

Requirements
------------

[Ansible Community DataPower Collection](https://github.com/tony-schndr/ansible-datapower)

Role Variables
--------------
```yaml
# Domain to create Crypto Certificate in
domain_name: "foo"
# The name of the certificate object.
cert_name: "datapowerguru.com"
# Local path to the certificate
cert_src: path/to/datapowerguru.com.pem
# Remote path to where the certificate should be uploaded to.
# For security reasons this should be in the /cert/ or /sharedcert/ directory.
cert_dest: "/cert/datapowerguru.com.pem"
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
