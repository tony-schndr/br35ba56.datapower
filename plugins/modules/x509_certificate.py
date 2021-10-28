#!/usr/bin/python

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: crypto

short_description: Manage Crypto objects in DataPower Application Domains.

version_added: "1.0.0"

description: Manage Crypto objects in DataPower Application Domains.
    This will not overwrite a certificate/key if it exists.  Best practice
    would be to create a new cert / key and disable the old.  Remove
    the old crypto object once certain its not needed.
    The only way to restore cert/key on datapower is through a secure restore.

options:
    domain:
        description: Domain to create crypto in.
        required: true
        type: str
    path:
        description: Path to the cert/key file on local host
        required: true
        type: path
    name:
        description: name of Crypto Object
        required: true
        type: str
    password:
        description: password for decrypting keys
        required: false
        type: str
    state:
        description: Create a certificate, private_key, or absent
        required: true
        type: str
        choices:
          - certificate
          - private_key
          - absent

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
    name: pub_cert_one
    path: /path/to/local/cert.pem"
'''

RETURN = r'''
response:
    description: The response returned from DataPowers Rest MGMT Interface.
    type: dict
    returned: on success
    sample: {}
'''
import base64

from ansible.module_utils._text import to_text
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.connection import (
    ConnectionError,
    Connection
)

from ansible_collections.community.crypto.plugins.module_utils.crypto.basic import (
    OpenSSLObjectError,
)

from ansible_collections.community.crypto.plugins.module_utils.crypto.module_backends.certificate_info import (
    select_backend,
)

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    FileRequest,
    ConfigRequest
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueRequest
)

def main():
    module = AnsibleModule(
        argument_spec=dict(
            domain=dict(type='str'),
            path=dict(type='path'),
            directory=dict(type='str', choices=['cert', 'sharedcert'], default='cert'),
            content=dict(type='str'),
            state=dict(type='str', choices=['absent', 'present'], default='present'),
            select_crypto_backend=dict(type='str', default='auto', choices=['auto', 'cryptography']),
        ),
        required_one_of=(
            ['path', 'content'],
        ),
        mutually_exclusive=(
            ['path', 'content'],
        ),
        supports_check_mode=True,
    )

    result = {}


    connection = Connection(module._socket_path)

    if module.params['content'] is not None:
        data = module.params['content'].encode('utf-8')
    else:
        try:
            with open(module.params['path'], 'rb') as f:
                data = f.read()
        except (IOError, OSError) as e:
            module.fail_json(msg='Error while reading certificate file from disk: {0}'.format(e))

    backend, module_backend = select_backend(module, module.params['select_crypto_backend'], data)


    try:
        local_cert_info = module_backend.get_info()
        result['local_cert_info'] = local_cert_info

    except OpenSSLObjectError as exc:
        module.fail_json(msg=to_native(exc))

    domain = module.params['domain']
    state = module.params['state']
    directory = module.params['directory']
    cert_name = local_cert_info['subject']['commonName'] + '_exp_'+ local_cert_info['not_after']
    destination = '/{directory}/{cert_name}.pem'.format(directory=directory, cert_name=cert_name)
    x509_cert_base64 = base64.b64encode(data).decode()

    connection = Connection(module._socket_path)

    cert_detail_req = ActionQueueRequest(connection, domain, "ViewCertificateDetails" , {"CertificateObject" : cert_name})

    try:
        cert_detail_resp = cert_detail_req.post()
        result['cert_details'] = cert_detail_resp
        cert_exists = True
    except ConnectionError as ce:
        if 'The specified certificate does not exist.' not in to_text(ce):
            result['changed'] = False
            result['request'] = {'path': cert_detail_req.path, 'body': cert_detail_req.body}
            module.fail_json(msg=to_text(ce), **result)
        else:
            cert_exists = False

    if cert_exists == False:
        # Create file
        file_req = FileRequest(connection)
        file_req.set_path(domain=domain, file_path=destination)
        file_req.set_body(file_path=destination, content=x509_cert_base64)

        try:
            file_create_resp = file_req.post()
            result['file_create_resp'] = file_create_resp
            result['changed'] = True
        except ConnectionError as ce:
            if 'Resource already exists.' not in to_text(ce):
                result['changed'] = False
                result['request'] = {'path': cert_detail_req.path, 'body': cert_detail_req.body}
                module.fail_json(msg=to_text(ce), **result)
     

        cert_config = {
            'CryptoCertificate' : {
                "name": cert_name,
                "mAdminState": "enabled",
                "Filename": "{directory}:///{cert_name}.pem".format(directory=directory, cert_name=cert_name),
                "PasswordAlias": "off",
                "IgnoreExpiration": "off"
            }
        }
        cert_create_req = ConfigRequest(connection)
        cert_create_req.set_path(
            domain=domain,
            class_name='CryptoCertificate',
            name=cert_name
        )
        cert_create_req.set_body(body=cert_config)

        try:
            cert_create_resp = cert_create_req.post()
            result['cert_create_resp'] = cert_create_resp
            result['changed'] = True
        except ConnectionError as ce:
            result['changed'] = False
            result['request'] = {'path': cert_create_req.path, 'body': cert_create_req.body}
            module.fail_json(msg=to_text(ce), **result)



    module.exit_json(**result)

if __name__ == '__main__':
    main()
