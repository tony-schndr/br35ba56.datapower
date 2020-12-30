from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

import pytest
import json
from ansible_collections.community.datapower.plugins.module_utils.datapower import (
    dp_diff
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.mgmt import (
    DPManageConfigObject,
    DPManageConfigSchema
)
from ansible_collections.community.datapower.tests.unit.module_utils.test_data import (
    dp_mgmt_test_data as test_data,
    dp_actionq_test_data as action_test_data
)
class TestDPManageConfigObject:
    
    
    def load_schema(self, class_):
        with open('tests/unit/module_utils/test_data/schema/' + class_ +'.json') as f:
            data = json.loads(f.read())
        return DPManageConfigSchema(data['schema'])

    def test_DPManageConfigSchema(self):
        assert DPManageConfigSchema(test_data.valcred_schema_response)
        
    def test_DPManageConfigSchema_get_prop_1(self):   
        dp_schema = self.load_schema('CryptoValCred')
        assert dp_schema.get_prop('Certificate') == {
            "array": "true",
            "cli-alias": "certificate",
            "description": "Define the certificate aliases for the validation credentials. Each certificate is the validation credentials is the certificate that a TLS peer might send or is the certificate of the Certification Authority (CA) that signed the certificate sent by a peer or is the root certificate.",
            "display": "Certificates",
            "name": "Certificate",
            "summary": "Certificate aliases in the validation credentials list",
            "type": {
                "href": "/mgmt/types/default/dmReference",
                "reference-to": {
                    "href": "/mgmt/metadata/default/CryptoCertificate"
                }
            }
        }
        assert dp_schema.get_prop('nothing') == None

    def test_DPManageConfigSchema_get_prop_2(self):
        dp_schema = self.load_schema('AAAPolicy')
        assert dp_schema.get_prop('AZCacheTTL') == {
            "name": "AZCacheTTL",
            "default": 3,
            "cli-alias": "cache-ttl",
            "maximum": 86400,
            "summary": "Time to cache Authorization decisions.",
            "minimum": 1,
            "ignored-when": {
                "condition": {
                    "property-name": "AZCacheAllow",
                    "evaluation": "property-equals",
                    "value": "disabled"
                }
            },
            "units": "seconds",
            "type": {
                "href": "/mgmt/types/default/dmUInt32"
            },
            "display": "Cache lifetime"
        }

    def test_DPManageConfigSchema_get_type_href_from_prop_1(self):   
        dp_schema =self.load_schema('CryptoValCred')
        prop = dp_schema.get_prop('Certificate')
        href = dp_schema.get_type_href_from_prop(prop)
        assert href == '/mgmt/types/default/dmReference'

    def test_DPManageConfigSchema_get_type_href_from_prop_2(self):  
        dp_schema = self.load_schema('CryptoValCred') 
        prop = dp_schema.get_prop('mAdminState')
        href = dp_schema.get_type_href_from_prop(prop)
        assert href == "/mgmt/types/default/dmAdminState"

    def test_DPManageConfigSchema_get_type_href_from_prop_3(self):  
        dp_schema = self.load_schema('CryptoValCred')
        prop = dp_schema.get_prop('InitialPolicySet')
        href = dp_schema.get_type_href_from_prop(prop)
        assert href == '/mgmt/types/default/dmString'
    
    def test_DPManageConfigSchema_get_type_href_from_prop_4(self):  
        dp_schema = self.load_schema('AAAPolicy')
        prop = dp_schema.get_prop('AZCacheTTL')
        href = dp_schema.get_type_href_from_prop(prop)
        assert href == '/mgmt/types/default/dmUInt32'

    def test_DPManageConfigSchema_get_type_1 (self):   
        dp_schema = self.load_schema('CryptoValCred')
        assert dp_schema.get_type('/mgmt/types/default/dmString') == {
                "_links": {
                    "doc": {
                        "href": "/mgmt/docs/types/dmString"
                    },
                    "self": {
                        "href": "/mgmt/types/default/dmString"
                    }
                },
                "type": {
                    "cli-arg": "string",
                    "name": "dmString"
                }
            }

    def test_DPManageConfigSchema_get_type_2(self):
        dp_schema = self.load_schema('AAAPolicy')

        type_ = {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmUInt32"
                },
                "self": {
                    "href": "/mgmt/types/default/dmUInt32"
                }
            },
            "type": {
                "cli-arg": "number",
                "maximum": "0xFFFFFFFF",
                "minimum": 0,
                "name": "dmUInt32"
            }
        }
        assert dp_schema.get_type('/mgmt/types/default/dmUInt32') == type_

    def test_DPManageConfigSchema_get_is_valid_param_1(self):
        dp_schema = self.load_schema('CryptoValCred')
        assert dp_schema.is_valid_param('mAdminState', 'disabled')

    def test_DPManageConfigSchema_get_is_valid_param_2(self):
        dp_schema = self.load_schema('CryptoValCred')
        assert dp_schema.is_valid_param('Certificate', {'value': 'Test1'})


    def test_DPManageConfigSchema_get_is_valid_param_3(self):
        dp_schema = self.load_schema('CryptoValCred')
        assert dp_schema.is_valid_param('Certificate', {'Value': 'Test1'}) == False

    def test_DPManageConfigSchema_get_is_valid_param_4(self):
        dp_schema = self.load_schema('CryptoValCred')
        assert dp_schema.is_valid_param('ExplicitPolicy', 'on')

    def test_DPManageConfigSchema_get_is_valid_param_5(self):
        dp_schema = self.load_schema('CryptoValCred')
        assert dp_schema.is_valid_param('ExplicitPolicy', 'foo') == False
        
    def test_DPManageConfigSchema_get_is_valid_param_6(self):
        dp_schema = self.load_schema('CryptoValCred')
        assert dp_schema.is_valid_param('InitialPolicySet', 'anystring')

    def test_DPManageConfigSchema_get_is_valid_param_7(self):
        dp_schema = self.load_schema('CryptoValCred')
        assert dp_schema.is_valid_param('InitialPolicySet', 2) == False

    def test_DPManageConfigSchema_get_is_valid_param_8(self):
        dp_schema = self.load_schema('EthernetInterface')
        assert dp_schema.is_valid_param('IPAddress', '10.0.1.1')

    def test_DPManageConfigSchema_get_is_valid_param_9(self):
        dp_schema = self.load_schema('AAAPolicy')
        assert dp_schema.is_valid_param('ExtractIdentity', test_data.AAAPolicy_ExtractIdentity)

    def test_DPManageConfigSchema_get_is_valid_param_10(self):
        dp_schema = self.load_schema('EthernetInterface')
        assert dp_schema.is_valid_param('mAdminState', 'disabled')
    
    def test_DPManageConfigSchema_get_is_valid_param_nested_prop_in_type(self):
        dp_schema = self.load_schema('AAAPolicy')
        assert dp_schema.is_valid_param('AZCacheTTL', 3)

    def test_DPManageConfigSchema_schema_get_type_int_boundries(self):
        type_ = test_data.int_type
        dp_schema = self.load_schema('EthernetInterface')
        assert dp_schema.get_type_int_boundries(type_) == (0, 65535)
