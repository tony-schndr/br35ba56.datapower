from __future__ import absolute_import, division, print_function
__metaclass__ = type

from copy import deepcopy
from posixpath import join
from ansible.module_utils._text import to_text


from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    ensure_file,
    ensure_config
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    ActionQueueRequest
)
from ansible.module_utils.connection import (
    ConnectionError,
    Connection
)
from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    dp_diff
)


def get_cert_details(connection, domain, cert_name):
    cert_detail_req = ActionQueueRequest(
        connection,
        domain,
        "ViewCertificateDetails",
        {"CertificateObject": cert_name}
    )
    cert_details = None

    try:
        cert_details = cert_detail_req.post()
    except ConnectionError as ce:
        if 'The specified certificate does not exist.' not in to_text(ce):
            raise
    return cert_details


def process_crypto_module(module, local_cert_info, data):
    result = {}
    connection = Connection(module._socket_path)
    domain = module.params['domain']
    state = module.params['state']
    cert_dir = module.params['cert_dir']

    if module.params.get('obj_name') is not None:
        obj_name = module.params.get('obj_name')
    else:
        obj_name = '{common_name}_exp_{not_after}'.format(
            common_name=local_cert_info['subject']['commonName'],
            not_after=local_cert_info['not_after'])

    if module.params.get('file_name') is not None:
        file_name = module.params.get('file_name')
    else:
        file_name = '{common_name}_exp_{not_after}'.format(
            common_name=local_cert_info['subject']['commonName'],
            not_after=local_cert_info['not_after'])

    path = '/{cert_dir}/{file_name}.pem'.format(
        cert_dir=cert_dir, file_name=file_name)

    if obj_name is None:
        raise Exception(obj_name, file_name)
    config = {
        'CryptoCertificate': {
            "name": obj_name,
            "mAdminState": "enabled",
            "Filename": "{cert_dir}:///{file_name}.pem".format(cert_dir=cert_dir, file_name=file_name),
            "PasswordAlias": "off",
            "IgnoreExpiration": "off"
        }
    }

    result['file'] = ensure_file(module, domain, path, data, state)
    result['config'] = ensure_config(module, domain, config, state)
    result['details'] = get_cert_details(connection, domain, obj_name)

    if result['details'] and local_cert_info['serial_number'] != result['details']['CryptoCertificate']['CertificateDetails']['SerialNumber']['value']:

        module.fail_json(msg='Critical error, serial numbers do not match.\n'
                         'This would likely only happen if there was an existing cert by the same filename\n'
                         'as these modules will not overwrite a file in cert / sharedcert directories.  {local_serial_number} != {remote_serial_number}'
                         .format(
                             local_serial_number=local_cert_info['serial_number'],
                             remote_serial_number=result['details']['CryptoCertificate']['CertificateDetails']['SerialNumber']),
                         **result)

    return result
