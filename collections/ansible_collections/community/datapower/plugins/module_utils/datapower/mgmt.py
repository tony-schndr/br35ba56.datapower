from __future__ import absolute_import, division, print_function

__metaclass__ = type


# This is hardcoded, the response is from DataPower v 10.0.1.0.
# This could be greatly improved by having it check an AnsibleFact.
# Would need to add a fact Module that gathers valid config object types
# from GET /mgmt/config/ and store it as a fact.
def is_valid_class(class_name):
    return val_obj_dict['_links'].get(class_name) or False
#PUT actionqueue help code here

class DPActionQueue():
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

class DPGetConfigObject:
    # domain and class_name are the bare minimum required to get a valid
    # response from DataPower
    # kwargs consisting of the arguments defined in the Ansible Modules
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)
        # If class_name not specified try to set it 
        # from config
        if not hasattr(self, 'class_name') or self.class_name is None:
            raise ValueError('Invalid class_name or no class_name provided.')
        
        if not hasattr(self, 'domain'):
            raise AttributeError('missing domain')


class DPManageConfigObject:
    # domain and class_name are the bare minimum required to get a valid
    # response from DataPower
    # kwargs consisting of the arguments defined in the Ansible Modules
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)
        # If class_name not specified try to set it 
        # from config
        if not hasattr(self, 'class_name') or self.class_name is None:
            self.class_name = list(self.config.keys())[0]
            if not is_valid_class(self.class_name):
                raise ValueError('Invalid class_name or no class_name provided.')
        
        if not hasattr(self, 'name') or self.name is None:
            if self.class_name in self.config:
                self.name = self.config.get(self.class_name).get('name')
            elif 'name' in self.config:
                self.name = self.config.get('name')
            else:
                raise AttributeError('name attribute is required.')
            
        if not hasattr(self, 'domain'):
            raise AttributeError('missing domain')

        if not hasattr(self,'config'):
            raise AttributeError('missing config')

class DPManageConfigSchema:
    
    def __init__(self, schema_resp):
        self.set_props(schema_resp)

    def get_prop(self, field):
        for prop in self.props:
            if prop.name == field:
                return prop
        else:
            return None

    # Create a property array to store the property objects, these are retrieved from the METADATA_URI
    # and store useful data like name of the feild, type, and if its an array or not.
    def set_props(self, schema_resp):
        self.props = []
        for dp_prop in schema_resp['object']['properties']['property']:
            prop = DPProperty()
            for k,v in dp_prop.items():
                if k == 'array':
                    if v == 'true':
                        setattr(prop, k, True)
                    else:
                        setattr(prop, k, False)
                else:
                    setattr(prop, k, v)
                self.props.append(prop)
            
class DPProperty:
    pass
def is_valid_object_class(obj):
    return obj in valid_objects

valid_objects = [ 
    'AAAPolicy',
    'Domain',
    'LDAPSearchParameters',
    'ProcessingMetadata',
    'RADIUSSettings',
    'RBMSettings',
    'SAMLAttributes',
    'SOAPHeaderDisposition',
    'TAM',
    'TFIMEndpoint',
    'XACMLPDP',
    'AccessControlList',
    'AccessProfile',
    'AnalyticsEndpoint',
    'APIApplicationType',
    'APICollection',
    'APIConnectGatewayService',
    'APIDefinition',
    'APIGateway',
    'APILDAPRegistry',
    'APIOperation',
    'APIPath',
    'APIPlan',
    'APISchema',
    'APISecurityAPIKey',
    'APISecurityBasicAuth',
    'APISecurityOAuthReq',
    'APISecurityOAuth',
    'APISecurityRequirement',
    'APISecurityTokenManager',
    'AppSecurityPolicy',
    'Assembly',
    'AuditLog',
    'B2BCPA',
    'B2BCPACollaboration',
    'B2BCPAReceiverSetting',
    'B2BCPASenderSetting',
    'B2BGateway',
    'B2BPersistence',
    'B2BProfile',
    'B2BProfileGroup',
    'B2BXPathRoutingPolicy',
    'WXSGrid',
    'XC10Grid',
    'CloudConnectorService',
    'CloudGatewayService',
    'CompactFlash',
    'CompileOptionsPolicy',
    'ConfigDeploymentPolicy',
    'ConfigSequence',
    'ConformancePolicy',
    'ControlList',
    'AAAJWTGenerator',
    'AAAJWTValidator',
    'CertMonitor',
    'CookieAttributePolicy',
    'CRLFetch',
    'CryptoCertificate',
    'CryptoFWCred',
    'CryptoIdentCred',
    'CryptoKerberosKDC',
    'CryptoKerberosKeytab',
    'CryptoKey',
    'CryptoProfile',
    'CryptoSSKey',
    'CryptoValCred',
    'JOSERecipientIdentifier',
    'JOSESignatureIdentifier',
    'JWEHeader',
    'JWERecipient',
    'JWSSignature',
    'OAuthSupportedClient',
    'OAuthSupportedClientGroup',
    'SocialLoginPolicy',
    'SSHClientProfile',
    'SSHDomainClientProfile',
    'SSHServerProfile',
    'SSLClientProfile',
    'SSLProxyProfile',
    'SSLServerProfile',
    'SSLSNIMapping',
    'SSLSNIServerProfile',
    'DeploymentPolicyParametersBinding',
    'ErrorReportSettings',
    'SystemSettings',
    'TimeSettings',
    'DFDLSettings',
    'DomainAvailability',
    'DomainSettings',
    'SchemaExceptionMap',
    'DocumentCryptoMap',
    'XPathRoutingMap',
    'LogTarget',
    'FormsLoginPolicy',
    'FTPQuoteCommands',
    'MultiProtocolGateway',
    'WSGateway',
    'GatewayPeering',
    'GeneratedPolicy',
    'GWScriptSettings',
    'HTTPInputConversionMap',
    'HTTPUserAgent',
    'ILMTScanner',
    'ImportPackage',
    'IMSConnect',
    'IncludeConfig',
    'InteropService',
    'EthernetInterface',
    'LinkAggregation',
    'VLANInterface',
    'IPMILanChannel',
    'IPMIUser',
    'IPMulticast',
    'ISAMReverseProxy',
    'ISAMReverseProxyJunction',
    'ISAMRuntime',
    'IScsiChapConfig',
    'IScsiHBAConfig',
    'IScsiInitiatorConfig',
    'IScsiTargetConfig',
    'IScsiVolumeConfig',
    'TibcoEMSServer',
    'WebSphereJMSServer',
    'JSONSettings',
    'Language',
    'LDAPConnectionPool',
    'LoadBalancerGroup',
    'LogLabel',
    'Luna',
    'LunaPartition',
    'Matching',
    'MCFCustomRule',
    'MCFHttpHeader',
    'MCFHttpMethod',
    'MCFHttpURL',
    'MCFXPath',
    'MessageContentFilters',
    'FilterAction',
    'MessageMatching',
    'CountMonitor',
    'DurationMonitor',
    'MessageType',
    'MPGWErrorAction',
    'MPGWErrorHandlingPolicy',
    'MQGW',
    'MQhost',
    'MQproxy',
    'MQQM',
    'MQQMGroup',
    'MTOMPolicy',
    'NameValueProfile',
    'DNSNameService',
    'HostAlias',
    'NetworkSettings',
    'NTPService',
    'NFSClientSettings',
    'NFSDynamicMounts',
    'NFSStaticMount',
    'OAuthProviderSettings',
    'ODR',
    'ODRConnectorGroup',
    'OperationRateLimit',
    'ParseSettings',
    'PasswordAlias',
    'Pattern',
    'PeerGroup',
    'PolicyAttachments',
    'PolicyParameters',
    'ProductInsights',
    'QuotaEnforcementServer',
    'RaidVolume',
    'SQLRuntimeSettings',
    'SecureBackupMode',
    'SecureCloudConnector',
    'SecureGatewayClient',
    'GWSRemoteDebug',
    'MgmtInterface',
    'RestMgmtInterface',
    'SSHService',
    'TelnetService',
    'WebB2BViewer',
    'WebGUI',
    'XMLFirewallService',
    'XSLProxyService',
    'HTTPService',
    'SSLProxyService',
    'TCPProxyService',
    'XSLCoprocService',
    'ShellAlias',
    'SimpleCountMonitor',
    'SLMAction',
    'SLMCredClass',
    'SLMPolicy',
    'SLMRsrcClass',
    'SLMSchedule',
    'SMTPServerConnection',
    'SNMPSettings',
    'AS2ProxySourceProtocolHandler',
    'AS2SourceProtocolHandler',
    'AS3SourceProtocolHandler',
    'EBMS2SourceProtocolHandler',
    'EBMS3SourceProtocolHandler',
    'FTPFilePollerSourceProtocolHandler',
    'NFSFilePollerSourceProtocolHandler',
    'SFTPFilePollerSourceProtocolHandler',
    'FTPServerSourceProtocolHandler',
    'HTTPSourceProtocolHandler',
    'HTTPSSourceProtocolHandler',
    'IMSCalloutSourceProtocolHandler',
    'IMSConnectSourceProtocolHandler',
    'TibcoEMSSourceProtocolHandler',
    'WebSphereJMSSourceProtocolHandler',
    'MQFTESourceProtocolHandler',
    'MQSourceProtocolHandler',
    'AS1PollerSourceProtocolHandler',
    'POPPollerSourceProtocolHandler',
    'SSHServerSourceProtocolHandler',
    'StatelessTCPSourceProtocolHandler',
    'XTCProtocolHandler',
    'SQLDataSource',
    'StandaloneStandbyControl',
    'StandaloneStandbyControlInterface',
    'Statistics',
    'StylePolicy',
    'APIClientIdentification',
    'APIContext',
    'APICORS',
    'APIExecute',
    'APIRateLimit',
    'APIResult',
    'APIRouting',
    'APISecurity',
    'AssemblyActionGatewayScript',
    'AssemblyActionInvoke',
    'AssemblyActionJson2Xml',
    'AssemblyActionJWTGenerate',
    'AssemblyActionJWTValidate',
    'AssemblyActionMap',
    'AssemblyActionOAuth',
    'AssemblyActionParse',
    'AssemblyActionSetVar',
    'AssemblyActionUserSecurity',
    'AssemblyActionValidate',
    'AssemblyActionXml2Json',
    'AssemblyActionXSLT',
    'AssemblyActionThrow',
    'AssemblyLogicSwitch',
    'StylePolicyAction',
    'APIRule',
    'StylePolicyRule',
    'WSStylePolicyRule',
    'Tenant',
    'Throttler',
    'UDDIRegistry',
    'URLMap',
    'URLRefreshPolicy',
    'URLRewritePolicy',
    'User',
    'UserGroup',
    'WCCService',
    'WebAppErrorHandlingPolicy',
    'WebAppFW',
    'WebAppRequest',
    'WebAppResponse',
    'WebAppSessionPolicy',
    'WebServiceMonitor',
    'WebServicesAgent',
    'UDDISubscription',
    'WSRRSavedSearchSubscription',
    'WSRRSubscription',
    'WebTokenService',
    'WSEndpointRewritePolicy',
    'WSRRServer',
    'WSStylePolicy',
    'XMLManager',
    'xmltrace',
    'ZHybridTargetControlService',
    'ZosNSSClient',
]


val_obj_dict = {
    "_links": {
        "self": {
            "href": "/mgmt/config/"
        },
        "AAAJWTGenerator": {
            "href": "/mgmt/config/{domain}/AAAJWTGenerator"
        },
        "AAAJWTValidator": {
            "href": "/mgmt/config/{domain}/AAAJWTValidator"
        },
        "AAAPolicy": {
            "href": "/mgmt/config/{domain}/AAAPolicy"
        },
        "AccessControlList": {
            "href": "/mgmt/config/{domain}/AccessControlList"
        },
        "AccessProfile": {
            "href": "/mgmt/config/{domain}/AccessProfile"
        },
        "AMQPBroker": {
            "href": "/mgmt/config/{domain}/AMQPBroker"
        },
        "AMQPSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/AMQPSourceProtocolHandler"
        },
        "AnalyticsEndpoint": {
            "href": "/mgmt/config/{domain}/AnalyticsEndpoint"
        },
        "APIApplicationType": {
            "href": "/mgmt/config/{domain}/APIApplicationType"
        },
        "APIAuthURLRegistry": {
            "href": "/mgmt/config/{domain}/APIAuthURLRegistry"
        },
        "APIClientIdentification": {
            "href": "/mgmt/config/{domain}/APIClientIdentification"
        },
        "APICollection": {
            "href": "/mgmt/config/{domain}/APICollection"
        },
        "APIConnectGatewayService": {
            "href": "/mgmt/config/{domain}/APIConnectGatewayService"
        },
        "APICORS": {
            "href": "/mgmt/config/{domain}/APICORS"
        },
        "APIDebugProbe": {
            "href": "/mgmt/config/{domain}/APIDebugProbe"
        },
        "APIDefinition": {
            "href": "/mgmt/config/{domain}/APIDefinition"
        },
        "APIExecute": {
            "href": "/mgmt/config/{domain}/APIExecute"
        },
        "APIGateway": {
            "href": "/mgmt/config/{domain}/APIGateway"
        },
        "APILDAPRegistry": {
            "href": "/mgmt/config/{domain}/APILDAPRegistry"
        },
        "APIOperation": {
            "href": "/mgmt/config/{domain}/APIOperation"
        },
        "APIPath": {
            "href": "/mgmt/config/{domain}/APIPath"
        },
        "APIPlan": {
            "href": "/mgmt/config/{domain}/APIPlan"
        },
        "APIRateLimit": {
            "href": "/mgmt/config/{domain}/APIRateLimit"
        },
        "APIResult": {
            "href": "/mgmt/config/{domain}/APIResult"
        },
        "APIRouting": {
            "href": "/mgmt/config/{domain}/APIRouting"
        },
        "APIRule": {
            "href": "/mgmt/config/{domain}/APIRule"
        },
        "APISchema": {
            "href": "/mgmt/config/{domain}/APISchema"
        },
        "APISecurity": {
            "href": "/mgmt/config/{domain}/APISecurity"
        },
        "APISecurityAPIKey": {
            "href": "/mgmt/config/{domain}/APISecurityAPIKey"
        },
        "APISecurityBasicAuth": {
            "href": "/mgmt/config/{domain}/APISecurityBasicAuth"
        },
        "APISecurityOAuth": {
            "href": "/mgmt/config/{domain}/APISecurityOAuth"
        },
        "APISecurityOAuthReq": {
            "href": "/mgmt/config/{domain}/APISecurityOAuthReq"
        },
        "APISecurityRequirement": {
            "href": "/mgmt/config/{domain}/APISecurityRequirement"
        },
        "APISecurityTokenManager": {
            "href": "/mgmt/config/{domain}/APISecurityTokenManager"
        },
        "AppSecurityPolicy": {
            "href": "/mgmt/config/{domain}/AppSecurityPolicy"
        },
        "AS1PollerSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/AS1PollerSourceProtocolHandler"
        },
        "AS2ProxySourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/AS2ProxySourceProtocolHandler"
        },
        "AS2SourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/AS2SourceProtocolHandler"
        },
        "AS3SourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/AS3SourceProtocolHandler"
        },
        "Assembly": {
            "href": "/mgmt/config/{domain}/Assembly"
        },
        "AssemblyActionClientSecurity": {
            "href": "/mgmt/config/{domain}/AssemblyActionClientSecurity"
        },
        "AssemblyActionFunctionCall": {
            "href": "/mgmt/config/{domain}/AssemblyActionFunctionCall"
        },
        "AssemblyActionGatewayScript": {
            "href": "/mgmt/config/{domain}/AssemblyActionGatewayScript"
        },
        "AssemblyActionGraphQLIntrospect": {
            "href": "/mgmt/config/{domain}/AssemblyActionGraphQLIntrospect"
        },
        "AssemblyActionHtmlPage": {
            "href": "/mgmt/config/{domain}/AssemblyActionHtmlPage"
        },
        "AssemblyActionInvoke": {
            "href": "/mgmt/config/{domain}/AssemblyActionInvoke"
        },
        "AssemblyActionJson2Xml": {
            "href": "/mgmt/config/{domain}/AssemblyActionJson2Xml"
        },
        "AssemblyActionJWTGenerate": {
            "href": "/mgmt/config/{domain}/AssemblyActionJWTGenerate"
        },
        "AssemblyActionJWTValidate": {
            "href": "/mgmt/config/{domain}/AssemblyActionJWTValidate"
        },
        "AssemblyActionLog": {
            "href": "/mgmt/config/{domain}/AssemblyActionLog"
        },
        "AssemblyActionMap": {
            "href": "/mgmt/config/{domain}/AssemblyActionMap"
        },
        "AssemblyActionOAuth": {
            "href": "/mgmt/config/{domain}/AssemblyActionOAuth"
        },
        "AssemblyActionParse": {
            "href": "/mgmt/config/{domain}/AssemblyActionParse"
        },
        "AssemblyActionRateLimit": {
            "href": "/mgmt/config/{domain}/AssemblyActionRateLimit"
        },
        "AssemblyActionRedact": {
            "href": "/mgmt/config/{domain}/AssemblyActionRedact"
        },
        "AssemblyActionSetVar": {
            "href": "/mgmt/config/{domain}/AssemblyActionSetVar"
        },
        "AssemblyActionThrow": {
            "href": "/mgmt/config/{domain}/AssemblyActionThrow"
        },
        "AssemblyActionUserSecurity": {
            "href": "/mgmt/config/{domain}/AssemblyActionUserSecurity"
        },
        "AssemblyActionValidate": {
            "href": "/mgmt/config/{domain}/AssemblyActionValidate"
        },
        "AssemblyActionXml2Json": {
            "href": "/mgmt/config/{domain}/AssemblyActionXml2Json"
        },
        "AssemblyActionXSLT": {
            "href": "/mgmt/config/{domain}/AssemblyActionXSLT"
        },
        "AssemblyFunction": {
            "href": "/mgmt/config/{domain}/AssemblyFunction"
        },
        "AssemblyLogicOperationSwitch": {
            "href": "/mgmt/config/{domain}/AssemblyLogicOperationSwitch"
        },
        "AssemblyLogicSwitch": {
            "href": "/mgmt/config/{domain}/AssemblyLogicSwitch"
        },
        "AuditLog": {
            "href": "/mgmt/config/{domain}/AuditLog"
        },
        "B2BCPA": {
            "href": "/mgmt/config/{domain}/B2BCPA"
        },
        "B2BCPACollaboration": {
            "href": "/mgmt/config/{domain}/B2BCPACollaboration"
        },
        "B2BCPAReceiverSetting": {
            "href": "/mgmt/config/{domain}/B2BCPAReceiverSetting"
        },
        "B2BCPASenderSetting": {
            "href": "/mgmt/config/{domain}/B2BCPASenderSetting"
        },
        "B2BGateway": {
            "href": "/mgmt/config/{domain}/B2BGateway"
        },
        "B2BPersistence": {
            "href": "/mgmt/config/{domain}/B2BPersistence"
        },
        "B2BProfile": {
            "href": "/mgmt/config/{domain}/B2BProfile"
        },
        "B2BProfileGroup": {
            "href": "/mgmt/config/{domain}/B2BProfileGroup"
        },
        "B2BXPathRoutingPolicy": {
            "href": "/mgmt/config/{domain}/B2BXPathRoutingPolicy"
        },
        "CertMonitor": {
            "href": "/mgmt/config/{domain}/CertMonitor"
        },
        "CloudConnectorService": {
            "href": "/mgmt/config/{domain}/CloudConnectorService"
        },
        "CloudGatewayService": {
            "href": "/mgmt/config/{domain}/CloudGatewayService"
        },
        "CompileOptionsPolicy": {
            "href": "/mgmt/config/{domain}/CompileOptionsPolicy"
        },
        "ConfigDeploymentPolicy": {
            "href": "/mgmt/config/{domain}/ConfigDeploymentPolicy"
        },
        "ConfigSequence": {
            "href": "/mgmt/config/{domain}/ConfigSequence"
        },
        "ConformancePolicy": {
            "href": "/mgmt/config/{domain}/ConformancePolicy"
        },
        "ControlList": {
            "href": "/mgmt/config/{domain}/ControlList"
        },
        "CookieAttributePolicy": {
            "href": "/mgmt/config/{domain}/CookieAttributePolicy"
        },
        "CountMonitor": {
            "href": "/mgmt/config/{domain}/CountMonitor"
        },
        "CRLFetch": {
            "href": "/mgmt/config/{domain}/CRLFetch"
        },
        "CryptoCertificate": {
            "href": "/mgmt/config/{domain}/CryptoCertificate"
        },
        "CryptoFWCred": {
            "href": "/mgmt/config/{domain}/CryptoFWCred"
        },
        "CryptoIdentCred": {
            "href": "/mgmt/config/{domain}/CryptoIdentCred"
        },
        "CryptoKerberosKDC": {
            "href": "/mgmt/config/{domain}/CryptoKerberosKDC"
        },
        "CryptoKerberosKeytab": {
            "href": "/mgmt/config/{domain}/CryptoKerberosKeytab"
        },
        "CryptoKey": {
            "href": "/mgmt/config/{domain}/CryptoKey"
        },
        "CryptoProfile": {
            "href": "/mgmt/config/{domain}/CryptoProfile"
        },
        "CryptoSSKey": {
            "href": "/mgmt/config/{domain}/CryptoSSKey"
        },
        "CryptoValCred": {
            "href": "/mgmt/config/{domain}/CryptoValCred"
        },
        "DeploymentPolicyParametersBinding": {
            "href": "/mgmt/config/{domain}/DeploymentPolicyParametersBinding"
        },
        "DNSNameService": {
            "href": "/mgmt/config/{domain}/DNSNameService"
        },
        "DocumentCryptoMap": {
            "href": "/mgmt/config/{domain}/DocumentCryptoMap"
        },
        "Domain": {
            "href": "/mgmt/config/{domain}/Domain"
        },
        "DomainAvailability": {
            "href": "/mgmt/config/{domain}/DomainAvailability"
        },
        "DomainSettings": {
            "href": "/mgmt/config/{domain}/DomainSettings"
        },
        "DurationMonitor": {
            "href": "/mgmt/config/{domain}/DurationMonitor"
        },
        "EBMS2SourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/EBMS2SourceProtocolHandler"
        },
        "EBMS3SourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/EBMS3SourceProtocolHandler"
        },
        "ErrorReportSettings": {
            "href": "/mgmt/config/{domain}/ErrorReportSettings"
        },
        "EthernetInterface": {
            "href": "/mgmt/config/{domain}/EthernetInterface"
        },
        "FilterAction": {
            "href": "/mgmt/config/{domain}/FilterAction"
        },
        "FormsLoginPolicy": {
            "href": "/mgmt/config/{domain}/FormsLoginPolicy"
        },
        "FTPFilePollerSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/FTPFilePollerSourceProtocolHandler"
        },
        "FTPQuoteCommands": {
            "href": "/mgmt/config/{domain}/FTPQuoteCommands"
        },
        "FTPServerSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/FTPServerSourceProtocolHandler"
        },
        "GatewayPeering": {
            "href": "/mgmt/config/{domain}/GatewayPeering"
        },
        "GatewayPeeringManager": {
            "href": "/mgmt/config/{domain}/GatewayPeeringManager"
        },
        "GeneratedPolicy": {
            "href": "/mgmt/config/{domain}/GeneratedPolicy"
        },
        "GWScriptSettings": {
            "href": "/mgmt/config/{domain}/GWScriptSettings"
        },
        "GWSRemoteDebug": {
            "href": "/mgmt/config/{domain}/GWSRemoteDebug"
        },
        "HostAlias": {
            "href": "/mgmt/config/{domain}/HostAlias"
        },
        "HTTPInputConversionMap": {
            "href": "/mgmt/config/{domain}/HTTPInputConversionMap"
        },
        "HTTPService": {
            "href": "/mgmt/config/{domain}/HTTPService"
        },
        "HTTPSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/HTTPSourceProtocolHandler"
        },
        "HTTPSSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/HTTPSSourceProtocolHandler"
        },
        "HTTPUserAgent": {
            "href": "/mgmt/config/{domain}/HTTPUserAgent"
        },
        "ILMTScanner": {
            "href": "/mgmt/config/{domain}/ILMTScanner"
        },
        "ImportPackage": {
            "href": "/mgmt/config/{domain}/ImportPackage"
        },
        "IMSCalloutSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/IMSCalloutSourceProtocolHandler"
        },
        "IMSConnect": {
            "href": "/mgmt/config/{domain}/IMSConnect"
        },
        "IMSConnectSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/IMSConnectSourceProtocolHandler"
        },
        "IncludeConfig": {
            "href": "/mgmt/config/{domain}/IncludeConfig"
        },
        "InteropService": {
            "href": "/mgmt/config/{domain}/InteropService"
        },
        "IPMulticast": {
            "href": "/mgmt/config/{domain}/IPMulticast"
        },
        "JOSERecipientIdentifier": {
            "href": "/mgmt/config/{domain}/JOSERecipientIdentifier"
        },
        "JOSESignatureIdentifier": {
            "href": "/mgmt/config/{domain}/JOSESignatureIdentifier"
        },
        "JSONSettings": {
            "href": "/mgmt/config/{domain}/JSONSettings"
        },
        "JWEHeader": {
            "href": "/mgmt/config/{domain}/JWEHeader"
        },
        "JWERecipient": {
            "href": "/mgmt/config/{domain}/JWERecipient"
        },
        "JWSSignature": {
            "href": "/mgmt/config/{domain}/JWSSignature"
        },
        "KafkaCluster": {
            "href": "/mgmt/config/{domain}/KafkaCluster"
        },
        "KafkaSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/KafkaSourceProtocolHandler"
        },
        "Language": {
            "href": "/mgmt/config/{domain}/Language"
        },
        "LDAPConnectionPool": {
            "href": "/mgmt/config/{domain}/LDAPConnectionPool"
        },
        "LDAPSearchParameters": {
            "href": "/mgmt/config/{domain}/LDAPSearchParameters"
        },
        "LinkAggregation": {
            "href": "/mgmt/config/{domain}/LinkAggregation"
        },
        "LoadBalancerGroup": {
            "href": "/mgmt/config/{domain}/LoadBalancerGroup"
        },
        "LogLabel": {
            "href": "/mgmt/config/{domain}/LogLabel"
        },
        "LogTarget": {
            "href": "/mgmt/config/{domain}/LogTarget"
        },
        "Luna": {
            "href": "/mgmt/config/{domain}/Luna"
        },
        "LunaHAGroup": {
            "href": "/mgmt/config/{domain}/LunaHAGroup"
        },
        "LunaHASettings": {
            "href": "/mgmt/config/{domain}/LunaHASettings"
        },
        "LunaPartition": {
            "href": "/mgmt/config/{domain}/LunaPartition"
        },
        "Matching": {
            "href": "/mgmt/config/{domain}/Matching"
        },
        "MCFCustomRule": {
            "href": "/mgmt/config/{domain}/MCFCustomRule"
        },
        "MCFHttpHeader": {
            "href": "/mgmt/config/{domain}/MCFHttpHeader"
        },
        "MCFHttpMethod": {
            "href": "/mgmt/config/{domain}/MCFHttpMethod"
        },
        "MCFHttpURL": {
            "href": "/mgmt/config/{domain}/MCFHttpURL"
        },
        "MCFXPath": {
            "href": "/mgmt/config/{domain}/MCFXPath"
        },
        "MessageContentFilters": {
            "href": "/mgmt/config/{domain}/MessageContentFilters"
        },
        "MessageMatching": {
            "href": "/mgmt/config/{domain}/MessageMatching"
        },
        "MessageType": {
            "href": "/mgmt/config/{domain}/MessageType"
        },
        "MgmtInterface": {
            "href": "/mgmt/config/{domain}/MgmtInterface"
        },
        "MPGWErrorAction": {
            "href": "/mgmt/config/{domain}/MPGWErrorAction"
        },
        "MPGWErrorHandlingPolicy": {
            "href": "/mgmt/config/{domain}/MPGWErrorHandlingPolicy"
        },
        "MQFTESourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/MQFTESourceProtocolHandler"
        },
        "MQGW": {
            "href": "/mgmt/config/{domain}/MQGW"
        },
        "MQhost": {
            "href": "/mgmt/config/{domain}/MQhost"
        },
        "MQproxy": {
            "href": "/mgmt/config/{domain}/MQproxy"
        },
        "MQQM": {
            "href": "/mgmt/config/{domain}/MQQM"
        },
        "MQQMGroup": {
            "href": "/mgmt/config/{domain}/MQQMGroup"
        },
        "MQSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/MQSourceProtocolHandler"
        },
        "MTOMPolicy": {
            "href": "/mgmt/config/{domain}/MTOMPolicy"
        },
        "MultiProtocolGateway": {
            "href": "/mgmt/config/{domain}/MultiProtocolGateway"
        },
        "NameValueProfile": {
            "href": "/mgmt/config/{domain}/NameValueProfile"
        },
        "NetworkSettings": {
            "href": "/mgmt/config/{domain}/NetworkSettings"
        },
        "NFSClientSettings": {
            "href": "/mgmt/config/{domain}/NFSClientSettings"
        },
        "NFSDynamicMounts": {
            "href": "/mgmt/config/{domain}/NFSDynamicMounts"
        },
        "NFSFilePollerSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/NFSFilePollerSourceProtocolHandler"
        },
        "NFSStaticMount": {
            "href": "/mgmt/config/{domain}/NFSStaticMount"
        },
        "NTPService": {
            "href": "/mgmt/config/{domain}/NTPService"
        },
        "OAuthProviderSettings": {
            "href": "/mgmt/config/{domain}/OAuthProviderSettings"
        },
        "OAuthSupportedClient": {
            "href": "/mgmt/config/{domain}/OAuthSupportedClient"
        },
        "OAuthSupportedClientGroup": {
            "href": "/mgmt/config/{domain}/OAuthSupportedClientGroup"
        },
        "ODR": {
            "href": "/mgmt/config/{domain}/ODR"
        },
        "ODRConnectorGroup": {
            "href": "/mgmt/config/{domain}/ODRConnectorGroup"
        },
        "OperationRateLimit": {
            "href": "/mgmt/config/{domain}/OperationRateLimit"
        },
        "ParseSettings": {
            "href": "/mgmt/config/{domain}/ParseSettings"
        },
        "PasswordAlias": {
            "href": "/mgmt/config/{domain}/PasswordAlias"
        },
        "Pattern": {
            "href": "/mgmt/config/{domain}/Pattern"
        },
        "PeerGroup": {
            "href": "/mgmt/config/{domain}/PeerGroup"
        },
        "PolicyAttachments": {
            "href": "/mgmt/config/{domain}/PolicyAttachments"
        },
        "PolicyParameters": {
            "href": "/mgmt/config/{domain}/PolicyParameters"
        },
        "POPPollerSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/POPPollerSourceProtocolHandler"
        },
        "ProcessingMetadata": {
            "href": "/mgmt/config/{domain}/ProcessingMetadata"
        },
        "QuotaEnforcementServer": {
            "href": "/mgmt/config/{domain}/QuotaEnforcementServer"
        },
        "RADIUSSettings": {
            "href": "/mgmt/config/{domain}/RADIUSSettings"
        },
        "RaidVolume": {
            "href": "/mgmt/config/{domain}/RaidVolume"
        },
        "RBMSettings": {
            "href": "/mgmt/config/{domain}/RBMSettings"
        },
        "RestMgmtInterface": {
            "href": "/mgmt/config/{domain}/RestMgmtInterface"
        },
        "SAMLAttributes": {
            "href": "/mgmt/config/{domain}/SAMLAttributes"
        },
        "SchemaExceptionMap": {
            "href": "/mgmt/config/{domain}/SchemaExceptionMap"
        },
        "SecureBackupMode": {
            "href": "/mgmt/config/{domain}/SecureBackupMode"
        },
        "SecureCloudConnector": {
            "href": "/mgmt/config/{domain}/SecureCloudConnector"
        },
        "SecureGatewayClient": {
            "href": "/mgmt/config/{domain}/SecureGatewayClient"
        },
        "SFTPFilePollerSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/SFTPFilePollerSourceProtocolHandler"
        },
        "ShellAlias": {
            "href": "/mgmt/config/{domain}/ShellAlias"
        },
        "SimpleCountMonitor": {
            "href": "/mgmt/config/{domain}/SimpleCountMonitor"
        },
        "SLMAction": {
            "href": "/mgmt/config/{domain}/SLMAction"
        },
        "SLMCredClass": {
            "href": "/mgmt/config/{domain}/SLMCredClass"
        },
        "SLMPolicy": {
            "href": "/mgmt/config/{domain}/SLMPolicy"
        },
        "SLMRsrcClass": {
            "href": "/mgmt/config/{domain}/SLMRsrcClass"
        },
        "SLMSchedule": {
            "href": "/mgmt/config/{domain}/SLMSchedule"
        },
        "SMTPServerConnection": {
            "href": "/mgmt/config/{domain}/SMTPServerConnection"
        },
        "SNMPSettings": {
            "href": "/mgmt/config/{domain}/SNMPSettings"
        },
        "SOAPHeaderDisposition": {
            "href": "/mgmt/config/{domain}/SOAPHeaderDisposition"
        },
        "SocialLoginPolicy": {
            "href": "/mgmt/config/{domain}/SocialLoginPolicy"
        },
        "SQLDataSource": {
            "href": "/mgmt/config/{domain}/SQLDataSource"
        },
        "SSHClientProfile": {
            "href": "/mgmt/config/{domain}/SSHClientProfile"
        },
        "SSHDomainClientProfile": {
            "href": "/mgmt/config/{domain}/SSHDomainClientProfile"
        },
        "SSHServerProfile": {
            "href": "/mgmt/config/{domain}/SSHServerProfile"
        },
        "SSHServerSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/SSHServerSourceProtocolHandler"
        },
        "SSHService": {
            "href": "/mgmt/config/{domain}/SSHService"
        },
        "SSLClientProfile": {
            "href": "/mgmt/config/{domain}/SSLClientProfile"
        },
        "SSLProxyProfile": {
            "href": "/mgmt/config/{domain}/SSLProxyProfile"
        },
        "SSLProxyService": {
            "href": "/mgmt/config/{domain}/SSLProxyService"
        },
        "SSLServerProfile": {
            "href": "/mgmt/config/{domain}/SSLServerProfile"
        },
        "SSLSNIMapping": {
            "href": "/mgmt/config/{domain}/SSLSNIMapping"
        },
        "SSLSNIServerProfile": {
            "href": "/mgmt/config/{domain}/SSLSNIServerProfile"
        },
        "StandaloneStandbyControl": {
            "href": "/mgmt/config/{domain}/StandaloneStandbyControl"
        },
        "StandaloneStandbyControlInterface": {
            "href": "/mgmt/config/{domain}/StandaloneStandbyControlInterface"
        },
        "StatelessTCPSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/StatelessTCPSourceProtocolHandler"
        },
        "Statistics": {
            "href": "/mgmt/config/{domain}/Statistics"
        },
        "StylePolicy": {
            "href": "/mgmt/config/{domain}/StylePolicy"
        },
        "StylePolicyAction": {
            "href": "/mgmt/config/{domain}/StylePolicyAction"
        },
        "StylePolicyRule": {
            "href": "/mgmt/config/{domain}/StylePolicyRule"
        },
        "SystemSettings": {
            "href": "/mgmt/config/{domain}/SystemSettings"
        },
        "TAM": {
            "href": "/mgmt/config/{domain}/TAM"
        },
        "TCPProxyService": {
            "href": "/mgmt/config/{domain}/TCPProxyService"
        },
        "TelnetService": {
            "href": "/mgmt/config/{domain}/TelnetService"
        },
        "TFIMEndpoint": {
            "href": "/mgmt/config/{domain}/TFIMEndpoint"
        },
        "Throttler": {
            "href": "/mgmt/config/{domain}/Throttler"
        },
        "TimeSettings": {
            "href": "/mgmt/config/{domain}/TimeSettings"
        },
        "TraceTarget": {
            "href": "/mgmt/config/{domain}/TraceTarget"
        },
        "UDDIRegistry": {
            "href": "/mgmt/config/{domain}/UDDIRegistry"
        },
        "UDDISubscription": {
            "href": "/mgmt/config/{domain}/UDDISubscription"
        },
        "URLMap": {
            "href": "/mgmt/config/{domain}/URLMap"
        },
        "URLRefreshPolicy": {
            "href": "/mgmt/config/{domain}/URLRefreshPolicy"
        },
        "URLRewritePolicy": {
            "href": "/mgmt/config/{domain}/URLRewritePolicy"
        },
        "User": {
            "href": "/mgmt/config/{domain}/User"
        },
        "UserGroup": {
            "href": "/mgmt/config/{domain}/UserGroup"
        },
        "VLANInterface": {
            "href": "/mgmt/config/{domain}/VLANInterface"
        },
        "WCCService": {
            "href": "/mgmt/config/{domain}/WCCService"
        },
        "WebAppErrorHandlingPolicy": {
            "href": "/mgmt/config/{domain}/WebAppErrorHandlingPolicy"
        },
        "WebAppFW": {
            "href": "/mgmt/config/{domain}/WebAppFW"
        },
        "WebAppRequest": {
            "href": "/mgmt/config/{domain}/WebAppRequest"
        },
        "WebAppResponse": {
            "href": "/mgmt/config/{domain}/WebAppResponse"
        },
        "WebAppSessionPolicy": {
            "href": "/mgmt/config/{domain}/WebAppSessionPolicy"
        },
        "WebB2BViewer": {
            "href": "/mgmt/config/{domain}/WebB2BViewer"
        },
        "WebGUI": {
            "href": "/mgmt/config/{domain}/WebGUI"
        },
        "WebServiceMonitor": {
            "href": "/mgmt/config/{domain}/WebServiceMonitor"
        },
        "WebServicesAgent": {
            "href": "/mgmt/config/{domain}/WebServicesAgent"
        },
        "WebSphereJMSServer": {
            "href": "/mgmt/config/{domain}/WebSphereJMSServer"
        },
        "WebSphereJMSSourceProtocolHandler": {
            "href": "/mgmt/config/{domain}/WebSphereJMSSourceProtocolHandler"
        },
        "WebTokenService": {
            "href": "/mgmt/config/{domain}/WebTokenService"
        },
        "WSEndpointRewritePolicy": {
            "href": "/mgmt/config/{domain}/WSEndpointRewritePolicy"
        },
        "WSGateway": {
            "href": "/mgmt/config/{domain}/WSGateway"
        },
        "WSRRSavedSearchSubscription": {
            "href": "/mgmt/config/{domain}/WSRRSavedSearchSubscription"
        },
        "WSRRServer": {
            "href": "/mgmt/config/{domain}/WSRRServer"
        },
        "WSRRSubscription": {
            "href": "/mgmt/config/{domain}/WSRRSubscription"
        },
        "WSStylePolicy": {
            "href": "/mgmt/config/{domain}/WSStylePolicy"
        },
        "WSStylePolicyRule": {
            "href": "/mgmt/config/{domain}/WSStylePolicyRule"
        },
        "WXSGrid": {
            "href": "/mgmt/config/{domain}/WXSGrid"
        },
        "XACMLPDP": {
            "href": "/mgmt/config/{domain}/XACMLPDP"
        },
        "XC10Grid": {
            "href": "/mgmt/config/{domain}/XC10Grid"
        },
        "XMLFirewallService": {
            "href": "/mgmt/config/{domain}/XMLFirewallService"
        },
        "XMLManager": {
            "href": "/mgmt/config/{domain}/XMLManager"
        },
        "xmltrace": {
            "href": "/mgmt/config/{domain}/xmltrace"
        },
        "XPathRoutingMap": {
            "href": "/mgmt/config/{domain}/XPathRoutingMap"
        },
        "XSLCoprocService": {
            "href": "/mgmt/config/{domain}/XSLCoprocService"
        },
        "XSLProxyService": {
            "href": "/mgmt/config/{domain}/XSLProxyService"
        },
        "XTCProtocolHandler": {
            "href": "/mgmt/config/{domain}/XTCProtocolHandler"
        },
        "ZHybridTargetControlService": {
            "href": "/mgmt/config/{domain}/ZHybridTargetControlService"
        },
        "ZosNSSClient": {
            "href": "/mgmt/config/{domain}/ZosNSSClient"
        }
    }
}