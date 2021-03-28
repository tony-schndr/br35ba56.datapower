#!/usr/bin/python

# Copyright: (c) 2020, Anthony Schneider tonyschndr@gmail.com
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: list_objects

short_description: Get information on available configuration objects.


version_added: "1.0.0"

description: Use for retrieving information on various objects.  Target the 

options:
    domain:
        description: Target domain
        default: default
        type: str
        required: false
  
author: 
- Anthony Schneider (@br35ba56)
'''

EXAMPLES = r'''
# List all available objects
- name: Get object config info
  community.datapower.list_objects:

- name: Get object config info
  community.datapower.list_objects:
    domain: foo
'''
 
RETURN = r'''
objects:
    description: List of configurable objects for a DataPower domain
    type: list
    returned: always
    sample:  [
        "AAAJWTGenerator",
        "AAAJWTValidator",
        "AAAPolicy",
        "AMQPBroker",
        "AMQPSourceProtocolHandler",
        "APIApplicationType",
        "APIAuthURLRegistry",
        "APICORS",
        "APIClientIdentification",
        "APICollection",
        "APIConnectGatewayService",
        "APIDebugProbe",
        "APIDefinition",
        "APIExecute",
        "APIGateway",
        "APILDAPRegistry",
        "APIOperation",
        "APIPath",
        "APIPlan",
        "APIRateLimit",
        "APIResult",
        "APIRouting",
        "APIRule",
        "APISchema",
        "APISecurity",
        "APISecurityAPIKey",
        "APISecurityBasicAuth",
        "APISecurityOAuth",
        "APISecurityOAuthReq",
        "APISecurityRequirement",
        "APISecurityTokenManager",
        "AS1PollerSourceProtocolHandler",
        "AS2ProxySourceProtocolHandler",
        "AS2SourceProtocolHandler",
        "AS3SourceProtocolHandler",
        "AccessControlList",
        "AccessProfile",
        "AnalyticsEndpoint",
        "AppSecurityPolicy",
        "Assembly",
        "AssemblyActionClientSecurity",
        "AssemblyActionFunctionCall",
        "AssemblyActionGatewayScript",
        "AssemblyActionGraphQLIntrospect",
        "AssemblyActionHtmlPage",
        "AssemblyActionInvoke",
        "AssemblyActionJWTGenerate",
        "AssemblyActionJWTValidate",
        "AssemblyActionJson2Xml",
        "AssemblyActionLog",
        "AssemblyActionMap",
        "AssemblyActionOAuth",
        "AssemblyActionParse",
        "AssemblyActionRateLimit",
        "AssemblyActionRedact",
        "AssemblyActionSetVar",
        "AssemblyActionThrow",
        "AssemblyActionUserSecurity",
        "AssemblyActionValidate",
        "AssemblyActionXSLT",
        "AssemblyActionXml2Json",
        "AssemblyFunction",
        "AssemblyLogicOperationSwitch",
        "AssemblyLogicSwitch",
        "AuditLog",
        "B2BCPA",
        "B2BCPACollaboration",
        "B2BCPAReceiverSetting",
        "B2BCPASenderSetting",
        "B2BGateway",
        "B2BPersistence",
        "B2BProfile",
        "B2BProfileGroup",
        "B2BXPathRoutingPolicy",
        "CORSPolicy",
        "CORSRule",
        "CRLFetch",
        "CertMonitor",
        "CloudConnectorService",
        "CloudGatewayService",
        "CompileOptionsPolicy",
        "ConfigDeploymentPolicy",
        "ConfigSequence",
        "ConformancePolicy",
        "ControlList",
        "CookieAttributePolicy",
        "CountMonitor",
        "CryptoCertificate",
        "CryptoFWCred",
        "CryptoIdentCred",
        "CryptoKerberosKDC",
        "CryptoKerberosKeytab",
        "CryptoKey",
        "CryptoProfile",
        "CryptoSSKey",
        "CryptoValCred",
        "DNSNameService",
        "DeploymentPolicyParametersBinding",
        "DocumentCryptoMap",
        "Domain",
        "DomainAvailability",
        "DomainSettings",
        "DurationMonitor",
        "EBMS2SourceProtocolHandler",
        "EBMS3SourceProtocolHandler",
        "ErrorReportSettings",
        "EthernetInterface",
        "FTPFilePollerSourceProtocolHandler",
        "FTPQuoteCommands",
        "FTPServerSourceProtocolHandler",
        "FilterAction",
        "FormsLoginPolicy",
        "GWSRemoteDebug",
        "GWScriptSettings",
        "GatewayPeering",
        "GatewayPeeringManager",
        "GeneratedPolicy",
        "GraphQLSchemaOptions",
        "HTTPInputConversionMap",
        "HTTPSSourceProtocolHandler",
        "HTTPService",
        "HTTPSourceProtocolHandler",
        "HTTPUserAgent",
        "HostAlias",
        "ILMTScanner",
        "IMSCalloutSourceProtocolHandler",
        "IMSConnect",
        "IMSConnectSourceProtocolHandler",
        "IPMulticast",
        "ImportPackage",
        "IncludeConfig",
        "InteropService",
        "JOSERecipientIdentifier",
        "JOSESignatureIdentifier",
        "JSONSettings",
        "JWEHeader",
        "JWERecipient",
        "JWSSignature",
        "KafkaCluster",
        "KafkaSourceProtocolHandler",
        "LDAPConnectionPool",
        "LDAPSearchParameters",
        "Language",
        "LinkAggregation",
        "LoadBalancerGroup",
        "LogLabel",
        "LogTarget",
        "Luna",
        "LunaHAGroup",
        "LunaHASettings",
        "LunaPartition",
        "MCFCustomRule",
        "MCFHttpHeader",
        "MCFHttpMethod",
        "MCFHttpURL",
        "MCFXPath",
        "MPGWErrorAction",
        "MPGWErrorHandlingPolicy",
        "MQFTESourceProtocolHandler",
        "MQGW",
        "MQManager",
        "MQManagerGroup",
        "MQQM",
        "MQQMGroup",
        "MQSourceProtocolHandler",
        "MQhost",
        "MQproxy",
        "MQv9PlusMFTSourceProtocolHandler",
        "MQv9PlusSourceProtocolHandler",
        "MTOMPolicy",
        "Matching",
        "MessageContentFilters",
        "MessageMatching",
        "MessageType",
        "MgmtInterface",
        "MultiProtocolGateway",
        "NFSClientSettings",
        "NFSDynamicMounts",
        "NFSFilePollerSourceProtocolHandler",
        "NFSStaticMount",
        "NTPService",
        "NameValueProfile",
        "NetworkSettings",
        "OAuthProviderSettings",
        "OAuthSupportedClient",
        "OAuthSupportedClientGroup",
        "ODR",
        "ODRConnectorGroup",
        "OperationRateLimit",
        "POPPollerSourceProtocolHandler",
        "ParseSettings",
        "PasswordAlias",
        "Pattern",
        "PeerGroup",
        "PolicyAttachments",
        "PolicyParameters",
        "ProcessingMetadata",
        "QuotaEnforcementServer",
        "RADIUSSettings",
        "RBMSettings",
        "RaidVolume",
        "RestMgmtInterface",
        "SAMLAttributes",
        "SFTPFilePollerSourceProtocolHandler",
        "SLMAction",
        "SLMCredClass",
        "SLMPolicy",
        "SLMRsrcClass",
        "SLMSchedule",
        "SMTPServerConnection",
        "SNMPSettings",
        "SOAPHeaderDisposition",
        "SQLDataSource",
        "SSHClientProfile",
        "SSHDomainClientProfile",
        "SSHServerProfile",
        "SSHServerSourceProtocolHandler",
        "SSHService",
        "SSLClientProfile",
        "SSLProxyProfile",
        "SSLProxyService",
        "SSLSNIMapping",
        "SSLSNIServerProfile",
        "SSLServerProfile",
        "SchemaExceptionMap",
        "SecureBackupMode",
        "SecureCloudConnector",
        "SecureGatewayClient",
        "ShellAlias",
        "SimpleCountMonitor",
        "SocialLoginPolicy",
        "StandaloneStandbyControl",
        "StandaloneStandbyControlInterface",
        "StatelessTCPSourceProtocolHandler",
        "Statistics",
        "StylePolicy",
        "StylePolicyAction",
        "StylePolicyRule",
        "SystemSettings",
        "TAM",
        "TCPProxyService",
        "TFIMEndpoint",
        "TelnetService",
        "Throttler",
        "TimeSettings",
        "TraceTarget",
        "UDDIRegistry",
        "UDDISubscription",
        "URLMap",
        "URLRefreshPolicy",
        "URLRewritePolicy",
        "User",
        "UserGroup",
        "VLANInterface",
        "VisibilityList",
        "WCCService",
        "WSEndpointRewritePolicy",
        "WSGateway",
        "WSRRSavedSearchSubscription",
        "WSRRServer",
        "WSRRSubscription",
        "WSStylePolicy",
        "WSStylePolicyRule",
        "WXSGrid",
        "WebAppErrorHandlingPolicy",
        "WebAppFW",
        "WebAppRequest",
        "WebAppResponse",
        "WebAppSessionPolicy",
        "WebB2BViewer",
        "WebGUI",
        "WebServiceMonitor",
        "WebServicesAgent",
        "WebSphereJMSServer",
        "WebSphereJMSSourceProtocolHandler",
        "WebTokenService",
        "XACMLPDP",
        "XC10Grid",
        "XMLFirewallService",
        "XMLManager",
        "XPathRoutingMap",
        "XSLCoprocService",
        "XSLProxyService",
        "XTCProtocolHandler",
        "ZHybridTargetControlService",
        "ZosNSSClient",
        "xmltrace"
    ]
'''

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import (
    ConnectionError, 
    Connection
) 
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.community.datapower.plugins.module_utils.datapower.requests import (
    MGMT_CONFIG_URI,
    MGMT_CONFIG_METADATA_URI
)
from ansible_collections.community.datapower.plugins.module_utils.datapower.request_handlers import (
    DPManageConfigRequestHandler
)

def run_module():
    module_args = dict(
        domain = dict(type='str', required=False, default='default')
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True 
    )
    
    connection = Connection(module._socket_path)
    
    dp_handler = DPManageConfigRequestHandler(connection)

    resp = dp_handler.config_info(module.params['domain'], module.params['class_name'])

    result = {}
    result['objects'] = resp

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()