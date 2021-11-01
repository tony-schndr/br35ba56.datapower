#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: x509_certificate

short_description: Manage x509 Certificates on DataPower.

version_added: "1.0.0"

description: |
    Manage x509 Certificates on DataPower.
    This will not overwrite a certificate/key file if it exists.  Best practice
    would be to create a new cert / key and disable the old.  Remove
    the old crypto object once certain its not needed.
    The only way to restore cert/key on datapower is through a secure restore.

options:
    domain:
        description: Domain to create crypto in.
        required: true
        type: str
    obj_name:
        description: |
            Name of the certificate object that will be configured on DataPower.
            If obj_name is not specified it will auto generate a file name using the subjects common name and not after date as ASN.1 TIME.
            For example datapowerguru.com_exp_20311021015228Z
        required: false
        type: str
    file_name:
        description:
            - Name of the certificate that is uploaded to cert or sharedcert.
            - If file_name is not specified it will auto generate a file name using the subjects common name and not after date as ASN.1 TIME.
            - For example datapowerguru.com_exp_20311021015228Z.pem
        required: false
        type: str
    src:
        description: Path to the pem formatted x509 certificate.
        required: true
        type: path
    cert_dir:
        description:
            - The directory to upload the certificate too.
            - Certificate files uploaded to "cert" will only be visible to the application domain.
            - Certificate files uploaded to "sharedcert" is visible to all domains.
        required: false
        type: str
        choices:
          - cert
          - sharedcert
        default: cert
    content:
        description:
            - Content of the X.509 certificate in PEM format.
            - Either I(path) or I(content) must be specified, but not both.
        type: str
    select_crypto_backend:
        description:
            - Determines which crypto backend to use.
            - The default choice is C(auto), which tries to use C(cryptography) if available.
            - If set to C(cryptography), will try to use the L(cryptography,https://cryptography.io/) library.
        type: str
        default: auto
        choices: [ auto, cryptography ]
    state:
        description: Apply the desired state if present, remove the CryptoObject and underlying file if absent.
        required: false
        type: str
        choices:
          - present
          - absent
        default: present

notes:
    - All timestamp values are provided in ASN.1 TIME format, in other words, following the C(YYYYMMDDHHMMSSZ) pattern.
      They are all in UTC.
author:
- Anthony Schneider (@br35ba56)
'''

# Create a valcred in {{ domain }}.  With this example the class_name CryptoValCred and
# name "valcred" are in the body of the request.
EXAMPLES = r'''
---
- name: cert details
  community.datapower.crypto:
    domain: foo
    state: certificate
    src: /local/path/to/cert.pem"
'''

RETURN = r'''
response:
    description: The response returned from DataPowers Rest MGMT Interface.
    type: dict
    returned: on success
    sample: {}
'''
import base64

# from ansible.module_utils._text import to_text
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
from ansible_collections.community.crypto.plugins.module_utils.crypto.basic import (
    OpenSSLObjectError,
)
from ansible_collections.community.crypto.plugins.module_utils.crypto.module_backends.certificate_info import (
    select_backend,
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.crypto import (
    process_crypto_module
)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            domain=dict(type='str', required=True),
            cert_dir=dict(type='str', choices=['cert', 'sharedcert'], default='cert'),
            content=dict(type='str'),
            file_name=dict(type='str', required=False),
            obj_name=dict(type='str', required=False),
            src=dict(type='path', required=True),
            state=dict(type='str', choices=['present', 'absent'], default='present'),
            select_crypto_backend=dict(type='str', default='auto', choices=['auto', 'cryptography']),
        ),
        required_one_of=(
            ['src', 'content'],
        ),
        mutually_exclusive=(
            ['src', 'content'],
        ),
        supports_check_mode=True,
    )

    result = {}

    if module.params['content'] is not None:
        data = module.params['content'].encode('utf-8')
    else:
        try:
            with open(module.params['src'], 'rb') as f:
                data = f.read()
        except (IOError, OSError) as e:
            module.fail_json(msg='Error while reading certificate file from disk: {0}'.format(e))

    backend, module_backend = select_backend(module, module.params['select_crypto_backend'], data)

    try:
        local_cert_info = module_backend.get_info()
    except OpenSSLObjectError as exc:
        module.fail_json(msg=to_native(exc))
    result['local_cert_info'] = local_cert_info
    crypto_result = process_crypto_module(module, local_cert_info, data)
    if crypto_result['config']['changed'] or crypto_result['file']['changed']:
        result['changed'] = True
    result.update(crypto_result)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
