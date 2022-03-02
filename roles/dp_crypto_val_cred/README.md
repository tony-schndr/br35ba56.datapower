# Ansible Role - dp_crypto_val_cred
=========

Create a Crypto Validation Credential on IBM DataPowers.

Requirements
------------
Requires certificates uploaded to DataPower and associated objects created; recommend to use the roles `br35ba56.datapower.dp_certificate` role included within this collection.
[Ansible Community DataPower Collection](https://github.com/tony-schndr/ansible-datapower)

Role Variables
--------------
```yaml
# Domain to create Crypto Validation Credential in
domain_name: datapower_domain_name
# Name of the Crypto Validation Credential Object
val_cred_name: crypto_Validation_object_name
# List of certificates that are added to the Crypto Validation Credential, this list will be merged into the running configuration.
certificates:
  - value: 'cert_name_1'
# Validation mode, valid options are either pkix, legacy, exact-match
cert_validation_mode: legacy
# Select whether to check Certificate Revocation Lists (CRLs) during certificate validation.
use_crl: 'on'
# Select whether to mandate the use of Certificate Revocation Lists (CRLs) during certificate validation.
require_crl: 'off'
# Select how to support certificate extensions for X.509 Certificate Distribution Points.
crl_dp_handling: ignore
# Select whether to check the current date and time against the notBefore and the notAfter values in certificates and CRLs during certificate validation.
check_dates: 'on'
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
    domain_name: datapower_domain_name
    valcred_name: crypto_certificate_object_name
    certificates:
      - value: 'cert_name_1'
      - value: 'cert_name_2'
      - value: 'cert_name_3'
```

License
-------

GNU GPLv3

Author Information
------------------

tonyschndr@gmail.com
