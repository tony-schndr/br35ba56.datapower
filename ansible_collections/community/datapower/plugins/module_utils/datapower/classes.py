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
