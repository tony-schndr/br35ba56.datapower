
config_info_schema_response = {
            "children": [
                {
                    "_links": {
                        "doc": {
                            "href": "/mgmt/docs/types/dmAdminState"
                        },
                        "self": {
                            "href": "/mgmt/types/default/dmAdminState"
                        }
                    },
                    "type": {
                        "cli-arg": "enabled | disabled",
                        "name": "dmAdminState",
                        "value-list": {
                            "value": [
                                {
                                    "display": "enabled",
                                    "name": "enabled"
                                },
                                {
                                    "display": "disabled",
                                    "name": "disabled"
                                }
                            ]
                        }
                    }
                },
                {
                    "_links": {
                        "doc": {
                            "href": "/mgmt/docs/types/dmReference"
                        },
                        "self": {
                            "href": "/mgmt/types/default/dmReference"
                        }
                    },
                    "type": {
                        "cli-arg": "object",
                        "name": "dmReference"
                    }
                },
                {
                    "_links": {
                        "doc": {
                            "href": "/mgmt/docs/types/dmCryptoValCredCertValidationMode"
                        },
                        "self": {
                            "href": "/mgmt/types/default/dmCryptoValCredCertValidationMode"
                        }
                    },
                    "type": {
                        "name": "dmCryptoValCredCertValidationMode",
                        "value-list": {
                            "value": [
                                {
                                    "description": "The validation credentials contain either the exact peer certificate to match or the immediate issuer's certificate, which could be an intermediate CA or a root CA. This mode is maintained for backwards compatibility but Exact Match or PKIX are better choices in most cases.",
                                    "display": "Match exact certificate or immediate issuer",
                                    "name": "legacy"
                                },
                                {
                                    "description": "The complete certificate chain is checked from subject to root when using the validation credentials for certificate validation. Validation succeeds only if the chain ends with a root certificate in the validation credentials. Non-root certificates in the validation credentials are used as untrusted intermediate certificates. Additional untrusted intermediate certificates are obtained dynamically from the context at hand (TLS handshake messages, PKCS#7 tokens, PKIPath tokens, and so forth).",
                                    "display": "Full certificate chain checking (PKIX)",
                                    "name": "pkix"
                                },
                                {
                                    "description": "The validation credentials contain the exact peer certificate to match. This mode is useful when you want to match the peer certificate exactly, but that certificate is not necessarily a self-signed (root) certificate.",
                                    "display": "Match exact certificate",
                                    "name": "exact-match"
                                }
                            ]
                        }
                    }
                },
                {
                    "_links": {
                        "doc": {
                            "href": "/mgmt/docs/types/dmToggle"
                        },
                        "self": {
                            "href": "/mgmt/types/default/dmToggle"
                        }
                    },
                    "type": {
                        "cli-arg": "on | off",
                        "name": "dmToggle",
                        "value-list": {
                            "value": [
                                {
                                    "display": "on",
                                    "name": "on"
                                },
                                {
                                    "display": "off",
                                    "name": "off"
                                }
                            ]
                        }
                    }
                },
                {
                    "_links": {
                        "doc": {
                            "href": "/mgmt/docs/types/dmCRLDPHandling"
                        },
                        "self": {
                            "href": "/mgmt/types/default/dmCRLDPHandling"
                        }
                    },
                    "type": {
                        "display": "X.509 CRL Distribution Points Handling",
                        "name": "dmCRLDPHandling",
                        "summary": "X.509 CRL Distribution Points Handling",
                        "value-list": {
                            "value": [
                                {
                                    "description": "Ignores the certificate extension, if present.",
                                    "display": "Ignore",
                                    "name": "ignore"
                                },
                                {
                                    "description": "Requires checks against, but does not fetch, the CRLs in the X.509 CRL Distribution Point extensions. If any CRL in a CRL Distribution Point extension no longer exists in the CRL cache, the certificate validation fails.",
                                    "display": "Require",
                                    "name": "require"
                                }
                            ]
                        }
                    }
                },
                {
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
            ],
            "parent": {
                "_links": {
                    "doc": {
                        "href": "/mgmt/docs/metadata/CryptoValCred"
                    },
                    "self": {
                        "href": "/mgmt/metadata/default/CryptoValCred"
                    }
                },
                "object": {
                    "cli-alias": "valcred",
                    "cmd-group": "validation",
                    "description": "&lt;p>A validation credentials list is used to authenticate certificates that are received from TLS peers. It can also be used to validate certificates that are used in digital signature and encryption operations.&lt;/p>&lt;p>a TLS client requires a validation credentials only when it authenticates the certificate presented by the remote TLS server. The TLS standard does not require authentication of the server certificate.&lt;/p>&lt;p>a TLS server requires a validation credentials only when it authenticates remote TLS clients. The TLS standard does not require authentication of the client certificate.&lt;/p>",
                    "display": "Crypto Validation Credentials",
                    "name": "CryptoValCred",
                    "properties": {
                        "property": [
                            {
                                "cli-alias": "admin-state",
                                "default": "enabled",
                                "description": "&lt;p>The administrative state of the configuration.&lt;/p>&lt;ul>&lt;li>To make active, set to enabled.&lt;/li>&lt;li>To make inactive, set to disabled.&lt;/li>&lt;/ul>",
                                "display": "Administrative state",
                                "hoverhelp": "&lt;p>Set the administrative state of the configuration.&lt;/p>&lt;ul>&lt;li>To make active, set the check box.&lt;/li>&lt;li>To make inactive, clear the check box.&lt;/li>&lt;/ul>",
                                "label": "Enable administrative state",
                                "name": "mAdminState",
                                "summary": "Set the administrative state of this configuration.",
                                "type": {
                                    "href": "/mgmt/types/default/dmAdminState"
                                }
                            },
                            {
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
                            },
                            {
                                "cli-alias": "cert-validation-mode",
                                "default": "legacy",
                                "description": "Select the method used to perform certificate validation.",
                                "display": "Certificate Validation Mode",
                                "name": "CertValidationMode",
                                "summary": "Method to perform certificate validation",
                                "type": {
                                    "href": "/mgmt/types/default/dmCryptoValCredCertValidationMode"
                                }
                            },
                            {
                                "cli-alias": "use-crl",
                                "default": "on",
                                "description": "Select whether to check Certificate Revocation Lists (CRLs) during certificate validation. If enabled, CRLs are checked. If disabled, CRLs are not checked.",
                                "display": "Use CRL",
                                "name": "UseCRL",
                                "summary": "Whether to use CRLs during certificate validation",
                                "type": {
                                    "href": "/mgmt/types/default/dmToggle"
                                }
                            },
                            {
                                "cli-alias": "require-crl",
                                "default": "off",
                                "description": "Select whether to mandate the use of Certificate Revocation Lists (CRLs) during certificate validation. If enabled, certificate validation fails if no CRL is available. If disabled, validation succeeds independent of the availability of a CRL.",
                                "display": "Require CRL",
                                "ignored-when": {
                                    "condition": {
                                        "evaluation": "property-equals",
                                        "property-name": "UseCRL",
                                        "value": "off"
                                    }
                                },
                                "name": "RequireCRL",
                                "summary": "Whether to require CRLs during certificate validation",
                                "type": {
                                    "href": "/mgmt/types/default/dmToggle"
                                }
                            },
                            {
                                "cli-alias": "crldp",
                                "default": "ignore",
                                "description": "Select how to support certificate extensions for X.509 Certificate Distribution Points. This certificate extension specifies how to obtain CRL information. For more information about certificates, see RFC 2527 and RFC 3280.",
                                "display": "CRL Distribution Points Handling",
                                "ignored-when": {
                                    "condition": {
                                        "evaluation": "property-equals",
                                        "property-name": "UseCRL",
                                        "value": "off"
                                    }
                                },
                                "name": "CRLDPHandling",
                                "summary": "How to support Distribution Point certificate extensions",
                                "type": {
                                    "href": "/mgmt/types/default/dmCRLDPHandling"
                                }
                            },
                            {
                                "array": "true",
                                "cli-alias": "initial-policy-set",
                                "default": "2.5.29.32.0",
                                "description": "&lt;p>Specify the unique object identifiers for the certificate policy that is associated with the current validation credentials.&lt;/p>&lt;p>RFC 3280 refers to the certificate chain validation input variable as 'user-initial-policy-set'. This set of OIDs specifies the allow values of certificate policies at the end of chain processing. To use this functionality, enable 'Require Explicit Policy'. Otherwise, this set is used only if there are policy constraint extensions in the certificate chain.&lt;/p>&lt;p>By default, the initial certificate policy set consists of the anyPolicy OID (2.5.29.32.0). All members of the set are used in certificate validation as described in Section 6.1.1 of RFC 3280.&lt;/p>",
                                "display": "Initial Certificate Policy Set",
                                "ignored-when": {
                                    "condition": {
                                        "evaluation": "property-does-not-equal",
                                        "property-name": "CertValidationMode",
                                        "value": "pkix"
                                    }
                                },
                                "name": "InitialPolicySet",
                                "summary": "Certificate policy for certificate validation",
                                "type": {
                                    "href": "/mgmt/types/default/dmString"
                                }
                            },
                            {
                                "cli-alias": "explicit-policy",
                                "default": "off",
                                "description": "Support the initial-explicit-policy variable as defined by RFC 3280. If enabled, the chain validation algorithm must end with a non-empty policy tree. If disabled, the algorithm can end with an empty policy tree unless policy constraint extensions in the chain require an explicit policy.",
                                "display": "Require Explicit Certificate Policy",
                                "ignored-when": {
                                    "condition": {
                                        "evaluation": "property-does-not-equal",
                                        "property-name": "CertValidationMode",
                                        "value": "pkix"
                                    }
                                },
                                "name": "ExplicitPolicy",
                                "summary": "Require certificate policy",
                                "type": {
                                    "href": "/mgmt/types/default/dmToggle"
                                }
                            },
                            {
                                "cli-alias": "check-dates",
                                "default": "on",
                                "description": "Select whether to check the current date and time against the notBefore and the notAfter values in certificates and CRLs during certificate validation. If enabled, the date values are checked and expired certificates cause validation to fail. If disabled, the date values are ignored and the fact that a certificate is expired does not cause validation to fail.",
                                "display": "Check Dates",
                                "name": "CheckDates",
                                "summary": "Whether to check dates during certificate validation",
                                "type": {
                                    "href": "/mgmt/types/default/dmToggle"
                                }
                            }
                        ]
                    },
                    "property-group": {
                        "member": {
                            "name": "dmAdminState"
                        },
                        "name": "summary"
                    },
                    "summary": "Set of certificates for authenticating peers' certificates",
                    "uri": "crypto/valcred"
                }
            }
        }
    


valcred_schema_resp = {
    "_links": {
        "self": {
            "href": "/mgmt/metadata/default/CryptoValCred"
        },
        "doc": {
            "href": "/mgmt/docs/metadata/CryptoValCred"
        }
    },
    "object": {
        "name": "CryptoValCred",
        "uri": "crypto/valcred",
        "cli-alias": "valcred",
        "cmd-group": "validation",
        "property-group": {
            "name": "summary",
            "member": {
                "name": "dmAdminState"
            }
        },
        "display": "Crypto Validation Credentials",
        "summary": "Set of certificates for authenticating peers' certificates",
        "description": "&lt;p>A validation credentials list is used to authenticate certificates that are received from TLS peers. It can also be used to validate certificates that are used in digital signature and encryption operations.&lt;/p>&lt;p>a TLS client requires a validation credentials only when it authenticates the certificate presented by the remote TLS server. The TLS standard does not require authentication of the server certificate.&lt;/p>&lt;p>a TLS server requires a validation credentials only when it authenticates remote TLS clients. The TLS standard does not require authentication of the client certificate.&lt;/p>",
        "properties": {
            "property": [
                {
                    "name": "mAdminState",
                    "type": {
                        "href": "/mgmt/types/default/dmAdminState"
                    },
                    "cli-alias": "admin-state",
                    "default": "enabled",
                    "display": "Administrative state",
                    "summary": "Set the administrative state of this configuration.",
                    "description": "&lt;p>The administrative state of the configuration.&lt;/p>&lt;ul>&lt;li>To make active, set to enabled.&lt;/li>&lt;li>To make inactive, set to disabled.&lt;/li>&lt;/ul>",
                    "hoverhelp": "&lt;p>Set the administrative state of the configuration.&lt;/p>&lt;ul>&lt;li>To make active, set the check box.&lt;/li>&lt;li>To make inactive, clear the check box.&lt;/li>&lt;/ul>",
                    "label": "Enable administrative state"
                },
                {
                    "name": "Certificate",
                    "array": "true",
                    "type": {
                        "href": "/mgmt/types/default/dmReference",
                        "reference-to": {
                            "href": "/mgmt/metadata/default/CryptoCertificate"
                        }
                    },
                    "cli-alias": "certificate",
                    "display": "Certificates",
                    "summary": "Certificate aliases in the validation credentials list",
                    "description": "Define the certificate aliases for the validation credentials. Each certificate is the validation credentials is the certificate that a TLS peer might send or is the certificate of the Certification Authority (CA) that signed the certificate sent by a peer or is the root certificate."
                },
                {
                    "name": "CertValidationMode",
                    "type": {
                        "href": "/mgmt/types/default/dmCryptoValCredCertValidationMode"
                    },
                    "cli-alias": "cert-validation-mode",
                    "default": "legacy",
                    "display": "Certificate Validation Mode",
                    "summary": "Method to perform certificate validation",
                    "description": "Select the method used to perform certificate validation."
                },
                {
                    "name": "UseCRL",
                    "type": {
                        "href": "/mgmt/types/default/dmToggle"
                    },
                    "cli-alias": "use-crl",
                    "default": "on",
                    "display": "Use CRL",
                    "summary": "Whether to use CRLs during certificate validation",
                    "description": "Select whether to check Certificate Revocation Lists (CRLs) during certificate validation. If enabled, CRLs are checked. If disabled, CRLs are not checked."
                },
                {
                    "name": "RequireCRL",
                    "type": {
                        "href": "/mgmt/types/default/dmToggle"
                    },
                    "cli-alias": "require-crl",
                    "default": "off",
                    "ignored-when": {
                        "condition": {
                            "evaluation": "property-equals",
                            "property-name": "UseCRL",
                            "value": "off"
                        }
                    },
                    "display": "Require CRL",
                    "summary": "Whether to require CRLs during certificate validation",
                    "description": "Select whether to mandate the use of Certificate Revocation Lists (CRLs) during certificate validation. If enabled, certificate validation fails if no CRL is available. If disabled, validation succeeds independent of the availability of a CRL."
                },
                {
                    "name": "CRLDPHandling",
                    "type": {
                        "href": "/mgmt/types/default/dmCRLDPHandling"
                    },
                    "cli-alias": "crldp",
                    "default": "ignore",
                    "ignored-when": {
                        "condition": {
                            "evaluation": "property-equals",
                            "property-name": "UseCRL",
                            "value": "off"
                        }
                    },
                    "display": "CRL Distribution Points Handling",
                    "summary": "How to support Distribution Point certificate extensions",
                    "description": "Select how to support certificate extensions for X.509 Certificate Distribution Points. This certificate extension specifies how to obtain CRL information. For more information about certificates, see RFC 2527 and RFC 3280."
                },
                {
                    "name": "InitialPolicySet",
                    "array": "true",
                    "type": {
                        "href": "/mgmt/types/default/dmString"
                    },
                    "cli-alias": "initial-policy-set",
                    "default": "2.5.29.32.0",
                    "ignored-when": {
                        "condition": {
                            "evaluation": "property-does-not-equal",
                            "property-name": "CertValidationMode",
                            "value": "pkix"
                        }
                    },
                    "display": "Initial Certificate Policy Set",
                    "summary": "Certificate policy for certificate validation",
                    "description": "&lt;p>Specify the unique object identifiers for the certificate policy that is associated with the current validation credentials.&lt;/p>&lt;p>RFC 3280 refers to the certificate chain validation input variable as 'user-initial-policy-set'. This set of OIDs specifies the allow values of certificate policies at the end of chain processing. To use this functionality, enable 'Require Explicit Policy'. Otherwise, this set is used only if there are policy constraint extensions in the certificate chain.&lt;/p>&lt;p>By default, the initial certificate policy set consists of the anyPolicy OID (2.5.29.32.0). All members of the set are used in certificate validation as described in Section 6.1.1 of RFC 3280.&lt;/p>"
                },
                {
                    "name": "ExplicitPolicy",
                    "type": {
                        "href": "/mgmt/types/default/dmToggle"
                    },
                    "cli-alias": "explicit-policy",
                    "default": "off",
                    "ignored-when": {
                        "condition": {
                            "evaluation": "property-does-not-equal",
                            "property-name": "CertValidationMode",
                            "value": "pkix"
                        }
                    },
                    "display": "Require Explicit Certificate Policy",
                    "summary": "Require certificate policy",
                    "description": "Support the initial-explicit-policy variable as defined by RFC 3280. If enabled, the chain validation algorithm must end with a non-empty policy tree. If disabled, the algorithm can end with an empty policy tree unless policy constraint extensions in the chain require an explicit policy."
                },
                {
                    "name": "CheckDates",
                    "type": {
                        "href": "/mgmt/types/default/dmToggle"
                    },
                    "cli-alias": "check-dates",
                    "default": "on",
                    "display": "Check Dates",
                    "summary": "Whether to check dates during certificate validation",
                    "description": "Select whether to check the current date and time against the notBefore and the notAfter values in certificates and CRLs during certificate validation. If enabled, the date values are checked and expired certificates cause validation to fail. If disabled, the date values are ignored and the fact that a certificate is expired does not cause validation to fail."
                }
            ]
        }
    }
}