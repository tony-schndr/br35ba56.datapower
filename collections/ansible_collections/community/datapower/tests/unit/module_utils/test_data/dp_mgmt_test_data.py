int_type = {
    "cli-arg": "number",
    "maximum": "0xFFFF",
    "minimum": 0,
    "name": "dmUInt16"
}

AAAPolicy_ExtractIdentity = {
    "EIBitmap": {
        "http-basic-auth": "off",
        "wssec-username": "off",
        "wssec-derived-key": "off",
        "wssec-binary-token": "off",
        "ws-secure-conversation": "off",
        "ws-trust": "off",
        "kerberos": "off",
        "kerberos-spnego": "off",
        "client-ssl": "off",
        "saml-attr-name": "off",
        "saml-authen-name": "off",
        "saml-artifact": "off",
        "client-ip-address": "off",
        "signer-dn": "off",
        "token": "off",
        "cookie-token": "off",
        "ltpa": "off",
        "metadata": "off",
        "jwt": "on",
        "custom": "off",
        "html-forms-auth": "off",
        "social-login": "off",
        "oauth": "off"
    },
    "EICustomURL": "",
    "EIXPath": "",
    "EISignerDNValcred": "",
    "EICookieName": "",
    "EIBasicAuthRealm": "login",
    "EIUseWSSec": "off",
    "EIMetadata": "",
    "EIAllowRemoteTokenReference": "off",
    "EIRemoteTokenProcessService": "",
    "EIPasswordRetrievalMechanism": "xmlfile",
    "EIPasswordRetrievalCustomURL": "",
    "EIPasswordRetrievalAAAInfoURL": "",
    "EISSLProxyProfile": "",
    "EIFormsLoginPolicy": "",
    "EIOAuthClientGroup": "",
    "EISSLClientConfigType": "proxy",
    "EISSLClientProfile": "",
    "EIJWTValidator": {
        "value": "dpEXT2dp_JWTValidator",
        "href": "/mgmt/config/Security/AAAJWTValidator/dpEXT2dp_JWTValidator"
    },
    "EISocialLoginPolicy": "",
    "EISAMLResponseValCred": ""
}

valcred_cert_is_array = {
    "CryptoValCred": {
        "CRLDPHandling": "ignore",
        "CertValidationMode": "legacy",
        "Certificate": 
        [
            {
                "value": "Test2"
            },
            {
                "value": "Test4"
            },
            {
                "value": "Test3"
            }  
        ],
        "CheckDates": "on",
        "ExplicitPolicy": "on",
        "InitialPolicySet": "2.5.29.32.0",
        "RequireCRL": "off",
        "UseCRL": "on",
        "mAdminState": "enabled",
        "name": "valcred"
    }
}

