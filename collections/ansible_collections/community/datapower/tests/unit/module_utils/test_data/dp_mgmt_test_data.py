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

schema_ethernet_interface = {
    "types": [
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
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmIPConfigMode"
                },
                "self": {
                    "href": "/mgmt/types/default/dmIPConfigMode"
                }
            },
            "type": {
                "name": "dmIPConfigMode",
                "value-list": {
                    "value": [
                        {
                            "description": "The configuration is static. Manually define the required properties.",
                            "display": "Static",
                            "name": "static",
                            "summary": "Use a static configuration"
                        },
                        {
                            "description": "The configuration uses IPv4 autoconfiguration with DHCP.",
                            "display": "DHCP",
                            "name": "dhcp",
                            "summary": "Use IPv4 autoconfiguration with DHCP"
                        },
                        {
                            "description": "The configuration uses IPv6 autoconfiguration with SLAAC.",
                            "display": "SLAAC",
                            "name": "slaac",
                            "summary": "Use IPv6 autoconfiguration with SLAAC"
                        }
                    ]
                }
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmIPNetAddress"
                },
                "self": {
                    "href": "/mgmt/types/default/dmIPNetAddress"
                }
            },
            "type": {
                "cli-arg": "dotted-ip/mask",
                "format": "(a.b.c.d/e)",
                "name": "dmIPNetAddress"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmIPHostAddress"
                },
                "self": {
                    "href": "/mgmt/types/default/dmIPHostAddress"
                }
            },
            "type": {
                "cli-arg": "dotted-ip",
                "format": "(a.b.c.d)",
                "name": "dmIPHostAddress"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmStaticRoute"
                },
                "self": {
                    "href": "/mgmt/types/default/dmStaticRoute"
                }
            },
            "type": {
                "name": "dmStaticRoute",
                "properties": {
                    "property": [
                        {
                            "description": "&lt;p>Specify the IP address and netmask for each destination network address. The netmask is in CIDR format is the integer that specifies the prefix length.&lt;/p>&lt;ul>&lt;li>For IPv4, the prefix length can be in the range 0 - 32.&lt;/li>&lt;li>For IPv6, the prefix length can be in the range 0 - 128.&lt;/li>&lt;/ul>",
                            "display": "Destination",
                            "name": "Destination",
                            "required": "true",
                            "summary": "IP address and netmask",
                            "type": {
                                "href": "/mgmt/types/default/dmIPNetAddress"
                            }
                        },
                        {
                            "description": "Specify the IP address of the next-hop router.",
                            "display": "Next-hop router",
                            "name": "Gateway",
                            "required": "true",
                            "summary": "IP address of next-hop router",
                            "type": {
                                "href": "/mgmt/types/default/dmIPHostAddress"
                            }
                        },
                        {
                            "default": 0,
                            "description": "&lt;p>Optionally specify the preference for the route. The lesser the value, the greater the preference. For each IP family, the supported range differs.&lt;/p>&lt;ul>&lt;li>For IPv4, enter a value in the range 0 - 255. The default value is 0.&lt;/li>&lt;li>For IPv6, enter a value in the range 0 - 65536. The default value is 512.&lt;/li>&lt;/ul>",
                            "display": "Metric",
                            "maximum": 65536,
                            "minimum": 0,
                            "name": "Metric",
                            "summary": "Preference for the route",
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            }
                        }
                    ]
                }
            }
        },
        {
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
                    "href": "/mgmt/docs/types/dmUInt64"
                },
                "self": {
                    "href": "/mgmt/types/default/dmUInt64"
                }
            },
            "type": {
                "cli-arg": "number",
                "maximum": "0xFFFFFFFFFFFFFFFF",
                "minimum": 0,
                "name": "dmUInt64"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmTimeInterval"
                },
                "self": {
                    "href": "/mgmt/types/default/dmTimeInterval"
                }
            },
            "type": {
                "cli-arg": "seconds",
                "maximum": "0xFFFFFFFF",
                "minimum": 0,
                "name": "dmTimeInterval"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmLVSDistributionAlgorithm"
                },
                "self": {
                    "href": "/mgmt/types/default/dmLVSDistributionAlgorithm"
                }
            },
            "type": {
                "display": "Distribution algorithm",
                "name": "dmLVSDistributionAlgorithm",
                "summary": "Distribution algorithm",
                "value-list": {
                    "value": [
                        {
                            "description": "The weighted least connection algorithm uses an internal CPU-based weight with the number of current connections to each member to distribute incoming connections among available member. A member receives a new connection that is based on a combination of its weight (or preference) and its number of active connections. The algorithm attempts to balance the connection completion rate across members so that each member has the same number of active connections.",
                            "display": "Weighted least connections",
                            "name": "wlc",
                            "summary": "Weighted least connections algorithm"
                        },
                        {
                            "description": "The round robin algorithm maintains a list of members and evenly distributes incoming connections among available members. The algorithm attempts to balance the incoming connection rate across members.",
                            "display": "Round robin",
                            "name": "rr",
                            "summary": "Round robin algorithm"
                        }
                    ]
                }
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmMACAddress"
                },
                "self": {
                    "href": "/mgmt/types/default/dmMACAddress"
                }
            },
            "type": {
                "cli-arg": "MAC a:b:c:d:e:f",
                "format": "(a:b:c:d:e:f)",
                "name": "dmMACAddress"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmEthernetMode"
                },
                "self": {
                    "href": "/mgmt/types/default/dmEthernetMode"
                }
            },
            "type": {
                "display": "Ethernet port mode",
                "name": "dmEthernetMode",
                "summary": "Ethernet port mode",
                "value-list": {
                    "value": [
                        {
                            "description": "For interfaces that do autonegotiation, performs standard IEEE 802.3 autonegotiation for interface speed and direction. Preference is given to the highest speed. Preference is for full-duplex over half-duplex.",
                            "display": "Auto",
                            "name": "Auto",
                            "summary": "Auto"
                        },
                        {
                            "description": "Advertises 10000BASE-T PHY (10 Gbps) in full-duplex mode.",
                            "display": "10000baseTx-FD",
                            "name": "10000baseTx-FD",
                            "summary": "10000baseTx-FD"
                        },
                        {
                            "description": "Advertises 1000BASE-T PHY (1 Gbps) in full-duplex mode.",
                            "display": "1000baseTx-FD",
                            "name": "1000baseTx-FD",
                            "summary": "1000baseTx-FD"
                        },
                        {
                            "description": "Advertises 100BASE-TX PHY (100 Mbps) in full-duplex mode.",
                            "display": "100baseTx-FD",
                            "name": "100baseTx-FD",
                            "summary": "100baseTx-FD"
                        },
                        {
                            "description": "Advertises 100BASE-TX PHY (100 Mbps) in half-duplex mode.",
                            "display": "100baseTx-HD",
                            "name": "100baseTx-HD",
                            "summary": "100baseTx-HD"
                        },
                        {
                            "description": "Advertises 10BASE-T PHY (10 Mbps) in full-duplex mode.",
                            "display": "10baseT-FD",
                            "name": "10baseT-FD",
                            "summary": "10baseT-FD"
                        },
                        {
                            "description": "Advertises 10BASE-T PHY (10 Mbps) in half-duplex mode.",
                            "display": "10baseT-HD",
                            "name": "10baseT-HD",
                            "summary": "10baseT-HD"
                        }
                    ]
                }
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmEthernetFCMode"
                },
                "self": {
                    "href": "/mgmt/types/default/dmEthernetFCMode"
                }
            },
            "type": {
                "display": "Ethernet Flow Control Mode",
                "name": "dmEthernetFCMode",
                "summary": "Ethernet Flow Control Mode",
                "value-list": {
                    "value": [
                        {
                            "description": "For interfaces that support autonegotiation, performs standard IEEE 802.3 autonegotiation for flow control.",
                            "display": "Auto",
                            "name": "auto",
                            "summary": "Auto"
                        },
                        {
                            "description": "Disables flow control. The interface does not send flow control PAUSE frames and ignores received PAUSE frames. Use this value only when IBM support diagnosed that you are encountering a problem.",
                            "display": "Disabled",
                            "name": "disabled",
                            "summary": "Disabled"
                        }
                    ]
                }
            }
        }
    ],
    "metadata": {
        "_links": {
            "doc": {
                "href": "/mgmt/docs/metadata/EthernetInterface"
            },
            "self": {
                "href": "/mgmt/metadata/default/EthernetInterface"
            }
        },
        "object": {
            "actions": {
                "action": [
                    {
                        "name": "Ping",
                        "parameters": {
                            "parameter": {
                                "name": "RemoteHost",
                                "select": "DefaultGateway"
                            }
                        }
                    },
                    {
                        "name": "Ping",
                        "parameters": {
                            "parameter": {
                                "name": "RemoteHost",
                                "select": "DefaultIPv6Gateway"
                            }
                        }
                    },
                    {
                        "display": "Start packet capture",
                        "name": "PacketCapture",
                        "parameters": {
                            "parameter": {
                                "name": "Interface",
                                "select": "dmObjectName"
                            }
                        }
                    },
                    {
                        "display": "Stop packet capture",
                        "name": "StopPacketCapture",
                        "parameters": {
                            "parameter": {
                                "name": "Interface",
                                "select": "dmObjectName"
                            }
                        }
                    },
                    {
                        "display": "Disable hardware offload",
                        "name": "DisableEthernetHardwareOffload",
                        "parameters": {
                            "parameter": {
                                "name": "Interface",
                                "select": "dmObjectName"
                            }
                        }
                    },
                    {
                        "display": "Yield standby",
                        "name": "YieldEthernetStandby",
                        "parameters": {
                            "parameter": {
                                "name": "Interface",
                                "select": "dmObjectName"
                            }
                        }
                    }
                ]
            },
            "cli-alias": "ethernet",
            "cmd-group": "interface",
            "description": "Configure and manage Ethernet interfaces.",
            "display": "Ethernet Interface",
            "name": "EthernetInterface",
            "platforms": {
                "platform": [
                    "container",
                    "software"
                ]
            },
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
                        "cli-alias": "summary",
                        "description": "A descriptive summary for the configuration.",
                        "display": "Comments",
                        "name": "UserSummary",
                        "summary": "Enter a descriptive summary for the configuration.",
                        "type": {
                            "href": "/mgmt/types/default/dmString"
                        }
                    },
                    {
                        "cli-alias": "ip-config-mode",
                        "default": "static",
                        "description": "&lt;p>The configuration mode of the interface. Although you can set multiple modes, only one mode is supported.&lt;/p>&lt;ul>&lt;li>With static configuration, you must define the configuration for the physical interface. &lt;ul>&lt;li>Assign the primary network address.&lt;/li>&lt;li>Manage secondary, or auxiliary, network addresses.&lt;/li>&lt;li>Assign the default IPv4 gateway.&lt;/li>&lt;li>Assign the default IPv6 gateway, if you define IPv6 IP addresses.&lt;/li>&lt;li>Manage static routes in the routing table.&lt;/li>&lt;/ul>&lt;/li>&lt;li>With DHCP autoconfiguration, the appliance ignores configuration data about the physical interface.&lt;/li>&lt;li>With SLAAC autoconfiguration, the appliance ignores configuration data about the physical interface.&lt;/li>&lt;/ul>",
                        "display": "IP address configuration mode",
                        "hoverhelp": "&lt;p>Set the configuration mode for the interface. Although you can set multiple modes, only one mode is supported.&lt;/p>&lt;ul>&lt;li>With static configuration, you must define the configuration for the physical interface.&lt;/li>&lt;li>With DHCP autoconfiguration, the appliance ignores configuration data about the physical interface.&lt;/li>&lt;li>With SLAAC autoconfiguration, the appliance ignores configuration data about the physical interface.&lt;/li>&lt;/ul>",
                        "ignored-when": {
                            "condition": {
                                "condition": {
                                    "evaluation": "property-equals",
                                    "property-name": "LinkAggMode",
                                    "value": "on"
                                },
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "IPConfigMode",
                        "summary": "Set the configuration mode for the interface.",
                        "type": {
                            "href": "/mgmt/types/default/dmIPConfigMode"
                        }
                    },
                    {
                        "cli-alias": "ip-address",
                        "description": "&lt;p>The IP address and netmask of the primary IP address. Specify the netmask with CIDR notation.&lt;/p>&lt;ul>&lt;li>For IPv4, the prefix length can be in the range 0 - 32.&lt;/li>&lt;li>For IPv6, the prefix length can be in the range 0 - 128.&lt;/li>&lt;/ul>",
                        "display": "Primary IP Address",
                        "hoverhelp": "&lt;p>Set the IP address and netmask of the primary IP address. Specify the netmask with CIDR notation.&lt;/p>&lt;ul>&lt;li>For IPv4, the prefix length can be in the range 0 - 32.&lt;/li>&lt;li>For IPv6, the prefix length can be in the range 0 - 128.&lt;/li>&lt;/ul>",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "IPAddress",
                        "summary": "Set the primary IP address and netmask.",
                        "type": {
                            "href": "/mgmt/types/default/dmIPNetAddress"
                        }
                    },
                    {
                        "cli-alias": "ipv4-default-gateway",
                        "description": "The IPv4 address for the default IPv4 gateway. All IPv4 network addresses use this gateway.",
                        "display": "Default IPv4 gateway",
                        "hoverhelp": "Set the IPv4 address for the default IPv4 gateway. All IPv4 network addresses use this gateway.",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "DefaultGateway",
                        "summary": "Set the IPv4 address for the default IPv4 gateway.",
                        "type": {
                            "href": "/mgmt/types/default/dmIPHostAddress"
                        }
                    },
                    {
                        "cli-alias": "ipv6-default-gateway",
                        "description": "The IPv6 address for the default IPv6 gateway. All IPv6 network addresses use this gateway. If you do not use IPv6 network addresses, do not define this property.",
                        "display": "Default IPv6 gateway",
                        "hoverhelp": "Set the IPv6 address for the default IPv6 gateway. All IPv6 network addresses use this gateway.",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "DefaultIPv6Gateway",
                        "summary": "Set the IPv6 address for the default IPv6 gateway.",
                        "type": {
                            "href": "/mgmt/types/default/dmIPHostAddress"
                        }
                    },
                    {
                        "array": "true",
                        "cli-alias": "ip-secondary-address",
                        "description": "&lt;p>The IP addresses and netmasks of secondary IP addresses. Specify the netmask with CIDR notation.&lt;/p>&lt;ul>&lt;li>For IPv4, the prefix length can be in the range 0 - 32.&lt;/li>&lt;li>For IPv6, the prefix length can be in the range 0 - 128.&lt;/li>&lt;/ul>",
                        "display": "Secondary Addresses",
                        "hoverhelp": "&lt;p>Set the IP address and netmask of the secondary IP address. Specify the netmask with CIDR notation.&lt;/p>&lt;ul>&lt;li>For IPv4, the prefix length can be in the range 0 - 32.&lt;/li>&lt;li>For IPv6, the prefix length can be in the range 0 - 128.&lt;/li>&lt;/ul>",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "SecondaryAddress",
                        "summary": "Set secondary IP addresses and netmasks.",
                        "type": {
                            "href": "/mgmt/types/default/dmIPNetAddress"
                        }
                    },
                    {
                        "array": "true",
                        "cli-alias": "ip-route",
                        "description": "The static routes in the routing table. Add a static route to a remote IP prefix through a router connected to this network. When the appliance connects to a remote address, the static route with the longest prefix match is used. If multiple routes have the same prefix match, the static route with the lowest metric is used. If the metric is the same, the static route is chosen randomly.",
                        "display": "Static routes",
                        "hoverhelp": "Manage the static routes in the routing table. Add a static route to a remote IP prefix through a router connected to this network.",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "StaticRoutes",
                        "summary": "Manage the static routes in the routing table.",
                        "type": {
                            "href": "/mgmt/types/default/dmStaticRoute"
                        }
                    },
                    {
                        "cli-alias": "ipv6-dadtransmits",
                        "default": 1,
                        "description": "The number of IPv6 duplication address detection (DAD) attempts. The default value is 1.",
                        "display": "IPv6 DAD attempts",
                        "ignored-when": {
                            "condition": {
                                "evaluation": "property-equals",
                                "property-name": "LinkAggMode",
                                "value": "on"
                            }
                        },
                        "maximum": 3,
                        "minimum": 1,
                        "name": "DADTransmits",
                        "summary": "Set the number of IPv6 duplication address detection attempts.",
                        "type": {
                            "href": "/mgmt/types/default/dmUInt32"
                        }
                    },
                    {
                        "cli-alias": "ipv6-nd-retransmit-timer",
                        "default": 1000,
                        "description": "The delay between IPv6 Neighbor Discovery (ND) attempts. The default value is 1000. This property affects duplication address detection (DAD) and other ND operations.",
                        "display": "IPv6 neighbor discovery delay",
                        "hoverhelp": "Set the delay between IPv6 Neighbor Discovery (ND) attempts. This property affects duplication address detection (DAD) and other ND operations.",
                        "ignored-when": {
                            "condition": {
                                "evaluation": "property-equals",
                                "property-name": "LinkAggMode",
                                "value": "on"
                            }
                        },
                        "maximum": 3000,
                        "minimum": 100,
                        "name": "DADRetransmitTimer",
                        "summary": "Set the delay between IPv6 neighbor discovery (ND) attempts.",
                        "type": {
                            "href": "/mgmt/types/default/dmUInt32"
                        },
                        "units": "Milliseconds"
                    },
                    {
                        "cli-alias": "standby-enable",
                        "default": "off",
                        "description": "&lt;p>Whether to allow a standby configuration. The standby configuration defines the policies for the group that this interface is a member. A standby group is the collection of interfaces on different appliances in the multicast domain that share the responsibility for one virtual IP address. When at least one member of a standby group can reach the multicast domain, the virtual IP group receives the traffic.&lt;/p>&lt;p>&lt;b>Attention:&lt;/b> Virtual IP addresses in a standby configuration must be IPv4 addresses.&lt;/p>",
                        "display": "Enable standby control",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "StandbyControl",
                        "summary": "Indicate whether to allow a standby configuration.",
                        "type": {
                            "href": "/mgmt/types/default/dmToggle"
                        }
                    },
                    {
                        "cli-alias": "standby-group",
                        "default": 1,
                        "description": "&lt;p>The number of the standby group in a multicast domain. The multicast domain is a group of interfaces that receive traffic from each other on the IP address 224.0.0.2 (the all-routers IP multicast group). If the multicast domain becomes partitioned, which is an unusual situation, a member in each partition becomes the active member to handle connections in its partition.&lt;/p>&lt;p>&lt;b>Attention:&lt;/b> Do not use a group number that conflicts with the number of an existing standby group or any network group that uses Hot Standby Router Protocol (HSRP).&lt;/p>&lt;p>The interfaces of a standby group are on the same network segment and share the responsibility for one virtual IP address. Interfaces in the standby group require the following configuration.&lt;/p>&lt;ul>&lt;li>Belong to the same group.&lt;/li>&lt;li>Use the same primary virtual IP address.&lt;/li>&lt;li>Use the same authentication, or security token.&lt;/li>&lt;/ul>",
                        "display": "Group number",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "off"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "maximum": 255,
                        "minimum": 1,
                        "name": "Group",
                        "required-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "on"
                                    },
                                    {
                                        "evaluation": "property-value-not-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "off"
                                    }
                                ],
                                "evaluation": "logical-and"
                            }
                        },
                        "summary": "Set the number of the standby group in the multicast domain.",
                        "type": {
                            "href": "/mgmt/types/default/dmUInt32"
                        }
                    },
                    {
                        "cli-alias": "standby-virtual-ip",
                        "description": "&lt;p>The primary virtual IP address of the standby group. The active member of the standby group uses this IP address. All interfaces in the standby group must use the same virtual IP address. External clients that contact the active member of the standby group should use this IP address.&lt;/p>&lt;p>&lt;b>Attention:&lt;/b> Virtual IP addresses in a standby configuration must be IPv4 addresses.&lt;/p>",
                        "display": "Primary virtual IP address",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "off"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "VirtualIP",
                        "required-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "on"
                                    },
                                    {
                                        "evaluation": "property-value-not-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "off"
                                    }
                                ],
                                "evaluation": "logical-and"
                            }
                        },
                        "summary": "Set the primary virtual IP address of standby group.",
                        "type": {
                            "href": "/mgmt/types/default/dmIPHostAddress"
                        }
                    },
                    {
                        "array": "true",
                        "cli-alias": "standby-secondary-virtual-ip",
                        "description": "&lt;p>Auxiliary, or secondary, virtual IP addresses to the standby configuration. Secondary addresses follow the active virtual IP address to the active interface. Secondary addresses are on the same interface as the primary address and are enabled and disabled in coordination with the primary address.&lt;/p>&lt;p>&lt;b>Attention:&lt;/b> Virtual IP addresses in a standby configuration must be IPv4 addresses.&lt;/p>",
                        "display": "Secondary virtual IP addresses",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "off"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "SecondaryVirtualIP",
                        "summary": "Manage secondary virtual IP addresses that follow the active virtual IP address to the active interface.",
                        "type": {
                            "href": "/mgmt/types/default/dmIPHostAddress"
                        }
                    },
                    {
                        "cli-alias": "standby-preempt",
                        "default": "off",
                        "description": "&lt;p>Whether to support preemption in the standby configuration for the initially active interface. Depending on the preemption setting, the follow activity occurs when the initially active member returns to service after a failure.&lt;/p>&lt;ul>&lt;li>When preemption is enabled, the interface resumes its active role. The standby interface becomes a passive member.&lt;/li>&lt;li>When preemption is disabled, the interface is a passive member.&lt;/li>&lt;/ul>&lt;p>&lt;b>Attention:&lt;/b> Do not enable preemption.&lt;/p>",
                        "display": "Enable preemption",
                        "hoverhelp": "&lt;p>Indicates whether to support preemption in the standby group. &lt;b>Attention:&lt;/b> Do not enable preemption.&lt;/p>",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "off"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "Preempt",
                        "required-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "on"
                                    },
                                    {
                                        "evaluation": "property-value-not-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "off"
                                    }
                                ],
                                "evaluation": "logical-and"
                            }
                        },
                        "summary": "Indicates whether to support preemption in the standby group.",
                        "type": {
                            "href": "/mgmt/types/default/dmToggle"
                        }
                    },
                    {
                        "cli-alias": "standby-priority",
                        "default": 100,
                        "description": "&lt;p>The priority of the interface in the standby group. Enter a value in the range 0 - 255. The default value is 100. Use the default value unless one system or interface is in some way better than another one.&lt;/p>&lt;p>For each standby group, there is one active member and one or more passive members. The interface with the highest priority seeks to be the active member. If multiple interfaces have the same priority, one becomes the active member.&lt;/p>",
                        "display": "Priority",
                        "hoverhelp": "Set the priority of the interface in the standby group. Enter a value in the range 0 - 255. Use the default value unless one system or interface is in some way better than another one.",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "off"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "maximum": 255,
                        "minimum": 0,
                        "name": "Priority",
                        "required-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "on"
                                    },
                                    {
                                        "evaluation": "property-value-not-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "off"
                                    }
                                ],
                                "evaluation": "logical-and"
                            }
                        },
                        "summary": "Set the priority of the interface in the standby group.",
                        "type": {
                            "href": "/mgmt/types/default/dmUInt32"
                        }
                    },
                    {
                        "cli-alias": "standby-self-balance",
                        "default": "off",
                        "description": "&lt;p>Whether to use self-balancing in the standby group.&lt;/p>&lt;ul>&lt;li>When enabled, the active member distributes connections to available members.&lt;/li>&lt;li>When disabled, all connections go to the active member. The active member receives all TCP connections and processes all requests and responses. If the active member becomes unavailable, the standby member becomes the active members.&lt;/li>&lt;/ul>&lt;p>The active member manages all TCP connections to virtual IP addresses. When a client initiates a new TCP connection, the active member selects a member to act as the connection endpoint. The active member tracks member capabilities to distribute traffic appropriately. The selected member completes the establishment of the connection. The active member forwards all segments of the TCP connection to the member that is acting as the connection endpoint.&lt;/p>&lt;ul>&lt;li>In a non-graceful transition, if the active member becomes unavailable, the passive member with the next highest priority becomes the active member. The active member might become unavailable because of network issues, an appliance crash, power outage, or similar cause.&lt;/li>&lt;li>In a graceful transition, such as for scheduled maintenance, most connections can be preserved if the appliance that terminates the connection remains available. In practice, quiesce the active appliance to ensure that established connections complete before you start maintenance; for example, apply firmware. In some environments, the time for the takeover exceeds the client timeout value. Similarly, if the appliance timeout value is aggressive, connections can be lost because the appliance terminated the connection because of a timeout.&lt;/li>&lt;/ul>",
                        "display": "Enable self-balancing",
                        "hoverhelp": "&lt;p>Indicates whether to use self-balancing in the standby group.&lt;/p>&lt;ul>&lt;li>When enabled, the active member distributes connections to available members.&lt;/li>&lt;li>When disabled, all connections go to the active member. The active member receives all TCP connections and processes all requests and responses. If the active member becomes unavailable, the standby member becomes the active members.&lt;/li>&lt;/ul>",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "off"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "SelfBalance",
                        "required-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "on"
                                    },
                                    {
                                        "evaluation": "property-value-not-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "off"
                                    }
                                ],
                                "evaluation": "logical-and"
                            }
                        },
                        "summary": "Indicates whether to use self-balancing in the standby group.",
                        "type": {
                            "href": "/mgmt/types/default/dmToggle"
                        }
                    },
                    {
                        "cli-alias": "standby-authentication",
                        "default": "0x5841333500000000",
                        "description": "The authentication string, or security token in hex. The default value is 0x5841333500000000. Every member in the standby group must use the same security token.",
                        "display": "Authentication data",
                        "hoverhelp": "Set the authentication string, or security token in hex. Every member in the standby group must use the same security token.",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "off"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "Authentication",
                        "required-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "on"
                                    },
                                    {
                                        "evaluation": "property-value-not-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "off"
                                    }
                                ],
                                "evaluation": "logical-and"
                            }
                        },
                        "summary": "Set the authentication string for the interface in the standby group.",
                        "type": {
                            "href": "/mgmt/types/default/dmUInt64"
                        }
                    },
                    {
                        "cli-alias": "standby-hello-timer",
                        "default": 3,
                        "description": "The frequency to broadcast hello messages. Set this value to at least one third the duration of the hold timer. Enter a value in the range 2 - 40. The default value is 3.",
                        "display": "Hello timer",
                        "hoverhelp": "Set the frequency to broadcast hello messages. Set this value to at least one third the duration of the hold timer. Enter a value in the range 2 - 40.",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "off"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "maximum": 40,
                        "minimum": 2,
                        "name": "HelloTimer",
                        "required-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "on"
                                    },
                                    {
                                        "evaluation": "property-value-not-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "off"
                                    }
                                ],
                                "evaluation": "logical-and"
                            }
                        },
                        "summary": "Set the frequency to broadcast hello messages",
                        "type": {
                            "href": "/mgmt/types/default/dmTimeInterval"
                        },
                        "units": "Seconds"
                    },
                    {
                        "cli-alias": "standby-hold-timer",
                        "default": 10,
                        "description": "The duration to wait before the standby member attempts a failover. Set this value to at least three times the interval of hello messages. Enter a value in the range 6 - 120. The default value is 10.",
                        "display": "Hold timer",
                        "hoverhelp": "Set the duration to wait before the standby member attempts a failover. Set this value to at least three times the interval of hello messages. Enter a value in the range 6 - 120.",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "off"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "maximum": 120,
                        "minimum": 6,
                        "name": "HoldTimer",
                        "required-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "on"
                                    },
                                    {
                                        "evaluation": "property-value-not-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "off"
                                    }
                                ],
                                "evaluation": "logical-and"
                            }
                        },
                        "summary": "Set the duration to wait before the standby member attempts a failover.",
                        "type": {
                            "href": "/mgmt/types/default/dmTimeInterval"
                        },
                        "units": "Seconds"
                    },
                    {
                        "cli-alias": "standby-distribution-algorithm",
                        "default": "wlc",
                        "description": "The algorithm to distribute incoming connections to available members when self-balancing is enabled.",
                        "display": "Distribution algorithm",
                        "ignored-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "off"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "on"
                                    }
                                ],
                                "evaluation": "logical-or"
                            }
                        },
                        "name": "DistAlg",
                        "required-when": {
                            "condition": {
                                "condition": [
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "StandbyControl",
                                        "value": "on"
                                    },
                                    {
                                        "evaluation": "property-value-in-list",
                                        "property-name": "SelfBalance",
                                        "value": "on"
                                    },
                                    {
                                        "evaluation": "property-value-not-in-list",
                                        "property-name": "IPConfigMode",
                                        "value": [
                                            "dhcp",
                                            "slaac"
                                        ]
                                    },
                                    {
                                        "evaluation": "property-equals",
                                        "property-name": "LinkAggMode",
                                        "value": "off"
                                    }
                                ],
                                "evaluation": "logical-and"
                            }
                        },
                        "summary": "Set the distribution algorithm for incoming connections when self-balancing is enabled.",
                        "type": {
                            "href": "/mgmt/types/default/dmLVSDistributionAlgorithm"
                        }
                    },
                    {
                        "cli-alias": "link-aggregation-mode",
                        "default": "off",
                        "description": "Whether the interface is part of a link aggregation interface. When part of a link aggregation interface, the appliance ignores configuration data about the physical interface.",
                        "display": "Enable for link aggregation",
                        "hoverhelp": "Indicate whether the interface is part of a link aggregation interface. When part of a link aggregation interface, the appliance ignores configuration data about the physical interface.",
                        "name": "LinkAggMode",
                        "summary": "Indicate whether the interface is part of a link aggregation interface.",
                        "type": {
                            "href": "/mgmt/types/default/dmToggle"
                        }
                    },
                    {
                        "cli-alias": "mtu",
                        "default": 1500,
                        "description": "&lt;p>The maximum transmission unit (MTU) for the Ethernet interface. The MTU is determined regardless of the length of the layer 2 encapsulation. Set the value greater than 1500 bytes only when you know that all other interfaces on this network are similarly configured. Enter a value in the range 576 - 16128. The default value is 1500.&lt;/p>&lt;ul>&lt;li>When the Ethernet interface is part of a VLAN interface, the MTU of the VLAN interface cannot be greater than the MTU for the Ethernet interface The appliance adds 4 bytes when a VLAN interface is enabled on this interface.&lt;/li>&lt;li>When the Ethernet interface is part of a link aggregation interface, the MTU of the aggregate interface overrides the MTU of the Ethernet interface.&lt;/li>&lt;/ul>",
                        "display": "MTU",
                        "hoverhelp": "Set the maximum transmission unit for the Ethernet interface. Set the value to greater than 1500 bytes only when you know that all other interfaces on this network are similarly configured. Enter a value in the range 576 - 16128.",
                        "maximum": 16128,
                        "minimum": 576,
                        "name": "MTU",
                        "summary": "Set the maximum transmission unit for the Ethernet interface.",
                        "type": {
                            "href": "/mgmt/types/default/dmUInt32"
                        },
                        "units": "Bytes"
                    },
                    {
                        "cli-alias": "mac-address",
                        "description": "The MAC address of the Ethernet interface. By default, the appliance uses the burned-in MAC address from the network interface controller that was assigned when the system was manufactured. Enter a 48-bit hex MAC address in the 00:12:34:56:78:9c format. The value must be a unicast address, where the first byte must be even.",
                        "display": "MAC address",
                        "hoverhelp": "Override the assigned 48-bit MAC address. By default, the appliance uses the burned-in MAC address from the network interface controller. Enter a 48-bit hex MAC address in the 00:12:34:56:78:9c format. The value must be a unicast address, where the first byte must be even.",
                        "name": "MACAddress",
                        "summary": "Override the assigned 48-bit MAC address.",
                        "type": {
                            "href": "/mgmt/types/default/dmMACAddress"
                        },
                        "valid-regexp": "^[0-9a-fA-F]{0,1}[02468aceACE]:[0-9a-fA-F]{0,2}:[0-9a-fA-F]{0,2}:[0-9a-fA-F]{0,2}:[0-9a-fA-F]{0,2}:[0-9a-fA-F]{0,2}$"
                    },
                    {
                        "cli-alias": "mode",
                        "default": "Auto",
                        "description": "The phyical mode is the interface speed and direction of the Ethernet unshielded twisted pair physical (PHY) layer. Use this property to set speed and direction explicitly when your networking equipment does not negotiate properly. If you manually configure one end of the link, you must manually configure the other end of the link to the same setting.",
                        "display": "Physical mode",
                        "hoverhelp": "Set the Ethernet physical mode. Use this property to set speed and direction explicitly when your networking equipment does not negotiate properly.",
                        "name": "Mode",
                        "summary": "Set the Ethernet physical mode.",
                        "type": {
                            "href": "/mgmt/types/default/dmEthernetMode"
                        }
                    },
                    {
                        "cli-alias": "force-mode",
                        "default": "off",
                        "description": "Whether to force Ethernet physical mode instead of autonegotiation behavior. By default, this option is disabled, which means that autonegotiation is used. When this option is enabled, the physical mode is forced, and there is no autonegotiation performed at the Ethernet driver level. Enable this option only when IBM Support diagnoses that you are encountering a problem.",
                        "display": "Force physical mode",
                        "hoverhelp": "Indicate whether to force Ethernet physical mode instead of autonegotiation behavior. Enable this option only when IBM Support diagnoses that you are encountering a problem.",
                        "ignored-when": {
                            "condition": {
                                "evaluation": "property-equals",
                                "property-name": "Mode",
                                "value": "Auto"
                            }
                        },
                        "name": "ForceMode",
                        "summary": "Indicate whether to force Ethernet physical mode instead of autonegotiation behavior.",
                        "type": {
                            "href": "/mgmt/types/default/dmToggle"
                        }
                    },
                    {
                        "cli-alias": "hardware-offload",
                        "default": "on",
                        "description": "&lt;p>Whether to offload TCP/IP packet processing. By default, offloading is enabled.&lt;/p>&lt;ul>&lt;li>When enabled, offloads TCP/IP packet processing of Ethernet device drivers and chips. Hardware offload can improve performance.&lt;/li>&lt;li>When disabled, does not offload TCP/IP packet processing. Disable this option only when IBM Support diagnoses that you are encountering a problem.&lt;/li>&lt;/ul>&lt;p>If you disable the hardware offload and then re-enable offloading, you must restart the appliance for the change to take effect.&lt;/p>",
                        "display": "Offload processing to hardware",
                        "hoverhelp": "Indicate whether to offload TCP/IP packet processing to hardware. Disable this option only when IBM Support diagnoses that you are encountering a problem.",
                        "name": "HardwareOffload",
                        "summary": "Indicate whether to offload TCP/IP packet processing to hardware.",
                        "type": {
                            "href": "/mgmt/types/default/dmToggle"
                        }
                    },
                    {
                        "cli-alias": "flow-control",
                        "default": "auto",
                        "description": "The flow control mode of the Ethernet interface. The default value is &lt;b>Auto&lt;/b>. Disable this option only when IBM Support diagnoses that you are encountering a problem.",
                        "display": "Flow control mode",
                        "hoverhelp": "Set the flow control mode. Disable this option only when IBM Support diagnoses that you are encountering a problem.",
                        "name": "FlowControl",
                        "summary": "Set the flow control mode.",
                        "type": {
                            "href": "/mgmt/types/default/dmEthernetFCMode"
                        }
                    }
                ]
            },
            "property-group": [
                {
                    "display": "Main",
                    "name": "main",
                    "property-group": [
                        {
                            "display": "Basic configuration",
                            "member": [
                                {
                                    "name": "mAdminState"
                                },
                                {
                                    "name": "UserSummary"
                                },
                                {
                                    "name": "IPConfigMode"
                                },
                                {
                                    "name": "LinkAggMode"
                                }
                            ],
                            "name": "general"
                        },
                        {
                            "display": "IP addressing",
                            "member": [
                                {
                                    "name": "IPAddress"
                                },
                                {
                                    "name": "SecondaryAddress"
                                }
                            ],
                            "name": "ip-addressing"
                        },
                        {
                            "display": "IP routing",
                            "member": [
                                {
                                    "name": "DefaultGateway"
                                },
                                {
                                    "name": "DefaultIPv6Gateway"
                                },
                                {
                                    "name": "StaticRoutes"
                                }
                            ],
                            "name": "ip-routing"
                        }
                    ]
                },
                {
                    "display": "Standby control",
                    "name": "standbycontrol",
                    "property-group": [
                        {
                            "display": "Basic properties for standby control",
                            "member": [
                                {
                                    "name": "StandbyControl"
                                },
                                {
                                    "name": "Group"
                                },
                                {
                                    "name": "VirtualIP"
                                },
                                {
                                    "name": "Preempt"
                                },
                                {
                                    "name": "SecondaryVirtualIP"
                                },
                                {
                                    "name": "Priority"
                                },
                                {
                                    "name": "SelfBalance"
                                },
                                {
                                    "name": "DistAlg"
                                }
                            ],
                            "name": "standbycontrolbasic"
                        },
                        {
                            "display": "Advanced properties for standby control",
                            "member": [
                                {
                                    "name": "Authentication"
                                },
                                {
                                    "name": "HelloTimer"
                                },
                                {
                                    "name": "HoldTimer"
                                }
                            ],
                            "name": "standbycontroladvanced"
                        }
                    ]
                },
                {
                    "display": "Advanced",
                    "member": [
                        {
                            "name": "MTU"
                        },
                        {
                            "name": "MACAddress"
                        },
                        {
                            "name": "Mode"
                        },
                        {
                            "name": "ForceMode"
                        },
                        {
                            "name": "HardwareOffload"
                        },
                        {
                            "name": "DADTransmits"
                        },
                        {
                            "name": "DADRetransmitTimer"
                        },
                        {
                            "name": "FlowControl"
                        }
                    ],
                    "name": "advanced"
                }
            ],
            "summary": "Configure and manage Ethernet interfaces.",
            "uri": "network/interface"
        }
    }
}

aaa_policy_schema_response = {
    "types": [
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
                            "name": "enabled",
                            "display": "enabled"
                        },
                        {
                            "name": "disabled",
                            "display": "disabled"
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
                    "href": "/mgmt/docs/types/dmNamespaceMapping"
                },
                "self": {
                    "href": "/mgmt/types/default/dmNamespaceMapping"
                }
            },
            "type": {
                "name": "dmNamespaceMapping",
                "properties": {
                    "property": [
                        {
                            "display": "Prefix",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "description": "The prefix (Prefix:) used to map namespaces that might be encountered in client requests.",
                            "name": "Prefix",
                            "summary": "Prefix for namespace"
                        },
                        {
                            "display": "URI",
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "description": "The URI (URI:) used to map namespaces that might be encountered in client requests.",
                            "name": "URI",
                            "summary": "URI for namespace"
                        }
                    ]
                }
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmAAAPExtractIdentity"
                },
                "self": {
                    "href": "/mgmt/types/default/dmAAAPExtractIdentity"
                }
            },
            "type": {
                "name": "dmAAAPExtractIdentity",
                "properties": {
                    "property": [
                        {
                            "name": "EIBitmap",
                            "type": {
                                "href": "/mgmt/types/default/dmAAAPEIBitmap"
                            },
                            "required": "true",
                            "summary": "Select the types of identity data to extract.",
                            "cli-alias": "method",
                            "display": "Methods"
                        },
                        {
                            "name": "EICustomURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-equals",
                                    "value": "custom"
                                }
                            },
                            "summary": "URL for custom processing.",
                            "cli-alias": "custom-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Custom processing URL",
                            "description": "The request is forwarded to the specified URL for extracting an identity. The custom process should return an identity."
                        },
                        {
                            "name": "EIXPath",
                            "required-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-equals",
                                    "value": "token"
                                }
                            },
                            "summary": "XPath expression for token.",
                            "cli-alias": "xpath",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmXPathExpr"
                            },
                            "display": "XPath expression",
                            "description": "When XPath is enabled for identity extraction, this XPath expression will be applied to the entire message. The value of this expression (as a string) will be used as the extracted identity."
                        },
                        {
                            "description": "The optional validation credentials to validate the signer certificate when the method \"Subject DN from certificate in message signature\" is in use.",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoValCred"
                                }
                            },
                            "ignored-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-does-not-equal",
                                    "value": "signer-dn"
                                }
                            },
                            "cli-alias": "valcred",
                            "display": "Validation credentials for signing certificate",
                            "name": "EISignerDNValcred"
                        },
                        {
                            "name": "EICookieName",
                            "required-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-equals",
                                    "value": "cookie-token"
                                }
                            },
                            "cli-alias": "cookie-name",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Cookie name",
                            "description": "The name of the cookie in the HTTP Cookie header to extract and use as the identity token."
                        },
                        {
                            "name": "EIBasicAuthRealm",
                            "default": "login",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "ignored-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-does-not-equal",
                                    "value": "http-basic-auth"
                                }
                            },
                            "cli-alias": "basic-auth-realm",
                            "display": "HTTP Basic Authentication Realm",
                            "description": "The name of the HTTP Basic Authentication Realm as described by RFC 2617. A browser might show this name to help the user determine which credentials to supply."
                        },
                        {
                            "name": "EIUseWSSec",
                            "default": "off",
                            "required-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-equals",
                                    "value": "ltpa"
                                }
                            },
                            "summary": "If there is more than one token available, use the token from the appropriate WS-Security Security header.",
                            "cli-alias": "use-wssec-token",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "display": "Use WS-Security token first",
                            "description": "By default, the token is extracted somewhere other than WS-Security &amp;lt;Security/> header. For example, an LTPA token is extracted from the Cookie header, set this option to 'on' to use the token from the WS-Security here, if available."
                        },
                        {
                            "description": "Extract the identity from processing metadata, such as variables, protocol headers and so on. For this configuration, only metadata items contained by this configuration are fetched and returned. Unless you select this method, all metadata items applicable for the current processing rule are returned.",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/ProcessingMetadata"
                                }
                            },
                            "ignored-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-does-not-equal",
                                    "value": "metadata"
                                }
                            },
                            "cli-alias": "metadata",
                            "display": "Processing metadata items",
                            "name": "EIMetadata"
                        },
                        {
                            "name": "EIAllowRemoteTokenReference",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Whether allow this action to get a remote security token or not.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-value-not-in-list",
                                    "value": "signer-dn"
                                }
                            },
                            "cli-alias": "remote-token-allowed",
                            "display": "Retrieve remote WS-Security token",
                            "description": "If the message indicates that the WS-Security token is at a remote location, for example, the SAML assertion that holds the signer public certificate or the SAML assertion that the signed Security Token Reference (STR de-reference transform) pointing at is not with the local message, this setting will determines whether retrieval of remote WS-Security token is allowed or prohibited."
                        },
                        {
                            "name": "EIRemoteTokenProcessService",
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "summary": "The URL for a service that can process the remote security token.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "EIBitmap",
                                            "evaluation": "property-value-not-in-list",
                                            "value": "signer-dn"
                                        },
                                        {
                                            "property-name": "EIAllowRemoteTokenReference",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "remote-token-url",
                            "display": "URL to process remote token",
                            "description": "The remote WS-Security token can be signed, encrypted, or encoded. A firewall or proxy service with different actions can be used to process the remote token, either decrypting pieces of a remote SAML assertion, doing a XSLT transform, or using AAA to assert the token. This setting is the URL for that service that accepts the security token as the request of the SOAP call and, if successful, provides the final security token as the response."
                        },
                        {
                            "name": "EIPasswordRetrievalMechanism",
                            "required-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-equals",
                                    "value": "wssec-derived-key"
                                }
                            },
                            "summary": "XPath expression for token.",
                            "cli-alias": "password-retrieval-method",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmPasswordRetrievalMechanism"
                            },
                            "display": "Password-retrieval method",
                            "description": "&lt;p>Select the method to obtain the user password. The password is required to calculate the derived symmetric key.&lt;/p>&lt;p>The property is available when the identity extraction method is \"Derived-key UsernameToken element from WS-Security header\".&lt;/p>"
                        },
                        {
                            "name": "EIPasswordRetrievalCustomURL",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "EIBitmap",
                                            "evaluation": "property-equals",
                                            "value": "wssec-derived-key"
                                        },
                                        {
                                            "property-name": "EIPasswordRetrievalMechanism",
                                            "evaluation": "property-equals",
                                            "value": "custom"
                                        }
                                    ]
                                }
                            },
                            "summary": "URL for custom processing.",
                            "cli-alias": "password-retrieval-custom-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Password-retrieval processing URL",
                            "description": "The specified stylesheet or GatewayScript file is invoked to obtain the password."
                        },
                        {
                            "name": "EIPasswordRetrievalAAAInfoURL",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "EIBitmap",
                                            "evaluation": "property-equals",
                                            "value": "wssec-derived-key"
                                        },
                                        {
                                            "property-name": "EIPasswordRetrievalMechanism",
                                            "evaluation": "property-equals",
                                            "value": "xmlfile"
                                        }
                                    ]
                                }
                            },
                            "summary": "URL for DataPower AAA information file.",
                            "cli-alias": "password-retrieval-xmlfile-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "AAA information file URL",
                            "description": "The password is obtained from the specified file."
                        },
                        {
                            "name": "EISSLProxyProfile",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/SSLProxyProfile"
                                }
                            },
                            "summary": "The TLS proxy profile is deprecated. Use an TLS client profile.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "EIBitmap",
                                            "evaluation": "property-value-not-in-list",
                                            "value": "signer-dn"
                                        },
                                        {
                                            "property-name": "EIAllowRemoteTokenReference",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "EISSLClientConfigType",
                                            "evaluation": "property-does-not-equal",
                                            "value": "proxy"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ssl",
                            "display": "TLS proxy profile (deprecated)",
                            "description": "The TLS proxy profile references the required cryptographic configurations for the secure connection."
                        },
                        {
                            "name": "EIFormsLoginPolicy",
                            "required-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-value-in-list",
                                    "value": "html-forms-auth"
                                }
                            },
                            "summary": "Name of an HTML forms-based login policy.",
                            "cli-alias": "forms-login-policy",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/FormsLoginPolicy"
                                }
                            },
                            "display": "HTML forms-based login policy",
                            "description": "The name of the HTML forms-based login policy that specifies the form to collect username and password information."
                        },
                        {
                            "name": "EIOAuthClientGroup",
                            "required-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-value-in-list",
                                    "value": "oauth"
                                }
                            },
                            "label": "OAuth",
                            "cli-alias": "oauth-client-group",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "summary": "Specifies the name of the OAuth client group.",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/OAuthSupportedClientGroup"
                                }
                            },
                            "display": "Registered OAuth clients",
                            "description": "When supporting OAuth through the DataPower DataPower Gateway, specify the name of the OAuth client group."
                        },
                        {
                            "name": "EISSLClientConfigType",
                            "type": {
                                "href": "/mgmt/types/default/dmSSLClientConfigType"
                            },
                            "summary": "Set the TLS profile type to secure connections between the DataPower Gateway and its targets",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "EIBitmap",
                                            "evaluation": "property-value-not-in-list",
                                            "value": "signer-dn"
                                        },
                                        {
                                            "property-name": "EIAllowRemoteTokenReference",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ssl-client-type",
                            "display": "TLS client type",
                            "description": "The TLS profile type to secure connections between the DataPower Gateway and its targets."
                        },
                        {
                            "name": "EISSLClientProfile",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/SSLClientProfile"
                                }
                            },
                            "summary": "Set the TLS client profile to secure connections between the DataPower Gateway and its targets",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "EIBitmap",
                                            "evaluation": "property-value-not-in-list",
                                            "value": "signer-dn"
                                        },
                                        {
                                            "property-name": "EIAllowRemoteTokenReference",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "EISSLClientConfigType",
                                            "evaluation": "property-does-not-equal",
                                            "value": "client"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ssl-client",
                            "display": "TLS client profile",
                            "description": "The TLS client profile to secure connections between the DataPower Gateway and its targets."
                        },
                        {
                            "name": "EIJWTValidator",
                            "required-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-value-in-list",
                                    "value": "jwt"
                                }
                            },
                            "summary": "Configure how to verify the JWT.",
                            "cli-alias": "validate-jwt",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/AAAJWTValidator"
                                }
                            },
                            "display": "JWT validator",
                            "description": "Specify the JWT validator configuration that defines how to verify the JWT, such as the JWT credentials and validation methods."
                        },
                        {
                            "name": "EISocialLoginPolicy",
                            "required-when": {
                                "condition": {
                                    "property-name": "EIBitmap",
                                    "evaluation": "property-value-in-list",
                                    "value": "social-login"
                                }
                            },
                            "summary": "Configure the social login policy",
                            "cli-alias": "social-login-policy",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/SocialLoginPolicy"
                                }
                            },
                            "display": "Social login policy",
                            "description": "Specify the social login policy. If you want to choose the social login policy object at run time, you can set the object name in the context variable \"var:///context/AAA/social-login-policy-name\" prior to invoking this AAA action. The object specified in the context variable takes precedence over the object configured here"
                        },
                        {
                            "name": "EISAMLResponseValCred",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoValCred"
                                }
                            },
                            "summary": "Validation credentials to verify the signature of the SAML response",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "EIBitmap",
                                            "evaluation": "property-does-not-equal",
                                            "value": "saml-attr-name"
                                        },
                                        {
                                            "property-name": "EIBitmap",
                                            "evaluation": "property-does-not-equal",
                                            "value": "saml-authen-name"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "saml-response-valcred",
                            "display": "SAML response validation credentials",
                            "description": "Specify the validation credentials to verify the signature of the SAML response that wraps up the SAML assertion."
                        }
                    ]
                }
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmAAAPAuthenticate"
                },
                "self": {
                    "href": "/mgmt/types/default/dmAAAPAuthenticate"
                }
            },
            "type": {
                "properties": {
                    "property": [
                        {
                            "name": "AUMethod",
                            "default": "ldap",
                            "type": {
                                "href": "/mgmt/types/default/dmAAAPAuthenticateType"
                            },
                            "required": "true",
                            "summary": "Authentication method.",
                            "cli-alias": "method",
                            "display": "Method",
                            "description": "Select a method for authenticating the extracted identity."
                        },
                        {
                            "name": "AUCustomURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "custom"
                                }
                            },
                            "summary": "Location of the stylesheet or GatewayScript file for custom processing.",
                            "cli-alias": "custom-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Custom URL",
                            "description": "The location of the stylesheet or GatewayScript file for authentication purposes."
                        },
                        {
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "name": "AUMapURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "xmlfile"
                                }
                            },
                            "summary": "Mapping details in the DataPower AAA information file.",
                            "subtype": "dmAAAInfoURL",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "xmlfile-url",
                            "display": "AAA information file URL",
                            "description": "The location of the AAA information file. This XML file contains a list of authenticated identities and the various values needed to authenticate successfully."
                        },
                        {
                            "name": "AUHost",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-value-in-list",
                                            "value": [
                                                "ldap",
                                                "oblix",
                                                "netegrity"
                                            ]
                                        },
                                        {
                                            "property-name": "AULDAPLoadBalanceGroup",
                                            "evaluation": "property-value-in-list",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "summary": "Host name or IP address.",
                            "cli-alias": "remote-host",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-value-not-in-list",
                                            "value": [
                                                "ldap",
                                                "netegrity",
                                                "oblix"
                                            ]
                                        },
                                        {
                                            "property-name": "AULDAPLoadBalanceGroup",
                                            "evaluation": "property-value-not-in-list",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmHostname"
                            },
                            "display": "Host",
                            "description": "Specify the host name or IP address of the authentication server."
                        },
                        {
                            "name": "AUPort",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-value-in-list",
                                            "value": [
                                                "ldap",
                                                "oblix",
                                                "netegrity"
                                            ]
                                        },
                                        {
                                            "property-name": "AULDAPLoadBalanceGroup",
                                            "evaluation": "property-value-in-list",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "summary": "Server port.",
                            "cli-alias": "remote-port",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-value-not-in-list",
                                            "value": [
                                                "ldap",
                                                "netegrity",
                                                "oblix"
                                            ]
                                        },
                                        {
                                            "property-name": "AULDAPLoadBalanceGroup",
                                            "evaluation": "property-value-not-in-list",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmIPPort"
                            },
                            "display": "Port",
                            "description": "The port number to use for the authentication server."
                        },
                        {
                            "description": "The optional validation credentials to authenticate the certificate sent by a remote TLS peer during the TLS handshake.",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoValCred"
                                }
                            },
                            "label": "TLS validation credentials",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "client-ssl"
                                }
                            },
                            "cli-alias": "valcred",
                            "display": "TLS client validation credentials",
                            "name": "AUSSLValcred"
                        },
                        {
                            "name": "AUCacheAllow",
                            "default": "absolute",
                            "type": {
                                "href": "/mgmt/types/default/dmAAACacheType"
                            },
                            "required": "true",
                            "summary": "Enable caching of authentication results.",
                            "cli-alias": "cache-type",
                            "display": "Cache authentication results",
                            "description": "&lt;p>Select how to control caching of AAA authentication results. The authentication cache stores authentication data to minimize the overhead of re-authenticating the same identity. Each entry in the cache must have a unique key. This key is the output from the identity extraction phase plus any ancillary data for the defined authentication method. When there is a match against a unique key, the cache returns the results from the previous authentication of this identity.&lt;/p>&lt;p>A protocol TTL is available only with SAML and LTPA.&lt;/p>"
                        },
                        {
                            "name": "AUCacheTTL",
                            "default": 3,
                            "cli-alias": "cache-ttl",
                            "maximum": 86400,
                            "summary": "Time to cache authentication decisions.",
                            "minimum": 1,
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUCacheAllow",
                                    "evaluation": "property-equals",
                                    "value": "disabled"
                                }
                            },
                            "units": "Seconds",
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "Cache lifetime"
                        },
                        {
                            "name": "AUKerberosPrincipal",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Principal name that must appear as the server name in the Kerberos ticket. This must be a full principal name, including the Kerberos realm (for example, \"foo/bar@REALM\").",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "kerberos"
                                }
                            },
                            "cli-alias": "kerberos-principal",
                            "display": "Kerberos principal name"
                        },
                        {
                            "name": "AUKerberosPassword",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Password for the Kerberos server principal. This password is required to decrypt the client's Kerberos ticket.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "",
                            "display": "Kerberos principal password"
                        },
                        {
                            "name": "AUClearTrustServerURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "cleartrust"
                                }
                            },
                            "summary": "URL for accessing the ClearTrust server for authentication.",
                            "cli-alias": "cleartrust-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "ClearTrust server URL"
                        },
                        {
                            "name": "AUClearTrustApplication",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Name of the application put in the authentication request to the ClearTrust server.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "",
                            "display": "ClearTrust application name"
                        },
                        {
                            "name": "AUSAMLArtifactResponder",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "URL of the SAML Artifact responder.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "saml-artifact"
                                }
                            },
                            "cli-alias": "saml-artifact-responder",
                            "display": "SAML Artifact responder"
                        },
                        {
                            "name": "AUKerberosVerifySignature",
                            "default": "on",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Verify signature with Kerberos session key.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "",
                            "display": "Verify signature with Kerberos session key",
                            "description": "If enabled, the message must be signed with an HMAC signature based on the Kerberos session key. If the signature cannot be verified, authentication fails."
                        },
                        {
                            "name": "AUNetegrityBaseURI",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "URI sent to CA Single Sign-On server.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "netegrity"
                                }
                            },
                            "cli-alias": "netegrity-base-uri",
                            "display": "CA Single Sign-On Base URI",
                            "description": "The Base URI is combined with the host and port to form the URL for attempting CA Single Sign-On authentication. The Base URI should equal the concatenation of the servlet-name and its url-pattern set in its web.xml configuration file. If the servlet name is \"datapoweragent\" and the url-pattern is /, the Base URI is \"datapoweragent/\"."
                        },
                        {
                            "name": "AUSAMLAuthQueryServer",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "SAML Authentication query server.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "saml-authen-query"
                                }
                            },
                            "cli-alias": "saml-authen-query-url",
                            "display": "SAML Authentication query server",
                            "description": "URL to which to post an SAML Authentication query"
                        },
                        {
                            "name": "AUSAMLVersion",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-value-in-list",
                                    "value": [
                                        "saml-artifact",
                                        "saml-authen-query"
                                    ]
                                }
                            },
                            "summary": "Select the version of the SAML messages.",
                            "cli-alias": "saml-version",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmSAMLVersion"
                            },
                            "display": "SAML version"
                        },
                        {
                            "name": "AULDAPPrefix",
                            "default": "cn=",
                            "cli-alias": "ldap-prefix",
                            "label": "Distinguished name prefix",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ldap"
                                        },
                                        {
                                            "property-name": "AULDAPSearchForDN",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "summary": "The prefix to construct the lookup DN.",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "LDAP DN prefix"
                        },
                        {
                            "name": "AULDAPSuffix",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "label": "Distinguished name suffix",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ldap"
                                        },
                                        {
                                            "property-name": "AULDAPSearchForDN",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "summary": "The suffix to construct the lookup DN.",
                            "cli-alias": "ldap-suffix",
                            "display": "LDAP DN suffix"
                        },
                        {
                            "name": "AULDAPLoadBalanceGroup",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/LoadBalancerGroup"
                                }
                            },
                            "label": "Load balancer group",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "summary": "The LDAP load balancer group.",
                            "cli-alias": "ldap-lbgroup",
                            "display": "LDAP load balancer group"
                        },
                        {
                            "name": "AUKerberosKeytab",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "kerberos"
                                }
                            },
                            "summary": "Keytab for the Kerberos server principal. This keytab is required to decrypt the client Kerberos ticket.",
                            "cli-alias": "kerberos-keytab",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoKerberosKeytab"
                                }
                            },
                            "display": "Kerberos keytab"
                        },
                        {
                            "name": "AUWSTrustURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "ws-trust"
                                }
                            },
                            "summary": "URL of the WS-Trust server.",
                            "cli-alias": "ws-trust-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "WS-Trust token server"
                        },
                        {
                            "name": "AUSAML2Issuer",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "The Identifier of the SAML 2.x protocol message Issuer.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "",
                            "display": "SAML 2 Issuer"
                        },
                        {
                            "name": "AUSignerValcred",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoValCred"
                                }
                            },
                            "summary": "The validation credentials for a signing certificate.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "validate-signer"
                                }
                            },
                            "cli-alias": "valcred",
                            "display": "Signature validation credentials",
                            "description": "An optional set of validation credentials to verify the signature validity for the incoming message. With validation credentials, the signer certificate must be in these validation credentials or the signature is rejected as untrusted."
                        },
                        {
                            "name": "AUSignedXPath",
                            "type": {
                                "href": "/mgmt/types/default/dmXPathExpr"
                            },
                            "summary": "XPath expression for the XML entity protected by signature.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "validate-signer"
                                }
                            },
                            "cli-alias": "signed-xpath",
                            "display": "XPath expression",
                            "description": "If the incoming message is digitally signed, first verify the signature validity; when the signature is valid, optionally verify if the specific XPath expression, defined with this optional property, is part of the signed message."
                        },
                        {
                            "name": "AUSSLProxyProfile",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/SSLProxyProfile"
                                }
                            },
                            "summary": "The TLS proxy profile is deprecated. Use an TLS client profile.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "evaluation": "logical-and",
                                            "condition": [
                                                {
                                                    "property-name": "AUMethod",
                                                    "evaluation": "property-value-not-in-list",
                                                    "value": [
                                                        "cleartrust",
                                                        "ldap",
                                                        "netegrity",
                                                        "saml-artifact",
                                                        "saml-authen-query",
                                                        "ws-trust"
                                                    ]
                                                },
                                                {
                                                    "evaluation": "logical-or",
                                                    "condition": [
                                                        {
                                                            "property-name": "AUMethod",
                                                            "evaluation": "property-value-not-in-list",
                                                            "value": [
                                                                "saml-signature",
                                                                "validate-signer"
                                                            ]
                                                        },
                                                        {
                                                            "property-name": "AUAllowRemoteTokenReference",
                                                            "evaluation": "property-equals",
                                                            "value": "off"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "AUSSLClientConfigType",
                                            "evaluation": "property-does-not-equal",
                                            "value": "proxy"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ssl",
                            "display": "TLS proxy profile (deprecated)",
                            "description": "The TLS proxy profile references the required cryptographic configurations for the secure connection with the specified external authentication provider."
                        },
                        {
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/Reserved117"
                                }
                            },
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "",
                            "display": "",
                            "name": "AUNetegrityConfig"
                        },
                        {
                            "name": "AULDAPBindDN",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Distinguished name used to bind to LDAP server.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "cli-alias": "ldap-bind-dn",
                            "display": "LDAP bind DN",
                            "description": "This property is only used when the password from the identity extraction stage is a WS-Security UsernameToken PasswordDigest. In this case, the LDAP server is searched for the corresponding password so the PasswordDigest can be verified. This DN is used to bind to the LDAP server for the LDAP search."
                        },
                        {
                            "name": "AULDAPBindPassword",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Password to bind to LDAP server.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ldap"
                                        },
                                        {
                                            "property-name": "AULDAPBindPassword",
                                            "evaluation": "property-equals",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ldap-bind-password",
                            "display": "LDAP bind password (deprecated)",
                            "description": "This property is only used when the password from the identity extraction stage is a WS-Security UsernameToken PasswordDigest. In this case, the LDAP server is searched for the corresponding password so the PasswordDigest can be verified. This bind password is the password to bind to the LDAP server for the LDAP search."
                        },
                        {
                            "name": "AULDAPSearchAttribute",
                            "default": "userPassword",
                            "cli-alias": "ldap-search-attr",
                            "label": "Search attribute",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "summary": "Attribute to search for.",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "LDAP search attribute",
                            "description": "This property is only used when the password from the identity extraction stage is a WS-Security UsernameToken PasswordDigest. In this case, the LDAP server is searched for the corresponding password so the PasswordDigest can be verified. This search attribute is the attribute used in the LDAP search."
                        },
                        {
                            "name": "AULTPATokenVersionsBitmap",
                            "default": "LTPA2",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "ltpa"
                                }
                            },
                            "summary": "Versions of LTPA token that to accept.",
                            "cli-alias": "lpta-version",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmLTPATokenVersion"
                            },
                            "display": "Acceptable LTPA versions",
                            "description": "Select which LTPA token versions are acceptable. For additional information about LTPA tokens, see to the information center."
                        },
                        {
                            "name": "AULTPAKeyFile",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "ltpa"
                                }
                            },
                            "locations": {
                                "location": [
                                    "local",
                                    "store",
                                    "cert",
                                    "sharedcert"
                                ]
                            },
                            "summary": "The location of the key file that can validate the incoming LTPA token during AAA authentication.",
                            "cli-alias": "lpta-key-file",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmFSFile"
                            },
                            "display": "LTPA key file",
                            "hoverhelp": "Specify the location of the LTPA key file that can validate the incoming LTPA token during AAA authentication.",
                            "description": "The LTPA key file contains the cryptographic material to create an LTPA token for use by WebSphere (v1 and v2) or Domino. For WebSphere token creation, you must export the LTPA key file from WebSphere; this file will have portions encrypted by a password you enter below. For Domino token creation, the key file should contain only the base 64-encoded Domino shared secret."
                        },
                        {
                            "name": "AULTPAKeyFilePassword",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "label": "Key file password",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ltpa"
                                        },
                                        {
                                            "evaluation": "logical-and",
                                            "condition": [
                                                {
                                                    "property-name": "AULTPATokenVersionsBitmap",
                                                    "evaluation": "property-value-not-in-list",
                                                    "value": [
                                                        "LTPA",
                                                        "LTPA2"
                                                    ]
                                                },
                                                {
                                                    "property-name": "AULTPATokenVersionsBitmap",
                                                    "evaluation": "property-value-in-list",
                                                    "value": "LTPADomino"
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "AULTPAKeyFilePassword",
                                            "evaluation": "property-equals",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "summary": "The password that decrypts the LTPA key file.",
                            "cli-alias": "lpta-key-password",
                            "display": "LTPA key file password (deprecated)",
                            "hoverhelp": "Enter the password that decrypts the LTPA key file.",
                            "description": "The key file password decrypts certain entries in a WebSphere LTPA key file (v1 and v2). This password is not applicable to Domino key files."
                        },
                        {
                            "description": "The stash file with the LTPA key file password.",
                            "type": {
                                "href": "/mgmt/types/default/dmFSFile"
                            },
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "lpta-stash-file",
                            "display": "LTPA stash file",
                            "name": "AULTPAStashFile"
                        },
                        {
                            "name": "AUBinaryTokenX509Valcred",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "binarytokenx509"
                                }
                            },
                            "cli-alias": "x509-bin-token-valcred",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoValCred"
                                }
                            },
                            "display": "X.509 BinarySecurityToken validation credentials",
                            "description": "The validation credentials to validate the X.509 certificate in the BinarySecurityToken."
                        },
                        {
                            "name": "AUTAMServer",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "tivoli"
                                }
                            },
                            "cli-alias": "tam",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/TAM"
                                }
                            },
                            "display": "IBM Security Access Manager client",
                            "description": "Select the IBM Security Access Manager client."
                        },
                        {
                            "name": "AUAllowRemoteTokenReference",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Whether to allow the retrieval of a remote security token.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-value-not-in-list",
                                    "value": [
                                        "saml-signature",
                                        "validate-signer"
                                    ]
                                }
                            },
                            "cli-alias": "remote-token-allowed",
                            "display": "Retrieve remote WS-Security token",
                            "description": "If the message indicates that the WS-Security token is at a remote location; for example, the SAML assertion that holds the signer public certificate or the SAML assertion that the signed Security Token Reference (STR de-reference transform) pointing at is not with the local message, this setting determines whether retrieval of remote WS-Security token is allowed or prohibited."
                        },
                        {
                            "name": "AURemoteTokenProcessService",
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "summary": "The URL for a service that can process the remote security token.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-value-not-in-list",
                                            "value": [
                                                "saml-signature",
                                                "validate-signer"
                                            ]
                                        },
                                        {
                                            "property-name": "AUAllowRemoteTokenReference",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "remote-token-url",
                            "display": "URL to process remote token",
                            "description": "The remote WS-Security token could be signed, encrypted, or encoded. A firewall or proxy service with different actions can be used to process the remote token, either decrypting pieces of a remote SAML assertion, doing a XSLT transform, or using AAA to assert the token. This property is the URL for the service that accepts the security token as the request of the SOAP call and provides the final security token as the response, if successful."
                        },
                        {
                            "name": "AUWSTrustVersion",
                            "type": {
                                "href": "/mgmt/types/default/dmCryptoWSSXVersion"
                            },
                            "summary": "The version of WS-Trust or WS-SecureConversation to use. Usually both specifications are updated at the same time.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ws-trust"
                                }
                            },
                            "cli-alias": "ws-trust-version",
                            "display": "WS-Trust compatibility version",
                            "description": "Specify the WS-Trust or WS-SecureConversation version to use when WS-Trust authentication sends a request to a remote STS. The default version is v1.2."
                        },
                        {
                            "name": "AULDAPSearchForDN",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Whether to retrieve the user DN with an LDAP search.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "cli-alias": "ldap-search-for-dn",
                            "display": "Search for DN",
                            "description": "If enabled, search for the DN. The process uses the login-name and the LDAP search parameters as part of an LDAP search to retrieve the user DN. If disabled, the login-name and the LDAP prefix and the LDAP suffix construct the user DN. &lt;p>When you use an LDAP search, you can configure an LDAP connection pool at the service level and assign it to the AAA policy's XML manager. The AAA policy can reuse the connections in the LDAP connection pool when the DataPower Gateway connects to an LDAP server.&lt;/p>"
                        },
                        {
                            "name": "AULDAPSearchParameters",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-equals",
                                            "value": "ldap"
                                        },
                                        {
                                            "property-name": "AULDAPSearchForDN",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "label": "Search parameters",
                            "cli-alias": "ldap-search-param",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ldap"
                                        },
                                        {
                                            "property-name": "AULDAPSearchForDN",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "summary": "The parameters for the LDAP search.",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/LDAPSearchParameters"
                                }
                            },
                            "display": "LDAP search parameters",
                            "description": "The LDAP search parameters to perform an LDAP search to retrieve the user DN. If the \"LDAP Search For DN\" option is enabled, this property is required; otherwise, this property is not used."
                        },
                        {
                            "name": "AUWSTrustRequireClientEntropy",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Require client entropy in the WS-Trust request.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ws-trust"
                                }
                            },
                            "cli-alias": "trust-require-client-entropy",
                            "display": "Require client entropy",
                            "description": "A WS-Trust entropy element is sent by the client as part of the security token request exchange. If a WS-Trust encryption certificate is used, the client entropy material is encrypted. If the certificate is not configured, a WS-Trust BinarySecret element contains the entropy material. In this case, us an TLS profile to secure the exchange with the WS-Trust server."
                        },
                        {
                            "name": "AUWSTrustClientEntropySize",
                            "default": 32,
                            "cli-alias": "trust-client-entropy-size",
                            "maximum": 128,
                            "summary": "Length of the WS-Trust client entropy value.",
                            "minimum": 8,
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ws-trust"
                                        },
                                        {
                                            "property-name": "AUWSTrustRequireClientEntropy",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "units": "bytes",
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "Client entropy size",
                            "description": "If client entropy is configured, this property determines the size of the entropy material. The size refers to the length of the entropy prior to base 64-encoding."
                        },
                        {
                            "name": "AUWSTrustRequireServerEntropy",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Require server entropy in the WS-Trust response.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ws-trust"
                                }
                            },
                            "cli-alias": "trust-require-server-entropy",
                            "display": "Require server entropy",
                            "description": "A WS-Trust entropy element must be returned to the client as part of the security token request exchange."
                        },
                        {
                            "name": "AUWSTrustServerEntropySize",
                            "default": 32,
                            "cli-alias": "trust-server-entropy-size",
                            "maximum": 128,
                            "summary": "Minimum length of the WS-Trust server entropy value.",
                            "minimum": 8,
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ws-trust"
                                        },
                                        {
                                            "property-name": "AUWSTrustRequireServerEntropy",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "units": "bytes",
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "Server entropy size",
                            "description": "If server entropy is required, this property determines the minimum allowable size of the received entropy material. The size refers to the length of the entropy before base 64-encoding."
                        },
                        {
                            "name": "AUWSTrustRequireRSTC",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Generate a WS-Trust RequestSecurityTokenCollection request.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ws-trust"
                                }
                            },
                            "cli-alias": "trust-require-rstc",
                            "display": "Require RequestSecurityTokenCollection",
                            "description": "This property determines whether a WS-Trust RequestSecurityToken or RequestSecurityTokenCollection element is sent by the client as part of the message exchange."
                        },
                        {
                            "name": "AUWSTrustRequireAppliesToHeader",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Generate a WS-Addressing AppliesTo header.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ws-trust"
                                }
                            },
                            "cli-alias": "trust-require-applies-to-header",
                            "display": "Require AppliesTo SOAP header",
                            "description": "This parameter allows configuration of a WS-Addressing AppliesTo header."
                        },
                        {
                            "name": "AUWSTrustAppliesToHeader",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Value for the WS-Addressing AppliesTo header.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ws-trust"
                                        },
                                        {
                                            "property-name": "AUWSTrustRequireAppliesToHeader",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "trust-applies-to-header",
                            "display": "AppliesTo SOAP header",
                            "description": "The value of the WS-Addressing AppliesTo header. The header element is included in the WS-Trust request security token message sent to the WS-Trust server."
                        },
                        {
                            "name": "AUWSTrustEncryptionCertificate",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoCertificate"
                                }
                            },
                            "locations": {
                                "location": [
                                    "cert",
                                    "sharedcert"
                                ]
                            },
                            "summary": "Certificate to encrypt WS-Trust elements for the recipient.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ws-trust"
                                }
                            },
                            "cli-alias": "trust-encryption-certificate",
                            "display": "WS-Trust encryption certificate",
                            "description": "If client entropy was configured, the certificate public key encrypts the material for the recipient. If client entropy is configured and this certificate is not specified, use an TLS profile to secure the message exchange."
                        },
                        {
                            "name": "AUZOSNSSConfig",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "zosnss"
                                }
                            },
                            "summary": "z/OS NSS client configuration for SAF communication.",
                            "cli-alias": "zos-nss-au",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/ZosNSSClient"
                                }
                            },
                            "display": "z/OS NSS client configuration",
                            "description": "Select a SAF Client."
                        },
                        {
                            "name": "AULDAPAttributes",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "The list of the extra user attributes retrieved from LDAP for AAA processing.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "cli-alias": "au-ldap-attributes",
                            "display": "User auxiliary LDAP attributes",
                            "description": "Define the list of LDAP attributes as the auxiliary information for AAA processing. Use the comma sign (',') as the delimiter. For example: \"email, cn, userPassword\". These attributes are retrieved from the LDAP user store and kept in the 'var://context/ldap/auxiliary-attributes' context variable for future use, such as AAA postprocessing."
                        },
                        {
                            "name": "AUSkewTime",
                            "default": 0,
                            "cli-alias": "au-skew-time",
                            "summary": "Set the skew time between the DataPower Gateway and other systems.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-value-not-in-list",
                                    "value": [
                                        "saml-artifact",
                                        "saml-authen-query",
                                        "saml-signature"
                                    ]
                                }
                            },
                            "units": "Seconds",
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "Skew time",
                            "description": "&lt;p>Skew time is the difference between the DataPower Gateway clock time and other system times. When the skew time is set, SAML assertion expiration takes the time difference into account when the DataPower Gateway consumes SAML tokens.&lt;/p>&lt;ul>&lt;li>&lt;tt>NotBefore&lt;/tt> is validated with &lt;tt>CurrentTime&lt;/tt> minus &lt;tt>SkewTime&lt;/tt> .&lt;/li>&lt;li>&lt;tt>NotOnOrAfter&lt;/tt> is validated with &lt;tt>CurrentTime&lt;/tt> plus &lt;tt>SkewTime&lt;/tt> .&lt;/li>&lt;/ul>"
                        },
                        {
                            "name": "AUTAMPACReturn",
                            "default": "off",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "tivoli"
                                }
                            },
                            "summary": "Whether to return an IBM Security Access Manager attribute token for further use.",
                            "cli-alias": "tam-pac-return",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "display": "Return Privilege Attribute Certificate",
                            "description": "If selected, returns an IBM Security Access Manager Privilege Attribute Certificate (PAC) token on a successful authentication. The PAC token can be used in the authorization and postprocessing phases."
                        },
                        {
                            "name": "AULDAPReadTimeout",
                            "default": 60,
                            "cli-alias": "ldap-readtimeout",
                            "maximum": 86400,
                            "summary": "Number of seconds to wait for a response from LDAP server before closing the connection.",
                            "minimum": 0,
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "units": "seconds",
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "LDAP Read Timeout",
                            "description": "Specify the number of seconds to wait for a response from the LDAP server before the DataPower Gateway closes the LDAP connection. Enter a value in the range 0 - 86400. The default value is 60. A value of 0 indicates that the connection never times out. &lt;p>If you configure an LDAP connection pool and assign it to the AAA Policy's XML manager, the AAA Policy can use this LDAP connection pool. The LDAP read timer of the AAA Policy can work with the idle timer of the LDAP connection pool to remove idle LDAP connections from the LDAP connection pool.&lt;/p>"
                        },
                        {
                            "name": "AUSSLClientConfigType",
                            "type": {
                                "href": "/mgmt/types/default/dmSSLClientConfigType"
                            },
                            "summary": "Set the TLS profile type to secure connections between the DataPower Gateway and its targets",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-value-not-in-list",
                                            "value": [
                                                "cleartrust",
                                                "ldap",
                                                "netegrity",
                                                "saml-artifact",
                                                "saml-authen-query",
                                                "ws-trust"
                                            ]
                                        },
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "AUMethod",
                                                    "evaluation": "property-value-not-in-list",
                                                    "value": [
                                                        "saml-signature",
                                                        "validate-signer"
                                                    ]
                                                },
                                                {
                                                    "property-name": "AUAllowRemoteTokenReference",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ssl-client-type",
                            "display": "TLS client type",
                            "description": "The TLS profile type to secure connections between the DataPower Gateway and its targets."
                        },
                        {
                            "name": "AUSSLClientProfile",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/SSLClientProfile"
                                }
                            },
                            "summary": "Set the TLS client profile to secure connections between the DataPower Gateway and its targets",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "evaluation": "logical-and",
                                            "condition": [
                                                {
                                                    "property-name": "AUMethod",
                                                    "evaluation": "property-value-not-in-list",
                                                    "value": [
                                                        "cleartrust",
                                                        "ldap",
                                                        "netegrity",
                                                        "saml-artifact",
                                                        "saml-authen-query",
                                                        "ws-trust"
                                                    ]
                                                },
                                                {
                                                    "evaluation": "logical-or",
                                                    "condition": [
                                                        {
                                                            "property-name": "AUMethod",
                                                            "evaluation": "property-value-not-in-list",
                                                            "value": [
                                                                "saml-signature",
                                                                "validate-signer"
                                                            ]
                                                        },
                                                        {
                                                            "property-name": "AUAllowRemoteTokenReference",
                                                            "evaluation": "property-equals",
                                                            "value": "off"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "AUSSLClientConfigType",
                                            "evaluation": "property-does-not-equal",
                                            "value": "client"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ssl-client",
                            "display": "TLS client profile",
                            "description": "The TLS client profile to secure connections between the DataPower Gateway and its targets."
                        },
                        {
                            "name": "AULDAPBindPasswordAlias",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/PasswordAlias"
                                }
                            },
                            "summary": "Password alias of the password to bind to LDAP server.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "cli-alias": "ldap-bind-password-alias",
                            "display": "LDAP bind password alias",
                            "description": "This property is only used when the password from the identity extraction stage is a WS-Security UsernameToken PasswordDigest. In this case, the LDAP server is searched for the corresponding password so the PasswordDigest can be verified. This bind password is the password to bind to the LDAP server for the LDAP search."
                        },
                        {
                            "name": "AULTPAKeyFilePasswordAlias",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AULTPAKeyFilePassword",
                                            "evaluation": "property-equals",
                                            "value": ""
                                        },
                                        {
                                            "evaluation": "logical-and",
                                            "condition": [
                                                {
                                                    "property-name": "AUMethod",
                                                    "evaluation": "property-equals",
                                                    "value": "ltpa"
                                                },
                                                {
                                                    "property-name": "AULTPATokenVersionsBitmap",
                                                    "evaluation": "property-value-in-list",
                                                    "value": [
                                                        "LTPA",
                                                        "LTPA2"
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "label": "Key file password alias",
                            "cli-alias": "ltpa-key-password-alias",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ltpa"
                                        },
                                        {
                                            "evaluation": "logical-and",
                                            "condition": [
                                                {
                                                    "property-name": "AULTPATokenVersionsBitmap",
                                                    "evaluation": "property-value-not-in-list",
                                                    "value": [
                                                        "LTPA",
                                                        "LTPA2"
                                                    ]
                                                },
                                                {
                                                    "property-name": "AULTPATokenVersionsBitmap",
                                                    "evaluation": "property-value-in-list",
                                                    "value": "LTPADomino"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "summary": "The password alias of the password that decrypts the LTPA key file.",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/PasswordAlias"
                                }
                            },
                            "display": "LTPA key file password alias",
                            "hoverhelp": "Enter the password alias of the password that decrypts the LTPA key file.",
                            "description": "The key file password decrypts certain entries in a WebSphere LTPA key file (v1 and v2). This password is not applicable to Domino key files."
                        },
                        {
                            "name": "AUSMRequestType",
                            "default": "webagent",
                            "required-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-equals",
                                    "value": "netegrity"
                                }
                            },
                            "summary": "The type of authentication request to make",
                            "cli-alias": "sm-request-type",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "netegrity"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmSMRequestType"
                            },
                            "display": "Request type",
                            "description": "Specifies the type of authentication request to make. You can make the request against the CA Single Sign-On authentication web service or CA Single Sign-On web agent."
                        },
                        {
                            "name": "AUSMCookieFlow",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmSMFlow"
                            },
                            "summary": "Which flow to include the authentication session cookie",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "netegrity"
                                }
                            },
                            "cli-alias": "sm-cookie-flow",
                            "display": "Session cookie flow",
                            "description": "Identifies the flow to include the authentication session cookie. When selected, the session cookie is included in the DataPower Gateway request, response, or both."
                        },
                        {
                            "name": "AUSMHeaderFlow",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmSMFlow"
                            },
                            "summary": "Which flow to include the CA Single Sign-On HTTP headers",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "netegrity"
                                }
                            },
                            "cli-alias": "sm-header-flow",
                            "display": "CA Single Sign-On header flow",
                            "description": "Identifies the flow to include the CA Single Sign-On HTTP headers that are generated during authentication. The CA Single Sign-On HTTP headers start with &lt;tt>SM_&lt;/tt> . When selected, the &lt;tt>SM_&lt;/tt> HTTP headers are included in the DataPower Gateway request, response, or both."
                        },
                        {
                            "name": "AUSMCookieAttributes",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CookieAttributePolicy"
                                }
                            },
                            "summary": "Cookie attributes for CA Single Sign-On cookies",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AUSMCookieFlow",
                                    "evaluation": "property-value-not-in-list",
                                    "value": [
                                        "frontend",
                                        "frontend+backend",
                                        "backend+frontend"
                                    ]
                                }
                            },
                            "cli-alias": "cookie-attributes",
                            "display": "Cookie attribute policy",
                            "description": "Specifies the cookie attribute policy that allows predefined or custom attributes to be included in CA Single Sign-On cookies."
                        },
                        {
                            "name": "AUCacheControl",
                            "default": "default",
                            "type": {
                                "href": "/mgmt/types/default/dmCacheControl"
                            },
                            "summary": "Set the way to manage the caching of authentication failures",
                            "cli-alias": "cache-control",
                            "display": "Authentication caching",
                            "description": "Set the way to manage the caching of authentication failures."
                        }
                    ]
                },
                "name": "dmAAAPAuthenticate",
                "summary": "How to authenticate the identity."
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmAAAPMapCredentials"
                },
                "self": {
                    "href": "/mgmt/types/default/dmAAAPMapCredentials"
                }
            },
            "type": {
                "properties": {
                    "property": [
                        {
                            "name": "MCMethod",
                            "default": "none",
                            "type": {
                                "href": "/mgmt/types/default/dmAAAPMapCredentialType"
                            },
                            "required": "true",
                            "summary": "Select the mapping method to use.",
                            "cli-alias": "method",
                            "display": "Method"
                        },
                        {
                            "name": "MCCustomURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "MCMethod",
                                    "evaluation": "property-equals",
                                    "value": "custom"
                                }
                            },
                            "summary": "URL for custom processing.",
                            "cli-alias": "custom-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Custom URL"
                        },
                        {
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "name": "MCMapURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "MCMethod",
                                    "evaluation": "property-equals",
                                    "value": "xmlfile"
                                }
                            },
                            "summary": "URL of mapping file.",
                            "subtype": "dmAAAInfoURL",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "xmlfile-url",
                            "display": "AAA information file URL"
                        },
                        {
                            "name": "MCMapXPath",
                            "required-when": {
                                "condition": {
                                    "property-name": "MCMethod",
                                    "evaluation": "property-equals",
                                    "value": "xpath"
                                }
                            },
                            "summary": "XPath expression for mapping.",
                            "cli-alias": "xpath",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmXPathExpr"
                            },
                            "display": "XPath expression"
                        },
                        {
                            "name": "MCTFIMEndpoint",
                            "required-when": {
                                "condition": {
                                    "property-name": "MCMethod",
                                    "evaluation": "property-equals",
                                    "value": "TFIM"
                                }
                            },
                            "summary": "Name of Tivoli Federated Identity Manager endpoint configuration.",
                            "cli-alias": "tfim",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/TFIMEndpoint"
                                }
                            },
                            "display": "Tivoli Federated Identity Manager endpoint"
                        }
                    ]
                },
                "name": "dmAAAPMapCredentials",
                "summary": "How to map credentials or resources."
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmAAAPExtractResource"
                },
                "self": {
                    "href": "/mgmt/types/default/dmAAAPExtractResource"
                }
            },
            "type": {
                "properties": {
                    "property": [
                        {
                            "name": "ERBitmap",
                            "type": {
                                "href": "/mgmt/types/default/dmAAAPERBitmap"
                            },
                            "required": "true",
                            "summary": "Items to identify the resource.",
                            "cli-alias": "method",
                            "display": "Resource information"
                        },
                        {
                            "name": "ERXPath",
                            "required-when": {
                                "condition": {
                                    "property-name": "ERBitmap",
                                    "evaluation": "property-equals",
                                    "value": "XPath"
                                }
                            },
                            "summary": "XPath expression to map resources.",
                            "cli-alias": "xpath",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmXPathExpr"
                            },
                            "display": "XPath expression",
                            "description": "When \"XPath\" is selected for resource extraction, the XPath expression to apply to the entire message. The resultant string is used as the resource."
                        },
                        {
                            "description": "Use the processing metadata as the resource to authorize access, such as variables, protocol headers, and so forth. If configured, only the metadata items in this configuration are fetched and returned. If not selected, all metadata items applicable for the current processing rule are returned.",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/ProcessingMetadata"
                                }
                            },
                            "ignored-when": {
                                "condition": {
                                    "property-name": "ERBitmap",
                                    "evaluation": "property-does-not-equal",
                                    "value": "metadata"
                                }
                            },
                            "cli-alias": "metadata",
                            "display": "Processing metadata items",
                            "name": "ERMetadata"
                        }
                    ]
                },
                "name": "dmAAAPExtractResource",
                "summary": "Information to extract to identify the resource."
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmAAAPMapResource"
                },
                "self": {
                    "href": "/mgmt/types/default/dmAAAPMapResource"
                }
            },
            "type": {
                "properties": {
                    "property": [
                        {
                            "name": "MRMethod",
                            "default": "none",
                            "type": {
                                "href": "/mgmt/types/default/dmAAAPMapResourceType"
                            },
                            "required": "true",
                            "summary": "Mapping method to use.",
                            "cli-alias": "method",
                            "display": "Method"
                        },
                        {
                            "name": "MRCustomURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "MRMethod",
                                    "evaluation": "property-equals",
                                    "value": "custom"
                                }
                            },
                            "label": "Custom",
                            "cli-alias": "custom-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "summary": "URL for custom processing.",
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Custom URL"
                        },
                        {
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "name": "MRMapURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "MRMethod",
                                    "evaluation": "property-equals",
                                    "value": "xmlfile"
                                }
                            },
                            "summary": "DataPower AAA information file as the mapping.",
                            "subtype": "dmAAAInfoURL",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "xmlfile-url",
                            "display": "AAA information file URL"
                        },
                        {
                            "name": "MRMapXPath",
                            "required-when": {
                                "condition": {
                                    "property-name": "MRMethod",
                                    "evaluation": "property-equals",
                                    "value": "xpath"
                                }
                            },
                            "summary": "XPath expression for mapping.",
                            "cli-alias": "xpath",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmXPathExpr"
                            },
                            "display": "XPath expression"
                        },
                        {
                            "name": "MRTAMMap",
                            "required-when": {
                                "condition": {
                                    "property-name": "MRMethod",
                                    "evaluation": "property-equals",
                                    "value": "tivoli"
                                }
                            },
                            "summary": "Object space prefix style.",
                            "cli-alias": "tam-mapping",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmTAMObjectSpacePrefix"
                            },
                            "display": "ISAM object space mapping",
                            "description": "IBM Security Access Manager organizes resources into a hierarchical protected object space. Each protected object space has a defined convention. Select which style of object space to concatenate with the extracted resource. &lt;p>Custom: &amp;lt;prefix>&lt;/p>&lt;p>TAMBI: /PDMQ/&amp;lt;prefix>&lt;/p>&lt;p>TFIM: /itfim-wssm/wssm-default/&amp;lt;prefix>&lt;/p>&lt;p>WebSEAL: /WebSEAL/&amp;lt;prefix>&lt;/p>&lt;p>These different options help in mapping the extracted resource to a resource string that follow IBM Security Services naming conventions.&lt;/p>"
                        },
                        {
                            "name": "MRTAMInstancePrefix",
                            "required-when": {
                                "condition": {
                                    "property-name": "MRMethod",
                                    "evaluation": "property-equals",
                                    "value": "tivoli"
                                }
                            },
                            "summary": "Object space prefix.",
                            "cli-alias": "tam-prefix",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "ISAM object space instance prefix",
                            "description": "The prefix to use in the naming convention. The value of the entered property customizes the naming convention to your specific environment. &lt;p>Custom: Any user defined prefix&lt;/p>&lt;p>TAMBI: The queue manager and queue separated with a forward slash&lt;/p>&lt;p>TFIM: The name of the Tivoli Federated Identity Manager domain&lt;/p>&lt;p>WebSEAL: The name of the WebSEAL instance&lt;/p>"
                        },
                        {
                            "name": "MRTAMWebSEALDynURLFile",
                            "type": {
                                "href": "/mgmt/types/default/dmFSFile"
                            },
                            "locations": {
                                "location": [
                                    "local",
                                    "store"
                                ]
                            },
                            "summary": "WebSEAL DynURL file.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-not",
                                    "condition": {
                                        "evaluation": "logical-and",
                                        "condition": [
                                            {
                                                "property-name": "MRMethod",
                                                "evaluation": "property-equals",
                                                "value": "tivoli"
                                            },
                                            {
                                                "property-name": "MRTAMMap",
                                                "evaluation": "property-equals",
                                                "value": "WebSEAL"
                                            }
                                        ]
                                    }
                                }
                            },
                            "cli-alias": "webseal-dynurl-file",
                            "display": "WebSEAL DynURL mapping file",
                            "description": "When configured and an entry is matched for a request, the DynURL output replaces the output of the extracted resource string that is appended to the IBM Security Access Manager object space prefix."
                        }
                    ]
                },
                "name": "dmAAAPMapResource",
                "summary": "How to map credentials or resources."
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmAAAPAuthorize"
                },
                "self": {
                    "href": "/mgmt/types/default/dmAAAPAuthorize"
                }
            },
            "type": {
                "properties": {
                    "property": [
                        {
                            "name": "AZMethod",
                            "default": "anyauthenticated",
                            "type": {
                                "href": "/mgmt/types/default/dmAAAPAuthorizeType"
                            },
                            "required": "true",
                            "summary": "Authorization method.",
                            "cli-alias": "method",
                            "display": "Method",
                            "description": "Select the authorization method."
                        },
                        {
                            "name": "AZCustomURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "custom"
                                }
                            },
                            "summary": "URL for custom processing.",
                            "cli-alias": "custom-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Custom URL"
                        },
                        {
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "name": "AZMapURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "xmlfile"
                                }
                            },
                            "summary": "Specify the URL of the DataPower AAA information file for mapping.",
                            "subtype": "dmAAAInfoURL",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "xmlfile-url",
                            "display": "AAA information file URL"
                        },
                        {
                            "name": "AZHost",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-value-in-list",
                                            "value": [
                                                "ldap",
                                                "oblix",
                                                "netegrity"
                                            ]
                                        },
                                        {
                                            "property-name": "AZLDAPLoadBalanceGroup",
                                            "evaluation": "property-value-in-list",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "summary": "Host name or IP address.",
                            "cli-alias": "remote-host",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-value-not-in-list",
                                            "value": [
                                                "ldap",
                                                "netegrity",
                                                "oblix"
                                            ]
                                        },
                                        {
                                            "property-name": "AZLDAPLoadBalanceGroup",
                                            "evaluation": "property-value-not-in-list",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmHostname"
                            },
                            "display": "Host",
                            "description": "Specify the host name or IP address of the authorization server."
                        },
                        {
                            "name": "AZPort",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-value-in-list",
                                            "value": [
                                                "ldap",
                                                "oblix",
                                                "netegrity"
                                            ]
                                        },
                                        {
                                            "property-name": "AZLDAPLoadBalanceGroup",
                                            "evaluation": "property-value-in-list",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "summary": "Port number.",
                            "cli-alias": "remote-port",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-value-not-in-list",
                                            "value": [
                                                "ldap",
                                                "netegrity",
                                                "oblix"
                                            ]
                                        },
                                        {
                                            "property-name": "AZLDAPLoadBalanceGroup",
                                            "evaluation": "property-value-not-in-list",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmIPPort"
                            },
                            "display": "Port",
                            "description": "Specify the listening port on the authorization server."
                        },
                        {
                            "name": "AZLDAPGroup",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "ldap"
                                }
                            },
                            "label": "Group distinguished name",
                            "cli-alias": "ldap-group-dn",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "summary": "DN of required LDAP group.",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "LDAP Group DN"
                        },
                        {
                            "name": "AZValcred",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoValCred"
                                }
                            },
                            "summary": "Optional TLS certificates.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "",
                            "display": "Validation credentials"
                        },
                        {
                            "name": "AZSAMLURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-value-in-list",
                                    "value": [
                                        "saml-attr",
                                        "saml-authz"
                                    ]
                                }
                            },
                            "summary": "URL of SAML server.",
                            "cli-alias": "saml-server-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "SAML server URL"
                        },
                        {
                            "name": "AZSAMLType",
                            "default": "any",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-value-in-list",
                                    "value": [
                                        "saml-attr",
                                        "saml-authz",
                                        "use-authen-attr"
                                    ]
                                }
                            },
                            "summary": "Match for SAML attributes.",
                            "cli-alias": "saml-type",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmSAMLMatch"
                            },
                            "display": "SAML match",
                            "description": "Select the way to match SAML attribute names and values. The default is Any."
                        },
                        {
                            "name": "AZSAMLXPath",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AZSAMLType",
                                            "evaluation": "property-equals",
                                            "value": "xpath"
                                        },
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-value-in-list",
                                            "value": [
                                                "saml-attr",
                                                "saml-authz",
                                                "use-authen-attr"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "summary": "The XPath expression to run against the SAML statement.",
                            "cli-alias": "saml-xpath",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AZSAMLType",
                                            "evaluation": "property-does-not-equal",
                                            "value": "xpath"
                                        },
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-value-not-in-list",
                                            "value": [
                                                "saml-attr",
                                                "saml-authz",
                                                "use-authen-attr"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmXPathExpr"
                            },
                            "display": "SAML XPath"
                        },
                        {
                            "name": "AZSAMLNameQualifier",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "The value of the NameQualifier attribute of the NameIdentifier in the generated SAML query. Although an optional attribute, some SAML implementations require this attribute to be present.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-value-not-in-list",
                                    "value": [
                                        "saml-attr",
                                        "saml-authz"
                                    ]
                                }
                            },
                            "cli-alias": "saml-name-qualifier",
                            "display": "SAML NameQualifier"
                        },
                        {
                            "name": "AZCacheAllow",
                            "default": "absolute",
                            "type": {
                                "href": "/mgmt/types/default/dmAAACacheType"
                            },
                            "required": "true",
                            "summary": "Enable caching of authorization results.",
                            "cli-alias": "cache-type",
                            "display": "Cache authorization results",
                            "description": "&lt;p>Select how to control caching of AAA authorization results. The authorization cache stores authorization data to minimize the overhead of reauthorization the same credentials-resource pair. Each entry in the cache must have a unique key. When there is a match against a unique key, the cache returns the results from the previous authorization.&lt;/p>&lt;p>A protocol TTL is available only with SAML, LTPA or OAuth with a Tivoli Federated Identity Manager endpoint.&lt;/p>"
                        },
                        {
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
                        },
                        {
                            "name": "AZNetegrityBaseURI",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "URI sent to CA Single Sign-On server.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "netegrity"
                                }
                            },
                            "cli-alias": "netegrity-base-uri",
                            "display": "CA Single Sign-On Base URI",
                            "description": "The CA Single Sign-On Base URI is combined with the host, port, and CA Single Sign-On operation name extension to form the URL for attempting CA Single Sign-On authentication. The URL is of the form: http://Host:Port/NetegrityBaseURI/operationNetegrityOpNameExtension where NetegrityOpNameExtension is concatenated directly with the operation name."
                        },
                        {
                            "name": "AZNetegrityOpNameExtension",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Extension for URI sent to CA Single Sign-On server.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "netegrity"
                                        },
                                        {
                                            "property-name": "AZSMRequestType",
                                            "evaluation": "property-equals",
                                            "value": "webservice"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "netegrity-opname-ext",
                            "display": "Operation name extension",
                            "description": "The CA Single Sign-On Base URI is combined with the host, port and CA Single Sign-On operation name extension to form the URL for attempting CA Single Sign-On authentication. The URL is of the form: http://Host:Port/NetegrityBaseURI/operationNetegrityOpNameExtension where NetegrityOpNameExtension is concatenated directly with the operation name."
                        },
                        {
                            "name": "AZClearTrustServerURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "cleartrust"
                                }
                            },
                            "summary": "URL for accessing the ClearTrust server for authorization.",
                            "cli-alias": "cleartrust-server-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "ClearTrust server URL"
                        },
                        {
                            "name": "AZSAMLVersion",
                            "type": {
                                "href": "/mgmt/types/default/dmSAMLVersion"
                            },
                            "summary": "Select the version to use for SAML messages.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-value-not-in-list",
                                    "value": [
                                        "saml-attr",
                                        "saml-authz"
                                    ]
                                }
                            },
                            "cli-alias": "saml-version",
                            "display": "SAML version"
                        },
                        {
                            "name": "AZLDAPLoadBalanceGroup",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/LoadBalancerGroup"
                                }
                            },
                            "label": "Load balancer group",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "summary": "The LDAP load balancer group.",
                            "cli-alias": "ldap-lbgroup",
                            "display": "LDAP load balancer group"
                        },
                        {
                            "name": "AZLDAPBindDN",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Distinguished name to bind to LDAP server.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "cli-alias": "ldap-bind-dn",
                            "display": "LDAP bind DN"
                        },
                        {
                            "name": "AZLDAPBindPassword",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Password to bind to LDAP server.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ldap"
                                        },
                                        {
                                            "property-name": "AZLDAPBindPassword",
                                            "evaluation": "property-equals",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ldap-bind-password",
                            "display": "LDAP bind password (deprecated)"
                        },
                        {
                            "name": "AZLDAPGroupAttribute",
                            "default": "member",
                            "cli-alias": "ldap-group-attr",
                            "label": "Group attribute",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "summary": "The LDAP group's attribute name to check for membership. The authorizing identity must exist as an attribute value in the group.",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "LDAP group attribute"
                        },
                        {
                            "name": "AZSSLProxyProfile",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/SSLProxyProfile"
                                }
                            },
                            "summary": "The TLS proxy profile is deprecated. Use an TLS client profile.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-value-not-in-list",
                                            "value": [
                                                "cleartrust",
                                                "ldap",
                                                "netegrity",
                                                "saml-attr",
                                                "saml-authz"
                                            ]
                                        },
                                        {
                                            "property-name": "AZSSLClientConfigType",
                                            "evaluation": "property-does-not-equal",
                                            "value": "proxy"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ssl",
                            "display": "TLS proxy profile (deprecated)",
                            "description": "The TLS proxy profile references the required cryptographic configurations for the secure connection with the specified external authorization provider."
                        },
                        {
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/Reserved117"
                                }
                            },
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "",
                            "display": "",
                            "name": "AZNetegrityConfig"
                        },
                        {
                            "name": "AZLDAPSearchScope",
                            "default": "subtree",
                            "cli-alias": "ldap-search-scope",
                            "label": "Search scope",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "summary": "LDAP search scope.",
                            "type": {
                                "href": "/mgmt/types/default/dmLDAPSearchScope"
                            },
                            "display": "LDAP search scope",
                            "description": "Select the scope of the search relative to the input. The default value is subtree."
                        },
                        {
                            "name": "AZLDAPSearchFilter",
                            "default": "(objectClass=*)",
                            "cli-alias": "ldap-search-filter",
                            "label": "Search filter",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "summary": "LDAP search filter.",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "LDAP search filter",
                            "description": "The LDAP search filter for the search."
                        },
                        {
                            "name": "AZXACMLVersion",
                            "default": 2.0,
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "xacml"
                                }
                            },
                            "summary": "Version used for XACML messages.",
                            "cli-alias": "xacml-version",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmXACMLVersion"
                            },
                            "display": "XACML version",
                            "description": "Select the XACML version to use for the communication between the PDP and the AAA policy. The AAA policy acts as an XACML Policy Enforcement Point (PEP). The default value is 2.0."
                        },
                        {
                            "name": "AZXACMLPEPType",
                            "default": "deny-biased",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-equals",
                                            "value": "xacml"
                                        },
                                        {
                                            "property-name": "AZXACMLVersion",
                                            "evaluation": "property-does-not-equal",
                                            "value": 1.0
                                        }
                                    ]
                                }
                            },
                            "summary": "PEP type.",
                            "cli-alias": "xacml-pep-type",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmXACMLPEPType"
                            },
                            "display": "PEP type",
                            "description": "Select how the AAA policy processes the PDP authorization response. The AAA policy acts as an XACML PEP. The default value is deny-biased PEP."
                        },
                        {
                            "name": "AZXACMLUseOnBoxPDP",
                            "default": "on",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "xacml"
                                }
                            },
                            "summary": "Whether to use the built-in XACML policy decision point.",
                            "cli-alias": "xacml-use-builtin",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "display": "Use on-box PDP",
                            "description": "If enable, the DataPower Gateway uses the built-in XACML policy decision point (PDP). The configuration of an XACML PDP or the external XACML PDP service URL is required."
                        },
                        {
                            "name": "AZXACMLPDP",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-equals",
                                            "value": "xacml"
                                        },
                                        {
                                            "property-name": "AZXACMLUseOnBoxPDP",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "summary": "The name of the PDP configuration for built-in PDP feature.",
                            "cli-alias": "xacml-pdp",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/XACMLPDP"
                                }
                            },
                            "display": "Policy decision point",
                            "description": "Specify the name of the XACML policy decision point (PDP) configuration. This property takes effect only if the \"Use on-box PDP\" setting is set."
                        },
                        {
                            "name": "AZXACMLExternalPDPUrl",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-equals",
                                            "value": "xacml"
                                        },
                                        {
                                            "property-name": "AZXACMLUseOnBoxPDP",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "summary": "The external service URL that this XACML PEP sends the authorization request to and gets authorization response from.",
                            "cli-alias": "xacml-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "URL for external policy decision point",
                            "description": "Specify the external service URL that this XACML PEP sends the authorization request to and gets authorization response from. This setting takes effect only if the \"Use on-box PDP\" setting is not set."
                        },
                        {
                            "name": "AZXACMLBindingMethod",
                            "type": {
                                "href": "/mgmt/types/default/dmAAAXACMLBindingMethod"
                            },
                            "summary": "Method to generate context request.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "xacml"
                                }
                            },
                            "cli-alias": "xacml-binding-method",
                            "display": "XACML binding method",
                            "description": "Select the method to use to generate the XACML context request. The default value is custom processing."
                        },
                        {
                            "name": "AZXACMLBindingObject",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "The name of the AAA XACML Binding configuration.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "xacml-binding-object",
                            "display": "XACML binding",
                            "description": "Specify the name of the AAA XACML Binding configuration that defines how the DataPower Gateway maps AAA results and input messages to the XACML context request. This property takes effect only if the XACML binding method uses the XACML binding tool."
                        },
                        {
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "name": "AZXACMLBindingXSL",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-equals",
                                            "value": "xacml"
                                        },
                                        {
                                            "property-name": "AZXACMLBindingMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "dp-pdp"
                                        }
                                    ]
                                }
                            },
                            "summary": "The URL of a custom stylesheet or GatewayScript file that can generate the XACML context request.",
                            "subtype": "dmURLProtocol",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "xacml-binding-custom-url",
                            "display": "Custom processing to bind AAA and XACML",
                            "description": "Specify the URL of a custom stylesheet or GatewayScript file that can map AAA results and input messages to the XACML context request. This request is used to contact the PDP for an XACML decision. This property takes effect only if XACML binding method uses custom processing."
                        },
                        {
                            "name": "AZXACMLCustomObligation",
                            "cli-alias": "xacml-obligation-custom-url",
                            "summary": "The URL of the custom obligation fulfillment stylesheet or GatewayScript file.",
                            "subtype": "dmURLProtocol",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "xacml"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Custom obligation fulfillment processing",
                            "description": "The custom stylesheet or GatewayScript file that can understand the obligations from the PDP and then take actions to fulfill the obligations base on the request context. When the obligations are fulfilled, the stylesheet or GatewayScript file should output text of &amp;lt;xsl:value-of select=\"true()\"/>, otherwise, output text of &amp;lt;xsl:value-of select=\"false()\"/>."
                        },
                        {
                            "name": "AZXACMLUseSAML2",
                            "default": "off",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-equals",
                                            "value": "xacml"
                                        },
                                        {
                                            "property-name": "AZXACMLVersion",
                                            "evaluation": "property-equals",
                                            "value": 2.0
                                        },
                                        {
                                            "property-name": "AZXACMLUseOnBoxPDP",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "summary": "Use SAML2.0 Profile to communicate with the external PDP service.",
                            "cli-alias": "xacml-use-saml2",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "display": "PDP requires SAML 2.0",
                            "description": "&lt;p>If the custom binding XSLT already generated the SAML 2.0 query, Set this property to 'off'. This property is for the external PDP only.&lt;/p>&lt;p>If 'on', this property forces the PEP to talk with the external PDP by using &amp;lt;xacml-samlp:XACMLAuthzDecisionQuery> defined by SAML 2.0 Profile of XACML 2.0. You can combine this property with SOAP enveloping if the xacml-samlp:XACMLAuthzDecisionQuery needs to be wrapped by a SOAP Body element.&lt;/p>"
                        },
                        {
                            "name": "AZTAMServer",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "tivoli"
                                }
                            },
                            "summary": "IBM Security Access Manager client.",
                            "cli-alias": "tam",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/TAM"
                                }
                            },
                            "display": "IBM Security Access Manager client",
                            "description": "Select the IBM Security Access Manager client."
                        },
                        {
                            "name": "AZTAMDefaultAction",
                            "default": "T",
                            "type": {
                                "href": "/mgmt/types/default/dmTAMActionType"
                            },
                            "summary": "Default IBM Security Access Manager action.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "tivoli"
                                }
                            },
                            "cli-alias": "tam-action-default",
                            "display": "Default action",
                            "description": "Select the default IBM Security Access Manager action. The default value is T (traverse)."
                        },
                        {
                            "name": "AZTAMActionResourceMap",
                            "cli-alias": "tam-action-map",
                            "summary": "The XML file that contains the ISAM resource-action map.",
                            "subtype": "dmAAATAMMappingURL",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "tivoli"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Resource-action map",
                            "description": "The XML file that contains the IBM Security Access Manager resource-action map. This file contains an ordered set of regular expression-action pairs. The mapped resource is evaluated against the regular expressions. When a match is found, the corresponding IBM Security Access Manager action is used as the authorization action for the current request. If no match is found, the setting for the default action is used. The map file must be in the local: or store: directory."
                        },
                        {
                            "name": "AZXACMLUseSOAP",
                            "default": "off",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-equals",
                                            "value": "xacml"
                                        },
                                        {
                                            "property-name": "AZXACMLUseOnBoxPDP",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "summary": "Whether the external PDP requires SOAP envelope.",
                            "cli-alias": "xacml-use-soap",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "display": "SOAP enveloping",
                            "description": "&lt;p>If the custom binding XSLT already generated the SOAP envelope, set this property to 'off'. This setting is for the external PDP only.&lt;/p>&lt;p>If 'off', the PEP directly posts the xacml-context:Request, whether or not wrapped by SAML Profile element &amp;lt;xacml-samlp:XACMLAuthzDecisionQuery>, to the external PDP via HTTP POST method; otherwise, the request is additionally wrapped by a SOAP Body. You can combine this property with PDP requires SAML 2.0 if the XACML request should be wrapped by xacml-samlp:XACMLAuthzDecisionQuery.&lt;/p>"
                        },
                        {
                            "name": "AZZOSNSSConfig",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "zosnss"
                                }
                            },
                            "summary": "z/OS NSS client configuration for SAF communication.",
                            "cli-alias": "zos-nss-az",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/ZosNSSClient"
                                }
                            },
                            "display": "z/OS NSS client configuration",
                            "description": "Select a SAF Client configuration."
                        },
                        {
                            "name": "AZSAFDefaultAction",
                            "default": "r",
                            "type": {
                                "href": "/mgmt/types/default/dmSAFActionType"
                            },
                            "summary": "Default action.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "zosnss"
                                }
                            },
                            "cli-alias": "zos-nss-default-action",
                            "display": "Default action",
                            "description": "Select the default action. The default value is R (Read)."
                        },
                        {
                            "name": "AZLDAPAttributes",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "The list of the extra user attributes retrieved from LDAP for AAA processing.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "cli-alias": "az-ldap-attributes",
                            "display": "User auxiliary LDAP attributes",
                            "description": "Define the list of LDAP attributes as the auxiliary information for AAA processing. Use the comma sign (',') as the delimiter. For example: \"email, cn, userPassword\". These attributes are retrieved from the LDAP user store and kept in the 'var://context/ldap/auxiliary-attributes' context variable for future use, such as by AAA postprocessing."
                        },
                        {
                            "name": "AZSkewTime",
                            "default": 0,
                            "cli-alias": "az-skew-time",
                            "summary": "The skew time between the DataPower Gateway and other systems.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-value-not-in-list",
                                    "value": [
                                        "saml-authz",
                                        "saml-attr"
                                    ]
                                }
                            },
                            "units": "Seconds",
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "Skew time",
                            "description": "&lt;p>Skew time is the difference between the DataPower Gateway clock time and other system times. When the skew time is set, SAML assertion expiration takes the time difference into account when the DataPower Gateway consumes SAML tokens.&lt;/p>&lt;ul>&lt;li>&lt;tt>NotBefore&lt;/tt> is validated with &lt;tt>CurrentTime&lt;/tt> minus &lt;tt>SkewTime&lt;/tt> .&lt;/li>&lt;li>&lt;tt>NotOnOrAfter&lt;/tt> is validated with &lt;tt>CurrentTime&lt;/tt> plus &lt;tt>SkewTime&lt;/tt> .&lt;/li>&lt;/ul>"
                        },
                        {
                            "name": "AZOAuthValidationEndpointType",
                            "default": "tfim",
                            "type": {
                                "href": "/mgmt/types/default/dmOAuthValidationEndpointType"
                            },
                            "summary": "Validation endpoint type for OAuth access token.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "oauth"
                                }
                            },
                            "cli-alias": "az-oauth-endpoint-type",
                            "display": "OAuth endpoint type",
                            "description": "Specifies the validation endpoint type for the OAuth access token."
                        },
                        {
                            "name": "AZTFIMEndpoint",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "oauth"
                                }
                            },
                            "summary": "Tivoli Federated Identity Manager configuration.",
                            "cli-alias": "az-tfim-endpoint",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/TFIMEndpoint"
                                }
                            },
                            "display": "Tivoli Federated Identity Manager endpoint",
                            "description": "Specifies the Tivoli Federated Identity Manager configuration that acts as the OAuth secure token service."
                        },
                        {
                            "name": "AZOAuthEnforceScope",
                            "default": "off",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "oauth"
                                }
                            },
                            "summary": "Enforce scope locally.",
                            "cli-alias": "az-oauth-enforce-scope",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "display": "Enforce scope",
                            "description": "Specifies how to enforce the scope of the access token. When set to 'on', the mapped resource is enforced locally against the scope. When set to 'off', scope enforcement is performed by the back end. The default value is 'off'."
                        },
                        {
                            "name": "AZOAuthExportHeaders",
                            "default": "on",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "oauth"
                                }
                            },
                            "summary": "Export Tivoli Federated Identity Manager response attributes.",
                            "cli-alias": "az-oauth-export-headers",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "display": "Export response attributes",
                            "description": "Specifies whether to export the response attributes that is returned by the Tivoli Federated Identity Manager STS as HTTP headers in the back-end request. When set to 'on', all response attributes are exported to HTTP headers. The default value is 'on'."
                        },
                        {
                            "name": "AZTAMPACReturn",
                            "default": "off",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "tivoli"
                                }
                            },
                            "summary": "Whether to return an IBM Security Access Manager attribute token for further use.",
                            "cli-alias": "tam-pac-return",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "label": "Return privilege attribute certificate",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "display": "Return Privilege Attribute Certificate",
                            "description": "If selected, returns an IBM Security Access Manager Privilege Attribute Certificate (PAC) token on a successful authorization. The PAC token can be used in the postprocessing phase. This property is mutually exclusive to the same property in the authentication phase. If you select this property for both authentication and authorization, the setting will be automatically cleared for authorization when applied."
                        },
                        {
                            "name": "AZTAMPACUse",
                            "default": "off",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "tivoli"
                                }
                            },
                            "summary": "Whether to use an existing IBM Security Access Manager attribute token.",
                            "cli-alias": "use-tam-pac",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "label": "Use privilege attribute certificate",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "display": "Use Privilege Attribute Certificate",
                            "description": "&lt;p>If selected, uses the IBM Security Access Manager Privilege Attribute Certificate (PAC) token that was returned in a previous AAA phase. To use this property, the authentication or map credentials phase must return a PAC token. You can use the PAC token in the postprocessing phase.&lt;/p>&lt;p>If not selected, uses the existing identity.&lt;/p>"
                        },
                        {
                            "name": "AZLDAPReadTimeout",
                            "default": 60,
                            "cli-alias": "ldap-readtimeout",
                            "maximum": 86400,
                            "summary": "Number of seconds to wait for a response from LDAP server before the DataPower Gateway closes the connection.",
                            "minimum": 0,
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "units": "seconds",
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "LDAP Read Timeout",
                            "description": "Specify the number of seconds to wait for a response from the LDAP server before the DataPower Gateway closes the LDAP connection. Enter a value in the range 0 - 86400. The default value is 60. A value of 0 indicates that the connection never times out. &lt;p>If you configure an LDAP connection pool and assign it to the AAA Policy's XML manager, the AAA Policy can use this LDAP connection pool. The LDAP read timer of the AAA Policy can work with the idle timer of the LDAP connection pool to remove idle LDAP connections from the LDAP connection pool.&lt;/p>"
                        },
                        {
                            "name": "AZSSLClientConfigType",
                            "type": {
                                "href": "/mgmt/types/default/dmSSLClientConfigType"
                            },
                            "summary": "Set the TLS profile type to secure connections between the DataPower Gateway and its targets",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-value-not-in-list",
                                    "value": [
                                        "cleartrust",
                                        "ldap",
                                        "netegrity",
                                        "saml-attr",
                                        "saml-authz"
                                    ]
                                }
                            },
                            "cli-alias": "ssl-client-type",
                            "display": "TLS client type",
                            "description": "The TLS profile type to secure connections between the DataPower Gateway and its targets."
                        },
                        {
                            "name": "AZSSLClientProfile",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/SSLClientProfile"
                                }
                            },
                            "summary": "Set the TLS client profile to secure connections between the DataPower Gateway and its targets",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AZMethod",
                                            "evaluation": "property-value-not-in-list",
                                            "value": [
                                                "cleartrust",
                                                "ldap",
                                                "netegrity",
                                                "saml-attr",
                                                "saml-authz"
                                            ]
                                        },
                                        {
                                            "property-name": "AZSSLClientConfigType",
                                            "evaluation": "property-does-not-equal",
                                            "value": "client"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ssl-client",
                            "display": "TLS client profile",
                            "description": "The TLS client profile to secure connections between the DataPower Gateway and its targets."
                        },
                        {
                            "name": "AZLDAPBindPasswordAlias",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/PasswordAlias"
                                }
                            },
                            "summary": "Password alias of the password to bind to LDAP server.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "ldap"
                                }
                            },
                            "cli-alias": "ldap-bind-password-alias",
                            "display": "LDAP bind password alias"
                        },
                        {
                            "name": "AZSMRequestType",
                            "default": "webagent",
                            "required-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-equals",
                                    "value": "netegrity"
                                }
                            },
                            "summary": "The type of authorization request to make",
                            "cli-alias": "sm-request-type",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "netegrity"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmSMRequestType"
                            },
                            "display": "Request type",
                            "description": "Specifies the type of authorization request to make. You can make the request against the CA Single Sign-On authorization web service or CA Single Sign-On web agent."
                        },
                        {
                            "name": "AZSMCookieFlow",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmSMFlow"
                            },
                            "summary": "Which flow to include the authorization session cookie",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "netegrity"
                                }
                            },
                            "cli-alias": "sm-cookie-flow",
                            "display": "Session cookie flow",
                            "description": "Identifies the flow to include the authorization session cookie. When selected, the session cookie is included in the DataPower Gateway request, response, or both."
                        },
                        {
                            "name": "AZSMHeaderFlow",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmSMFlow"
                            },
                            "summary": "Which flow to include the CA Single Sign-On HTTP headers",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZMethod",
                                    "evaluation": "property-does-not-equal",
                                    "value": "netegrity"
                                }
                            },
                            "cli-alias": "sm-header-flow",
                            "display": "CA Single Sign-On header flow",
                            "description": "Identifies the flow to include the CA Single Sign-On HTTP headers that are generated during authorization. The CA Single Sign-On HTTP headers start with &lt;tt>SM_&lt;/tt> . When selected, the &lt;tt>SM_&lt;/tt> HTTP headers are included in the DataPower Gateway request, response, or both."
                        },
                        {
                            "name": "AZSMCookieAttributes",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CookieAttributePolicy"
                                }
                            },
                            "summary": "Cookie attributes for CA Single Sign-On cookies",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "AZSMCookieFlow",
                                    "evaluation": "property-value-not-in-list",
                                    "value": [
                                        "frontend",
                                        "frontend+backend",
                                        "backend+frontend"
                                    ]
                                }
                            },
                            "cli-alias": "cookie-attributes",
                            "display": "Cookie attribute policy",
                            "description": "Specifies the cookie attribute policy that allows predefined or custom attributes to be included in CA Single Sign-On cookies."
                        },
                        {
                            "name": "AZCacheControl",
                            "default": "default",
                            "type": {
                                "href": "/mgmt/types/default/dmCacheControl"
                            },
                            "summary": "Set the way to manage the caching of authorization failures",
                            "cli-alias": "cache-control",
                            "display": "Authorization caching",
                            "description": "Set the way to manage the caching of authorization failures."
                        }
                    ]
                },
                "name": "dmAAAPAuthorize",
                "summary": "Information to authorize the request."
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmAAAPPostProcess"
                },
                "self": {
                    "href": "/mgmt/types/default/dmAAAPPostProcess"
                }
            },
            "type": {
                "properties": {
                    "property": [
                        {
                            "name": "PPEnabled",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "required": "true",
                            "summary": "Run postprocessing stylesheet or GatewayScript file.",
                            "cli-alias": "custom-processing",
                            "display": "Run postprocessing custom processing"
                        },
                        {
                            "name": "PPCustomURL",
                            "required-when": {
                                "condition": {
                                    "property-name": "PPEnabled",
                                    "evaluation": "property-equals",
                                    "value": "on"
                                }
                            },
                            "summary": "URL for custom postprocessing stylesheet or GatewayScript file.",
                            "cli-alias": "custom-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Custom processing"
                        },
                        {
                            "name": "PPSAMLAuthAssertion",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Generate an SAML Authentication statement as provided by 3.8.0.x and later releases.",
                            "cli-alias": "saml-generate-assertion",
                            "display": "Generate SAML assertion with only Authentication statement",
                            "description": "&lt;p>Generate an SAML Authentication assertion for the authenticated identity. If a custom stylesheet or GatewayScript file successfully generates an SAML assertion, features with this setting will not generate additional SAML Assertions. This setting is functionally disabled if a custom stylesheet or GatewayScript file already provides this feature.&lt;/p>&lt;p>Enable this option to generate an SAML assertion that contains an SAML authentication statement for the authenticated user identity. The destination system might choose to rely on this SAML assertion to determine the user identity.&lt;/p>&lt;p>This setting is functionally disabled if a custom stylesheet or GatewayScript file for postprocessing already generated SAML assertions. You can enable this setting so that the custom stylesheet or GatewayScript file can customize the generation of the SAML assertion by using same configurations.&lt;/p>&lt;p>To enable the option of placing the SAML assertion within a WS-Security header, the SAML version must be 1.1.&lt;/p>"
                        },
                        {
                            "name": "PPSAMLServerName",
                            "default": "XS",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "The value of the Issuer attribute of the generated saml:Assertion or SAML SLO request.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLAuthAssertion",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLSendSLO",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "saml-server-name",
                            "display": "SAML Issuer identity",
                            "description": "&lt;p>The value of the &amp;lt;saml:Issuer> element. The default value is XS.&lt;/p>&lt;ul>&lt;li>If generating an SAML assertion, identifies the server that is making the assertion.&lt;/li>&lt;li>If sending an SLO request, identifies the issuer that is sending the request.&lt;/li>&lt;/ul>"
                        },
                        {
                            "name": "PPSAMLNameQualifier",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "The value of the NameQualifier attribute of the NameIdentifier in the generated SAML assertion. Although an optional attribute, some SAML implementations require this attribute to be present.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLAuthAssertion",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPSAMLIdentityProvider",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                },
                                                {
                                                    "property-name": "PPSAMLNameID",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "saml-name-qualifier",
                            "display": "SAML name qualifier"
                        },
                        {
                            "name": "PPKerberosTicket",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Include a WS-Security Kerberos AP-REQ BinarySecurityToken for the specified client and server principals in the WS-Security header.",
                            "cli-alias": "kerberos-include-token",
                            "display": "Include a WS-Security Kerberos AP-REQ token"
                        },
                        {
                            "name": "PPKerberosClient",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                }
                                            ]
                                        },
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosUseS4U2Proxy",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                },
                                                {
                                                    "evaluation": "logical-and",
                                                    "condition": [
                                                        {
                                                            "property-name": "PPKerberosUseS4U2Proxy",
                                                            "evaluation": "property-equals",
                                                            "value": "on"
                                                        },
                                                        {
                                                            "property-name": "AUMethod",
                                                            "evaluation": "property-does-not-equal",
                                                            "value": "kerberos"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosUseS4U2SelfAndS4U2Proxy",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                },
                                                {
                                                    "evaluation": "logical-and",
                                                    "condition": [
                                                        {
                                                            "property-name": "PPKerberosUseS4U2SelfAndS4U2Proxy",
                                                            "evaluation": "property-equals",
                                                            "value": "on"
                                                        },
                                                        {
                                                            "property-name": "AUMethod",
                                                            "evaluation": "property-equals",
                                                            "value": "kerberos"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "summary": "The principal name in the client portion of the Kerberos ticket.",
                            "cli-alias": "kerberos-client-principal",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Kerberos client principal"
                        },
                        {
                            "name": "PPKerberosClientPassword",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "The password for the client. This password is required to authenticate the client to the KDC.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "",
                            "display": "Kerberos client password"
                        },
                        {
                            "name": "PPKerberosServer",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "PPKerberosServerSource",
                                            "evaluation": "property-does-not-equal",
                                            "value": "custom-url"
                                        },
                                        {
                                            "property-name": "PPKerberosServerSource",
                                            "evaluation": "property-does-not-equal",
                                            "value": "ctx-var"
                                        }
                                    ]
                                }
                            },
                            "summary": "The principal name in the server portion of the Kerberos ticket.",
                            "cli-alias": "kerberos-server",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Kerberos server principal"
                        },
                        {
                            "name": "PPWSTrust",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "For a valid WS-Trust SecurityContextToken request, generate the appropriate security token response. This postprocessing works as WS-Trust STS. Currently only WS-SecureConversation SCT is supported.",
                            "cli-alias": "ws-trust-generate-resp",
                            "display": "Process WS-Trust SCT STS request"
                        },
                        {
                            "name": "PPTimestamp",
                            "default": "on",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Whether to output the timestamp for the generated security context token.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPWSTrust",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "ws-trust-add-timestamp",
                            "display": "Output WS-Trust token timestamp"
                        },
                        {
                            "name": "PPTimestampExpiry",
                            "default": 0,
                            "cli-alias": "ws-trust-timestamp-expiry",
                            "maximum": 31622400,
                            "summary": "Allow an explicit validity interval for the generated WS-Trust security context token. If the \"defaultexpiry\" system variable is set, use the value of 0 as the duration in seconds while issuing a new security context or renewing a context instance with new instance; if that system variable is not set, uses the value of 14400 (4 hours). If you use this setting to renew an existing security context or instance, the default value 0 means to use the old duration for the renewed cycle. The maximum validity is 31622400 (366 days).",
                            "minimum": 0,
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPWSTrust",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPWSTrustNeverExpire",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "units": "seconds",
                            "type": {
                                "href": "/mgmt/types/default/dmTimeInterval"
                            },
                            "display": "Security context validity"
                        },
                        {
                            "name": "PPAllowRenewal",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "If selected, issued WS-Trust tokens can have their lifetime period reset without a new bootstrapping authentication event. If the WS-Trust request specifically asks that the issued should be renewable, this setting is ignored.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPWSTrust",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPWSTrustNeverExpire",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ws-trust-allow-renewal",
                            "display": "Allow WS-Trust token renewal"
                        },
                        {
                            "name": "PPSAMLVersion",
                            "default": 2.0,
                            "type": {
                                "href": "/mgmt/types/default/dmSAMLVersion"
                            },
                            "summary": "Select the version of SAML assertion to generate.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLAuthAssertion",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "saml-version",
                            "display": "SAML version"
                        },
                        {
                            "name": "PPSAMLSendSLO",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Send an SAML 2.0 Single Logout request.",
                            "cli-alias": "saml-send-slo",
                            "display": "Send SAML Single Logout request (SAML 2.0 only)",
                            "description": "&lt;p>Sends an SAML 2.0 Single Logout (SLO) request to revoke the SAML Assertion token used for single-sign-on (SSO). The SLO is a request-response that the DataPower Gateway handles differently when it is working as a service provider (SP) or identity provider (IdP).&lt;/p>&lt;ul>&lt;li>When an SP, the DataPower Gateway sends an SLO request to the SAML SLO endpoint (IdP). On response, the DataPower Gateway processes the SLO response for its status.&lt;/li>&lt;li>When an IdP, the request to the DataPower Gateway contains the SLO request. The DataPower Gateway postprocessing validates against the SAML metadata file and sends the corresponding endpoint the SLO response.&lt;/li>&lt;/ul>"
                        },
                        {
                            "name": "PPSAMLSLOEndpoint",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Endpoint URL for SAML 2.0 SLO request.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLSendSLO",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "saml-slo-endpoint",
                            "display": "SAML SLO service URL",
                            "description": "The endpoint URL for SAML 2.0 Single Logout (SLO) messages. This endpoint is the authority that authenticated the assertion subject."
                        },
                        {
                            "name": "PPSSLProxyProfile",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/SSLProxyProfile"
                                }
                            },
                            "summary": "The TLS proxy profile is deprecated. Use an TLS client profile.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLSendSLO",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSSLClientConfigType",
                                            "evaluation": "property-does-not-equal",
                                            "value": "proxy"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ssl",
                            "display": "TLS proxy profile (deprecated)",
                            "description": "The TLS proxy profile references the required cryptographic configurations for the secure connection with the specified SAML Single Logout (SLO) session authority."
                        },
                        {
                            "name": "PPWSUsernameToken",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Add WS-Security UsernameToken.",
                            "cli-alias": "wssec-add-user-name-token",
                            "display": "Add WS-Security UsernameToken",
                            "description": "Add an WS-Security UsernameToken to the message. The username and password are taken from the output from the credential mapping phase."
                        },
                        {
                            "description": "Select the type of password that the UsernameToken provides.",
                            "type": {
                                "href": "/mgmt/types/default/dmWSUsernameTokenPasswordType"
                            },
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPWSUsernameToken",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPWSUsernameTokenIncludePwd",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "wssec-user-name-token-type",
                            "display": "WS-Security UsernameToken password type",
                            "name": "PPWSUsernameTokenPasswordType"
                        },
                        {
                            "name": "PPSAMLValidity",
                            "default": 0,
                            "cli-alias": "saml-validity",
                            "summary": "The value of the SAML assertion validity. This value and the skew time are for fine control of assertion validity duration.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLAuthAssertion",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "units": "seconds",
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "Assertion validity"
                        },
                        {
                            "name": "PPSAMLSkew",
                            "default": 0,
                            "cli-alias": "saml-skew",
                            "summary": "The IdP and SP system clocks can have a skew time. When the SAML assertion is generated, the expiration takes the skew time setting value into account. NotBefore has the value of (CurrentTime - SkewTime). NotOnOrAfter has the value of (CurrentTime + Validity + SkewTime).",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLAuthAssertion",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "units": "seconds",
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "Skew time"
                        },
                        {
                            "name": "PPWSUsernameTokenIncludePwd",
                            "default": "on",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Whether the password must be included in the WS-Security UsernameToken.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPWSUsernameToken",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "wssec-user-name-token-contains-pwd",
                            "display": "Include password in UsernameToken",
                            "description": "Whether the password must be included in WS-Security UsernameToken."
                        },
                        {
                            "name": "PPLTPA",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Generate an LTPA token.",
                            "cli-alias": "lpta-generate-token",
                            "display": "Generate LTPA token",
                            "description": "Generate an LTPA token."
                        },
                        {
                            "name": "PPLTPAVersion",
                            "default": "LTPA2",
                            "type": {
                                "href": "/mgmt/types/default/dmLTPATokenVersionNonBitmap"
                            },
                            "summary": "Version of the LTPA token to create.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPLTPA",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "lpta-version",
                            "display": "LTPA token version",
                            "description": "Select the LTPA token version to generate. For additional information about LTPA tokens, see the information center."
                        },
                        {
                            "name": "PPLTPAExpiry",
                            "default": 600,
                            "cli-alias": "lpta-expiry",
                            "maximum": 628992000,
                            "summary": "Lifetime of LTPA token.",
                            "minimum": 1,
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPLTPA",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "units": "seconds",
                            "type": {
                                "href": "/mgmt/types/default/dmTimeInterval"
                            },
                            "display": "LTPA token expiry"
                        },
                        {
                            "name": "PPLTPAKeyFile",
                            "required-when": {
                                "condition": {
                                    "property-name": "PPLTPA",
                                    "evaluation": "property-equals",
                                    "value": "on"
                                }
                            },
                            "locations": {
                                "location": [
                                    "local",
                                    "store",
                                    "cert",
                                    "sharedcert"
                                ]
                            },
                            "summary": "The location of the LTPA key file that can protect the LTPA token generated by the postprocessing action.",
                            "cli-alias": "lpta-key-file",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPLTPA",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmFSFile"
                            },
                            "display": "LTPA key file",
                            "hoverhelp": "Specify the location of the LTPA key file that can protect the LTPA token generated by the postprocessing action.",
                            "description": "The LTPA key file contains the cryptographic material to create an LTPA token that can be consumed by WebSphere (v1 and v2) or Domino. For WebSphere token creation, you must export the LTPA key file from WebSphere. This file has portions encrypted by a password you enter. For Domino token creation, the key file should contain only the base 64-encoded Domino shared secret."
                        },
                        {
                            "name": "PPLTPAKeyFilePassword",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "label": "Key file password",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPLTPA",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                },
                                                {
                                                    "evaluation": "logical-and",
                                                    "condition": [
                                                        {
                                                            "property-name": "PPLTPAVersion",
                                                            "evaluation": "property-value-not-in-list",
                                                            "value": [
                                                                "LTPA",
                                                                "LTPA1FIPS",
                                                                "LTPA2",
                                                                "LTPA2WAS7"
                                                            ]
                                                        },
                                                        {
                                                            "property-name": "PPLTPAVersion",
                                                            "evaluation": "property-value-in-list",
                                                            "value": "LTPADomino"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "PPLTPAKeyFilePassword",
                                            "evaluation": "property-equals",
                                            "value": ""
                                        }
                                    ]
                                }
                            },
                            "summary": "The password that decrypts the LTPA key file.",
                            "cli-alias": "lpta-key-file-password",
                            "display": "LTPA key file password",
                            "hoverhelp": "Enter the password that decrypts the LTPA key file.",
                            "description": "The key file password decrypts certain entries in a WebSphere LTPA key file (v1 and v2). This password is not applicable to Domino key files."
                        },
                        {
                            "name": "PPLTPAStashFile",
                            "type": {
                                "href": "/mgmt/types/default/dmFSFile"
                            },
                            "summary": "The stash file with the LTPA key file password.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "cli-alias": "lpta-stash-file",
                            "display": "LTPA stash file"
                        },
                        {
                            "name": "PPKerberosSPNEGOToken",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Generate a Kerberos SPNEGO token to be inserted into the WWW-Authenticate HTTP header.",
                            "cli-alias": "kerberos-generate-spnego",
                            "display": "Generate Kerberos SPNEGO token"
                        },
                        {
                            "name": "PPKerberosBstValueType",
                            "default": "http://docs.oasis-open.org/wss/oasis-wss-kerberos-token-profile-1.1#GSS_Kerberosv5_AP_REQ",
                            "required-when": {
                                "condition": {
                                    "property-name": "PPKerberosTicket",
                                    "evaluation": "property-equals",
                                    "value": "on"
                                }
                            },
                            "summary": "Value of the ValueType attribute in the Kerberos AP-REQ message.",
                            "cli-alias": "kerberos-value-type",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmCryptoKerberosBstValueType"
                            },
                            "display": "ValueType for generated Kerberos BinarySecurityToken",
                            "description": "Select the value for the ValueType attribute of the WS-Security BinarySecurityToken. The Kerberos AP-REQ message contains the ValueType attribute."
                        },
                        {
                            "name": "PPSAMLUseWSSec",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Generate a WS-Security Security header to wrap the token.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLAuthAssertion",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "saml-in-wssec",
                            "display": "Wrap SAML assertion in WS-Security Security header",
                            "description": "By default, the SAML assertion is inserted as a child element of the SOAP header. Setting to 'on' places the SAML assertion in a WS-Security compliant header, as detailed in the WS-Security SAML token profile."
                        },
                        {
                            "name": "PPKerberosClientKeytab",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                }
                                            ]
                                        },
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosUseS4U2Proxy",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                },
                                                {
                                                    "evaluation": "logical-and",
                                                    "condition": [
                                                        {
                                                            "property-name": "PPKerberosUseS4U2Proxy",
                                                            "evaluation": "property-equals",
                                                            "value": "on"
                                                        },
                                                        {
                                                            "property-name": "AUMethod",
                                                            "evaluation": "property-does-not-equal",
                                                            "value": "kerberos"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosUseS4U2SelfAndS4U2Proxy",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                },
                                                {
                                                    "evaluation": "logical-and",
                                                    "condition": [
                                                        {
                                                            "property-name": "PPKerberosUseS4U2SelfAndS4U2Proxy",
                                                            "evaluation": "property-equals",
                                                            "value": "on"
                                                        },
                                                        {
                                                            "property-name": "AUMethod",
                                                            "evaluation": "property-equals",
                                                            "value": "kerberos"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "summary": "The keytab for the client. This keytab is required to authenticate the client to the KDC.",
                            "cli-alias": "kerberos-client-keytab",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoKerberosKeytab"
                                }
                            },
                            "display": "Kerberos client keytab"
                        },
                        {
                            "name": "PPUseWSSec",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Generate a WS-Security Security header to wrap the token.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": {
                                        "evaluation": "logical-or",
                                        "condition": [
                                            {
                                                "property-name": "PPLTPA",
                                                "evaluation": "property-equals",
                                                "value": "off"
                                            },
                                            {
                                                "property-name": "PPLTPAVersion",
                                                "evaluation": "property-equals",
                                                "value": "LTPADomino"
                                            }
                                        ]
                                    }
                                }
                            },
                            "cli-alias": "wssec-header-wrap-token",
                            "display": "Wrap token in WS-Security Security header",
                            "description": "By default, the token cannot be wrapped by the WS-Security standard &amp;lt;Security/> header. Set to 'on' to generate a WS-Security header that contains the token. Otherwise, the default wrapping for that token type is used. Use this setting for the LTPA token."
                        },
                        {
                            "name": "PPActorRoleID",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Specify the actor role identifier for the WS-Security Security header.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-not",
                                    "condition": {
                                        "evaluation": "logical-or",
                                        "condition": [
                                            {
                                                "property-name": "PPWSUsernameToken",
                                                "evaluation": "property-equals",
                                                "value": "on"
                                            },
                                            {
                                                "property-name": "PPTFIMTokenMapping",
                                                "evaluation": "property-equals",
                                                "value": "on"
                                            },
                                            {
                                                "property-name": "PPICRXToken",
                                                "evaluation": "property-equals",
                                                "value": "on"
                                            },
                                            {
                                                "property-name": "PPSAMLIdentityProvider",
                                                "evaluation": "property-equals",
                                                "value": "on"
                                            },
                                            {
                                                "evaluation": "logical-and",
                                                "condition": [
                                                    {
                                                        "property-name": "PPLTPA",
                                                        "evaluation": "property-equals",
                                                        "value": "on"
                                                    },
                                                    {
                                                        "property-name": "PPLTPAVersion",
                                                        "evaluation": "property-does-not-equal",
                                                        "value": "LTPADomino"
                                                    },
                                                    {
                                                        "property-name": "PPUseWSSec",
                                                        "evaluation": "property-equals",
                                                        "value": "on"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            },
                            "cli-alias": "wssec-actor-role-id",
                            "display": "Actor or role identifier",
                            "description": "Specify the identifier for the SOAP1.1 actor or SOAP1.2 role for the DataPower DataPower Gateway in processing a WS-Security Security header. The DataPower Gateway works as that actor or role in consuming the input and generating the output for the next SOAP endpoint. This property is only effective when a SOAP message is being used for WS-Security 1.0 or 1.1. Some well-known values are as follows: &lt;table border=\"1\">&lt;tr>&lt;td valign=\"left\">http://schemas.xmlsoap.org/soap/actor/next&lt;/td>&lt;td>Every one, including the intermediary and ultimate receiver, receives the message should be able to processing the Security header.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">http://www.w3.org/2003/05/soap-envelope/role/none&lt;/td>&lt;td>No one should process the Security Header.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">http://www.w3.org/2003/05/soap-envelope/role/next&lt;/td>&lt;td>Every one, including the intermediary and ultimate receiver, receives the message should be able to processing the Security header.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">http://www.w3.org/2003/05/soap-envelope/role/ultimateReceiver&lt;/td>&lt;td>The message ultimate receiver can process the Security header. This is the default value if such setting is not configured.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">&amp;lt;blank or empty string>&lt;/td>&lt;td>The empty string \"\" (without quotes) indicates that no \"actor/role\" identifier is configured. If no actor/role setting is configured, the ultimateReceiver is assumed when processing the message, and no actor/role attribute will be added when generating the WS-Security Security header. Note: This value will NOT generate an attribute with an empty value, which is the behavior as defined by constant string \"USE_MESSAGE_BASE_URI\". There should not be more than one Security header omitting the actor/role identifier.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">USE_MESSAGE_BASE_URI&lt;/td>&lt;td>The constant value \"USE_MESSAGE_BASE_URI\" without quotes indicates that the actor/role identifier will be the base URL of the message. If the SOAP message is transported using HTTP, the base URI is the Request-URI of the http request.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">any other customized string&lt;/td>&lt;td>You can input any string to identify the Security header's actor or role.&lt;/td>&lt;/tr>&lt;/table>"
                        },
                        {
                            "name": "PPTFIMTokenMapping",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Request Tivoli Federated Identity Manager token mapping.",
                            "cli-alias": "tfim-token-mapping",
                            "display": "Request Tivoli Federated Identity Manager token mapping"
                        },
                        {
                            "name": "PPTFIMEndpoint",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPTFIMTokenMapping",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPTFIMRetrieveMode",
                                            "evaluation": "property-does-not-equal",
                                            "value": "FromMC"
                                        }
                                    ]
                                }
                            },
                            "summary": "Tivoli Federated Identity Manager endpoint configuration.",
                            "cli-alias": "tfim-endpoint",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/TFIMEndpoint"
                                }
                            },
                            "display": "Tivoli Federated Identity Manager endpoint"
                        },
                        {
                            "name": "PPWSDerivedKeyUsernameToken",
                            "default": "off",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPWSUsernameToken",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPWSUsernameTokenIncludePwd",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "summary": "Add WS-Security Derived-Key UsernameToken.",
                            "cli-alias": "wssec-use-derived-key",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "display": "Use Derived-Key variant of WS-Security UsernameToken",
                            "description": "Add a WS-Security Derived-Key UsernameToken to the message, and add an HMAC signature using the derived key. The username and password are taken from the output of the credential mapping phase."
                        },
                        {
                            "name": "PPWSDerivedKeyUsernameTokenIterations",
                            "default": 1000,
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPWSUsernameToken",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPWSUsernameTokenIncludePwd",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPWSDerivedKeyUsernameToken",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "summary": "Number of rounds of hashing to perform.",
                            "cli-alias": "wssec-derived-key-hash-iter",
                            "minimum": 2,
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "Hashing iteration count",
                            "description": "Number of rounds of hashing to use when generating a derived key from a password. The default value is 1000. The minimum value is 2."
                        },
                        {
                            "name": "PPWSUsernameTokenAllowReplacement",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Whether to replace an existing UsernameToken.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPWSUsernameToken",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "wssec-replace-existing",
                            "display": "Replace existing UsernameToken",
                            "description": "If postprocessing requests the generation of a UsernameToken but the message already contains a UsernameToken, the default behavior is to retain the original token and not generate a new one. Setting to 'on' causes the generated token to replace any existing ones."
                        },
                        {
                            "name": "PPTFIMReplaceMethod",
                            "default": "all",
                            "required-when": {
                                "condition": {
                                    "property-name": "PPTFIMTokenMapping",
                                    "evaluation": "property-equals",
                                    "value": "on"
                                }
                            },
                            "summary": "Method to use with Tivoli Federated Identity Manager responses.",
                            "cli-alias": "tfim-replace-method",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmTFIMTokenReplaceMode"
                            },
                            "display": "Replacement method",
                            "description": "Select how to handle the token that Tivoli Federated Identity Manager returns."
                        },
                        {
                            "name": "PPTFIMRetrieveMode",
                            "default": "CallTFIM",
                            "required-when": {
                                "condition": {
                                    "property-name": "PPTFIMTokenMapping",
                                    "evaluation": "property-equals",
                                    "value": "on"
                                }
                            },
                            "summary": "Method to retrieve token from Tivoli Federated Identity Manager.",
                            "cli-alias": "tfim-retrieval-method",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmTFIMRetrieveMode"
                            },
                            "display": "Retrieval method",
                            "description": "Select the method to retrieve the token from Tivoli Federated Identity Manager."
                        },
                        {
                            "name": "PPHMACSigningAlg",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPWSUsernameToken",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPWSUsernameTokenIncludePwd",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPWSDerivedKeyUsernameToken",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "summary": "The algorithm to sign the token.",
                            "cli-alias": "hmac-signing-algorithm",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmCryptoHMACSigningAlgorithm"
                            },
                            "display": "HMAC signing algorithm",
                            "description": "Select the HMAC algorithm to sign the token. This option is available if WS-Security UsernameToken was requested in postprocessing and WS-Security Derived-Key UsernameToken is added to the message with an HMAC signature."
                        },
                        {
                            "name": "PPSigningHashAlg",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPWSUsernameToken",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPWSUsernameTokenIncludePwd",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPWSDerivedKeyUsernameToken",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "summary": "Signing message digest algorithm.",
                            "cli-alias": "message-digest-algorithm",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmCryptoHashAlgorithm"
                            },
                            "display": "Signing message digest algorithm",
                            "description": "Select the algorithm for the message digest when generating a digital signature. This algorithm is used with only the UsernameToken postprocessing method."
                        },
                        {
                            "name": "PPWSTrustHeader",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Return the WS-Trust token in the SOAP header rather than in the SOAP body.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPWSTrust",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "ws-trust-in-header",
                            "display": "Return the WS-Trust token as SOAP header",
                            "description": "Rather than being put inside the SOAP Body, the wst:RequestedSecurityToken is wrapped by a wst:IssuedToken element and returned as a SOAP header."
                        },
                        {
                            "name": "PPWSSCKeySource",
                            "default": "random",
                            "type": {
                                "href": "/mgmt/types/default/dmWSSCKeySourceType"
                            },
                            "summary": "Where to get the shared secret to initialize the WS-Trust or WS-SecureConversation SecurityContext.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPWSTrust",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "ws-trust-key-source",
                            "display": "Source of shared secret to initialize SecurityContext",
                            "description": "With the WS-Trust postprocessing method, processing works as an on-box WS-Trust STS backed by WS-SecureConversation. A symmetric shared secret key is needed to initialize the WS-SecureConversation SecurityContext. This key can be an authenticated token from the request message (such as Kerberos token), a token generated by the DataPower DataPower Gateway (not supported), a randomness key, or a static shared secret."
                        },
                        {
                            "name": "PPSharedSecretKey",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoSSKey"
                                }
                            },
                            "summary": "Static shared secret defined by the Shared Secret Key configuration.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPWSSCKeySource",
                                    "evaluation": "property-does-not-equal",
                                    "value": "static"
                                }
                            },
                            "cli-alias": "ws-trust-shared-key",
                            "display": "Shared secret key",
                            "description": "A shared secret key that can be used to initialize the SecurityContext. This setting specifies a static symmetric key to use for every SecurityContext. Therefore, this method is less secure than any other key types and not recommended."
                        },
                        {
                            "name": "PPWSTrustRenewalWait",
                            "default": 0,
                            "cli-alias": "ws-trust-renewal-wait",
                            "maximum": 2678400,
                            "summary": "How long the service can keep the expired token before a renewal is requested.",
                            "minimum": 0,
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPWSTrust",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPWSTrustNeverExpire",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPAllowRenewal",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "Wait time for renewal",
                            "description": "Specify the number of seconds that you allow STS to keep the expired SecurityContext. By default, after a WS-Trust token expires, it can be removed from the STS and is not allowed to renew after expiration. Therefore, you would have to renew it before a token expires. If the WS-Trust request specifically asks that the issued can be renewed after expiration and this setting has a value of 0, the token is issued or renewed with 1 hour (3600 seconds) wait time. The default value is 0. The maximum TTL is 2678400 (31 days)."
                        },
                        {
                            "name": "PPWSTrustNewInstance",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Issue a new Instance when the request is to renew the WS-Trust token.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPWSTrust",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPWSTrustNeverExpire",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPAllowRenewal",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ws-trust-new-instance",
                            "display": "Issue new Instance for WS-Trust renewal",
                            "description": "When set to 'on', the SCT renewal request creates a new Instance of the current context, if the request does not have an Instance name. If the request is for a valid existing Instance, renews that Instance."
                        },
                        {
                            "name": "PPWSTrustNewKey",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Use a different key than the current one for requests to renew the WS-Trust token.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPWSTrust",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPWSTrustNeverExpire",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPAllowRenewal",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPWSTrustNewInstance",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ws-trust-new-key",
                            "display": "Update context key for WS-Trust renewal",
                            "description": "When set to 'on', the SCT renewal request does not use the existing shared secret key of the renewed context."
                        },
                        {
                            "name": "PPWSTrustNeverExpire",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Force the SecurityContext or Instance to live forever unless explicitly changed afterwards.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPWSTrust",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "ws-trust-never-expire",
                            "display": "WS-Trust SecurityContext never expires",
                            "description": "When set to 'on', the SCT or Instance will be initialized to live forever. The duration can still be changed afterwards with an explicit number of seconds."
                        },
                        {
                            "name": "PPICRXToken",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Create an ICRX token from the authenticated credentials.",
                            "cli-alias": "generate-icrx",
                            "display": "Generate ICRX token for z/OS identity propagation",
                            "description": "Create an ICRX token from the authenticated credentials. When generated, the WS-Security binary token with an ICRX token is inserted into the WS-Security header. This token can be used for interoperability with the CICS Transaction Server for z/OS identity propagation support."
                        },
                        {
                            "name": "PPICRXUserRealm",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "ICRX realm as defined in the SAF configuration.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPICRXToken",
                                    "evaluation": "property-does-not-equal",
                                    "value": "on"
                                }
                            },
                            "cli-alias": "icrx-user-realm",
                            "display": "ICRX realm",
                            "description": "The ICRX realm as defined in the SAF configuration. Generally, this value is the equivalent of the prefix for a DN in a user registry."
                        },
                        {
                            "name": "PPSAMLIdentityProvider",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Generate a general SAML assertion with flexible format.",
                            "cli-alias": "generate-saml-assertion",
                            "display": "Generate SAML assertion or response",
                            "description": "&lt;p>This postprocessing method provides more flexible features than the \"Generate SAML assertion with only Authentication statement\" postprocessing method, which is kept to support earlier releases.&lt;/p>&lt;p>Enable this option to generate an SAML assertion in a more flexible format. The SAML assertion can contain an authentication statement, an authorization statement, or an attribute statement.&lt;/p>&lt;p>The SAML attribute value can be a user LDAP attribute value, which can be fetched directly by the LDAP authentication or authorization method with the list of LDAP attribute names defined by user auxiliary LDAP attributes, or available indirectly with the 'var://context/ldap/auxiliary-attributes' variable by a custom stylesheet or GatewayScript file, such as the dp:ldap-search call to the LDAP, and put the &amp;lt;attribute-value/> elements of the LDAP results to the variable.&lt;/p>&lt;p>This postprocessing method provides options so that different SAML subject confirmation method can be configured.&lt;/p>&lt;p>To sign the SAML assertion, configure a WS-Security sign action or SAML enveloped sign action after the AAA action in the processing rule.&lt;/p>"
                        },
                        {
                            "name": "PPSAMLProtocol",
                            "default": "assertion",
                            "type": {
                                "href": "/mgmt/types/default/dmSAMLProtocol"
                            },
                            "summary": "Scenario to generate the SAML assertion for.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLIdentityProvider",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "saml-protocol",
                            "display": "SAML protocol or profile",
                            "description": "Select the SAML protocol to wrap up the SAML assertion."
                        },
                        {
                            "name": "PPSAMLResponseDestination",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Value of the optional destination attribute for the SAML 2.0 Response element.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLVersion",
                                            "evaluation": "property-does-not-equal",
                                            "value": 2.0
                                        },
                                        {
                                            "property-name": "saml-protocol",
                                            "evaluation": "property-equals",
                                            "value": "assertion"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "saml-response-destination",
                            "display": "Response destination",
                            "description": "A URI reference that indicates the address where this request was sent. This attribute is useful to prevent malicious forwarding of requests to unintended recipients, which is a required protection by some protocol bindings. If present, the actual recipient must check that the URI reference identifies the location at which the message was received. If the location is not checked, the request must be discarded. Some protocol bindings require the use of this attribute"
                        },
                        {
                            "name": "PPResultWrapup",
                            "default": "wssec-replace",
                            "type": {
                                "href": "/mgmt/types/default/dmResultWrapup"
                            },
                            "summary": "Define how to wrap up the result being generated.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLIdentityProvider",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "result-wrapup",
                            "display": "Wrap up result",
                            "description": "Select the method to output the result being generated. When the DataPower DataPower Gateway is configured for SOAP or WS-Security processing, different output methods are used."
                        },
                        {
                            "name": "PPSAMLAssertionType",
                            "default": "authentication+attribute",
                            "required-when": {
                                "condition": {
                                    "property-name": "PPSAMLIdentityProvider",
                                    "evaluation": "property-equals",
                                    "value": "on"
                                }
                            },
                            "summary": "Which SAML statements to include.",
                            "cli-alias": "saml-assertion-type",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLIdentityProvider",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmSAMLStatementType"
                            },
                            "display": "SAML assertion type",
                            "description": "Specify the SAML statement types to generate for the SAML assertion."
                        },
                        {
                            "name": "PPSAMLSubjectConfirm",
                            "default": "bearer",
                            "type": {
                                "href": "/mgmt/types/default/dmSAMLSubjectConfirmationType"
                            },
                            "summary": "Subject confirmation method for the SAML assertion.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLIdentityProvider",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "saml-subject-confirm",
                            "display": "SAML subject confirmation method",
                            "description": "Specify the methods so that the destination system can confirm the subject of the SAML assertion."
                        },
                        {
                            "name": "PPSAMLNameID",
                            "default": "on",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Whether the generated token contains a Name Identifier.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLIdentityProvider",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "saml-nid",
                            "display": "SAML subject contains Name Identifier",
                            "description": "&lt;p>The SAML Subject element cannot contain a Name Identifier, especially if the Subject confirmation method is holder of key. If holder of key, the key represents the same entity as the subject. In this case, the Name Identifier can be omitted.&lt;/p>&lt;p>Set to 'off' if the SAML assertion expected by the SAML SP, for any reason, decided not to require a Name Identifier for the SAML Subject element.&lt;/p>"
                        },
                        {
                            "name": "PPSAMLNameIDFormat",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "The value of the optional Format attribute of the Name Identifier in the generated SAML query.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLNameID",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "saml-nid-format",
                            "display": "SAML Name Identifier format",
                            "description": "&lt;p>Specify a URI reference that represents the classification of string-based identifier information. Any standard or arbitrary URI is allowed. If the value is an empty string, the DataPower Gateway attempts to determine the value from the AAA context.&lt;/p>&lt;p>Some SAML protocols require a specified value, such as 'urn:oasis:names:tc:SAML:2.0:nameid-format:entity' or 'urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified'.&lt;/p>"
                        },
                        {
                            "name": "PPSAMLRecipient",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "The value of the Recipient for SAML1.x Response or SAML 2.0 SubjectConfirmationData.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLIdentityProvider",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "saml-recipient",
                            "display": "SAML Recipient",
                            "description": "&lt;p>A URI that specifies the entity or location where an attesting entity can present the assertion. Any standard or arbitrary URI is allowed.&lt;/p>&lt;ul>&lt;li>If the value is an empty string, the optional attribute is not generated.&lt;/li>&lt;li>If the generated SAML assertion is in version 2.0, specifies the value for the Recipient attribute of the SubjectConfirmationData element.&lt;/li>&lt;li>If the generated SAML assertion is in version 1.x, specifies the value for the Recipient attribute of the Response element.&lt;/li>&lt;/ul>"
                        },
                        {
                            "name": "PPSAMLAudience",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Optional SAML Audience for the assertion.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLIdentityProvider",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "saml-audience",
                            "display": "SAML Audience",
                            "description": "&lt;p>SAML Audience is a URI reference that identifies an intended audience. Specify any number of audience URIs to process the generated SAML assertion.&lt;/p>&lt;ul>&lt;li>If the value is an empty string, the SAML audience is not restricted.&lt;/li>&lt;li>If there are more than one audience URIs, use the '+' character as the delimiter between URIs. In this case, if a URI contains real '+' characters, convert each '+' to '\\+'.&lt;/li>&lt;/ul>"
                        },
                        {
                            "name": "PPSAMLOmitNotBefore",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Whether the assertion is considered valid in the past.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLIdentityProvider",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "saml-omit-notbefore",
                            "display": "Omit NotBefore attribute",
                            "description": "&lt;p>If true, the &lt;tt>NotBefore&lt;/tt> attribute in the SAML assertion is omitted. The assertion is considered as valid in all its past, even before the time it was issued.&lt;/p>&lt;p>This behavior is a behavior being required to respond an &lt;tt>AuthnRequest&lt;/tt> .&lt;/p>"
                        },
                        {
                            "name": "PPOneTimeUse",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Whether the generated token is for only one time use.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLVersion",
                                            "evaluation": "property-equals",
                                            "value": 1.0
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "one-time-use",
                            "display": "One time use only",
                            "description": "&lt;p>If true, the destination system or relying party should not cache the generated token.&lt;/p>&lt;p>The token being generated might contain the property for this characteristic, which is especially practical for SAML assertions.&lt;/p>"
                        },
                        {
                            "name": "PPSAMLProxy",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Whether SAML ProxyRestriction is needed.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLVersion",
                                            "evaluation": "property-does-not-equal",
                                            "value": 2.0
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "saml-proxy",
                            "display": "Allow SAML ProxyRestriction",
                            "description": "If true, the generated SAML assertion provides limitations that the asserting party imposes on relying parties that in turn wish to act as asserting parties and issue subsequent assertions of their own on the basis of the information in the original assertion. A relying party acting as an asserting party must not issue an assertion that itself violates the restrictions specified in this condition on the basis of an assertion containing such a condition."
                        },
                        {
                            "name": "PPSAMLProxyAudience",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "summary": "Who can issue subsequent assertions of their own on the basis of this assertion.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLProxy",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLVersion",
                                            "evaluation": "property-does-not-equal",
                                            "value": 2.0
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "saml-proxy-audience",
                            "display": "SAML proxy audience",
                            "description": "&lt;p>Specifies the set of audiences (proxy) to whom the asserting party permits new assertions to be issued on the basis of this assertion.&lt;/p>&lt;ul>&lt;li>If the value is an empty string, the assertion does not contain the Audience element in the ProxyRestriction element.&lt;/li>&lt;li>If there are more than one audience URIs, use the '+' character as the delimiter between URIs. If a URI contains real '+' characters, convert each '+' to '\\+'.&lt;/li>&lt;/ul>"
                        },
                        {
                            "name": "PPSAMLProxyCount",
                            "default": 0,
                            "cli-alias": "saml-proxy-count",
                            "maximum": 65535,
                            "summary": "How many times can new assertions be issued before the ultimate use.",
                            "minimum": 0,
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLProxy",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLVersion",
                                            "evaluation": "property-does-not-equal",
                                            "value": 2.0
                                        }
                                    ]
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmUInt32"
                            },
                            "display": "SAML proxy count",
                            "description": "&lt;p>Specifies the maximum number of indirections that the asserting party permits between this assertion and the assertion that is ultimately issued on this basis.&lt;/p>&lt;p>A value of zero indicates that a relying party must not issue an assertion to another relying party on the basis of this assertion. If greater than zero, any assertions issued must contain a ProxyRestriction element with a Count value of at most one less than this value.&lt;/p>&lt;p>The maximum value is 65535.&lt;/p>"
                        },
                        {
                            "name": "PPSAMLAuthzAction",
                            "default": "AllHTTP",
                            "type": {
                                "href": "/mgmt/types/default/dmSAMLAction"
                            },
                            "summary": "Specify what action the subject can take on the resource.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSAMLAssertionType",
                                            "evaluation": "property-does-not-equal",
                                            "value": "authorization"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "saml-authz-action",
                            "display": "Action for SAML Authorization decision",
                            "description": "Specify what standard action the subject is authorized to take on the resource. The SAML specification has defined a list of the action identifiers with corresponding namespace URI. Select an action identifier to generate the SAML Authorization statement action."
                        },
                        {
                            "name": "PPSAMLAttributes",
                            "default": "",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLIdentityProvider",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPSAMLAssertionType",
                                            "evaluation": "property-equals",
                                            "value": "attribute"
                                        }
                                    ]
                                }
                            },
                            "summary": "A list of SAML Attribute elements for the SAML assertion postprocessing method.",
                            "cli-alias": "saml-attributes",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/SAMLAttributes"
                                }
                            },
                            "display": "SAML Attribute definition",
                            "description": "Define the information to put in the SAML assertion to generate the Attribute statement. Each SAML attribute requires the Name, NameFormat/Namespace, and Value. The value can be from a DataPower variable carrying predefined format, from a static string, or from the input message."
                        },
                        {
                            "name": "PPLTPAInsertCookie",
                            "default": "on",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Insert a Set-Cookie header in the response.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPLTPA",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPUseWSSec",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ltpa-insert-cookie",
                            "display": "Insert LTPA Set-Cookie",
                            "description": "Insert a Set-Cookie header in the response that contains the LTPA token that is generated during the postprocessing phase."
                        },
                        {
                            "name": "PPTAMPACPropagate",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Place the existing IBM Security Access Manager Privilege Attribute Certificate token in a HTTP header.",
                            "cli-alias": "propagate-tam-pac",
                            "display": "Generate IBM Security Access Manager Privilege Attribute Certificate token",
                            "description": "The IBM Security Access Manager Privilege Attribute Certificate returned from a prior Authentication or Authorization is added to a HTTP header"
                        },
                        {
                            "name": "PPTAMHeader",
                            "default": "iv-creds",
                            "required-when": {
                                "condition": {
                                    "property-name": "PPTAMPACPropagate",
                                    "evaluation": "property-equals",
                                    "value": "on"
                                }
                            },
                            "summary": "The name of the HTTP header to store the token in.",
                            "cli-alias": "tam-header",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPTAMPACPropagate",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Privilege Attribute Certificate header name",
                            "description": "The Privilege Attribute Certificate is stored in the HTTP header with the entered name. The default name is that used by IBM Security Access Manager WebSeal when placing the header in back-end connections."
                        },
                        {
                            "name": "PPTAMHeaderSize",
                            "default": 0,
                            "required-when": {
                                "condition": {
                                    "property-name": "PPTAMPACPropagate",
                                    "evaluation": "property-equals",
                                    "value": "on"
                                }
                            },
                            "summary": "The maximum size of Privilege Attribute Certificate token allowed in a single header entry.",
                            "cli-alias": "tam-header-size",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPTAMPACPropagate",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Privilege Attribute Certificate header value size",
                            "description": "Some servers limit the size of HTTP header values. If the size is not zero then the Privilege Attribute Certificate token will be broken down to multiple headers of this length"
                        },
                        {
                            "name": "PPKerberosUseS4U2Proxy",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Uses S4U2Proxy (constrained delegation) during the authentication step to generate Kerberos tokens in this step.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "kerberos"
                                        },
                                        {
                                            "evaluation": "logical-and",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "kerberos-use-s4u2proxy",
                            "display": "Use constrained delegation when generating Kerberos AP-REQ or SPNEGO tokens in this step.",
                            "description": "Define whether to use constrained delegation during the authentication step to generate this step's Kerberos tokens in order to preserve the identity from the original incoming Kerberos token."
                        },
                        {
                            "name": "PPCookieAttributes",
                            "default": "",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CookieAttributePolicy"
                                }
                            },
                            "summary": "Use a cookie attribute policy to include additional attributes in the cookie",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPLTPA",
                                            "evaluation": "property-does-not-equal",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPLTPAInsertCookie",
                                            "evaluation": "property-does-not-equal",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "cookie-attributes",
                            "display": "Cookie attribute policy",
                            "description": "Defines a policy for including standard or custom attributes in the cookie. The response message that contains a Set-Cookie header is updated with the attributes defined in the selected policy."
                        },
                        {
                            "name": "PPKerberosUseS4U2SelfAndS4U2Proxy",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Uses S4U2Self (protocol transition) to generate a token to the DataPower DataPower Gateway and subsequently uses S4U2Proxy (constrained delegation) to generate Kerberos tokens in this step.",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-equals",
                                            "value": "kerberos"
                                        },
                                        {
                                            "evaluation": "logical-and",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "off"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "kerberos-use-s4u2self",
                            "display": "Use protocol transition and constrained delegation when generating Kerberos AP-REQ or SPNEGO tokens in this step.",
                            "description": "Controls whether to use protocol transition to generate this step's Kerberos tokens to the DataPower DataPower Gateway to transition from non-Kerberos authentication to Kerberos authentication and subsequently preserve the client identity in the Kerberos token that is generated in this step."
                        },
                        {
                            "name": "PPKerberosClientSource",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "kerberos"
                                        },
                                        {
                                            "property-name": "PPKerberosUseS4U2SelfAndS4U2Proxy",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "summary": "Where to get the Kerberos client principal",
                            "cli-alias": "kerberos-client-source",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmPPKerberosClientSourceType"
                            },
                            "display": "Kerberos client principal source",
                            "description": "Specifies the source of the principal name of the Kerberos client. By default, the output of credential mapping in this AAA policy is used as the client principal name. The client principal is based on the authenticated identity that is followed by the corresponding realm name. For example, if the authenticated user is alice, the client principal name can be HTTP/alice.datapower.com@DATAPOWER.COM. The client principal must be present in the KDC for S4U2Self (protocol transition) to work."
                        },
                        {
                            "name": "PPKerberosSelf",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "kerberos"
                                        },
                                        {
                                            "property-name": "PPKerberosUseS4U2SelfAndS4U2Proxy",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "summary": "The principal name of the DataPower Gateway",
                            "cli-alias": "kerberos-self-principal",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Kerberos self principal",
                            "description": "Specifies the principal name of the DataPower Gateway when the DataPower Gateway supports S4U2Self that is known as protocol transition. S4U2Self allows the DataPower Gateway to obtain a service ticket from the KDC to itself on behalf of the user that authenticates to the DataPower Gateway by using a non-Kerberos mechanism, for example, by using an LTPA token."
                        },
                        {
                            "name": "PPKerberosSelfKeytab",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "kerberos"
                                        },
                                        {
                                            "property-name": "PPKerberosUseS4U2SelfAndS4U2Proxy",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "summary": "The keytab for the DataPower DataPower Gateway",
                            "cli-alias": "kerberos-self-keytab",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/CryptoKerberosKeytab"
                                }
                            },
                            "display": "Kerberos self keytab",
                            "description": "Specifies the name of an existing Kerberos keytab configuration that defines the keytab for the DataPower DataPower Gateway. This keytab is required to authenticate the DataPower Gateway to the KDC."
                        },
                        {
                            "name": "PPKerberosClientCustomURL",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "kerberos"
                                        },
                                        {
                                            "property-name": "PPKerberosUseS4U2SelfAndS4U2Proxy",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPKerberosClientSource",
                                            "evaluation": "property-equals",
                                            "value": "custom-url"
                                        }
                                    ]
                                }
                            },
                            "summary": "Specify the URL of the custom stylesheet or GatewayScript file to use the value of its output as the Kerberos client principal",
                            "cli-alias": "kerberos-client-custom-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Kerberos client principal - custom processing",
                            "description": "Specifies the URL of a custom stylesheet or GatewayScript file. This stylesheet or GatewayScript file returns the client principal name within the &lt;tt>kerberos-client-principal&lt;/tt> element. This stylesheet or GatewayScript file gets the following input: &lt;ul>&lt;li>The output of all the steps that are executed in this AAA action&lt;/li>&lt;li>The incoming request message&lt;/li>&lt;/ul>"
                        },
                        {
                            "name": "PPKerberosClientCtxVar",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "AUMethod",
                                            "evaluation": "property-does-not-equal",
                                            "value": "kerberos"
                                        },
                                        {
                                            "property-name": "PPKerberosUseS4U2SelfAndS4U2Proxy",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPKerberosClientSource",
                                            "evaluation": "property-equals",
                                            "value": "ctx-var"
                                        }
                                    ]
                                }
                            },
                            "summary": "Enter a context variable to use its value as the Kerberos client principal",
                            "cli-alias": "kerberos-client-ctx-var",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Kerberos client principal - context variable",
                            "description": "Specifies the context variable. The value of this context variable is used as the Kerberos client principal. This context variable must be specified in the var://context/name format. For example, var://context/AAA/krb-client-princ. You can use the set variable action to set this variable before you define the AAA policy."
                        },
                        {
                            "name": "PPKerberosServerSource",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPKerberosTicket",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        },
                                        {
                                            "property-name": "PPKerberosSPNEGOToken",
                                            "evaluation": "property-equals",
                                            "value": "on"
                                        }
                                    ]
                                }
                            },
                            "summary": "Where to get the Kerberos server principal",
                            "cli-alias": "kerberos-server-source",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmPPKerberosServerSourceType"
                            },
                            "display": "Kerberos server principal source",
                            "description": "Specifies the source of the principal name of the Kerberos server. By default, the server principal name is the value that is specified by the Kerberos server principal property."
                        },
                        {
                            "name": "PPKerberosServerCustomURL",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "PPKerberosServerSource",
                                            "evaluation": "property-equals",
                                            "value": "custom-url"
                                        }
                                    ]
                                }
                            },
                            "summary": "Specify the URL of the custom stylesheet or GatewayScript file to use the value of its output as the Kerberos server principal",
                            "cli-alias": "kerberos-server-custom-url",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmURL"
                            },
                            "display": "Kerberos server principal - custom processing",
                            "description": "&lt;p>Specifies the location of a custom stylesheet or GatewayScript file. This stylesheet or GatewayScript file returns the server principal name within the &lt;tt>kerberos-server-principal&lt;/tt> element. This stylesheet or GatewayScript file gets the following input:&lt;/p>&lt;ul>&lt;li>If constrained delegation is used, the output of only the identity extraction step&lt;/li>&lt;li>If constrained delegation is not used, the output of all the steps that are executed in this AAA action&lt;/li>&lt;li>The incoming request message&lt;/li>&lt;/ul>"
                        },
                        {
                            "name": "PPKerberosServerCtxVar",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "evaluation": "logical-or",
                                            "condition": [
                                                {
                                                    "property-name": "PPKerberosTicket",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPKerberosSPNEGOToken",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                }
                                            ]
                                        },
                                        {
                                            "property-name": "PPKerberosServerSource",
                                            "evaluation": "property-equals",
                                            "value": "ctx-var"
                                        }
                                    ]
                                }
                            },
                            "summary": "Enter a context variable to use its value as the Kerberos server principal",
                            "cli-alias": "kerberos-server-ctx-var",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Kerberos server principal - context variable",
                            "description": "Specifies a context variable. The value of this context variable is used as the Kerberos server principal. This context variable must be specified in the var://context/name format. For example, var://context/AAA/krb-server-princ. You can use the set variable action to set this variable before you define the AAA policy."
                        },
                        {
                            "name": "PPSSLClientConfigType",
                            "type": {
                                "href": "/mgmt/types/default/dmSSLClientConfigType"
                            },
                            "summary": "Set the TLS profile type to secure connections between the DataPower Gateway and its targets",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "PPSAMLSendSLO",
                                    "evaluation": "property-equals",
                                    "value": "off"
                                }
                            },
                            "cli-alias": "ssl-client-type",
                            "display": "TLS client type",
                            "description": "The TLS profile type to secure connections between the DataPower Gateway and its targets."
                        },
                        {
                            "name": "PPSSLClientProfile",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/SSLClientProfile"
                                }
                            },
                            "summary": "Set the TLS client profile to secure connections between the DataPower Gateway and its targets",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPSAMLSendSLO",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "property-name": "PPSSLClientConfigType",
                                            "evaluation": "property-does-not-equal",
                                            "value": "client"
                                        }
                                    ]
                                }
                            },
                            "cli-alias": "ssl-client",
                            "display": "TLS client profile",
                            "description": "The TLS client profile to secure connections between the DataPower Gateway and its targets."
                        },
                        {
                            "name": "PPLTPAKeyFilePasswordAlias",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-and",
                                    "condition": [
                                        {
                                            "property-name": "PPLTPAKeyFilePassword",
                                            "evaluation": "property-equals",
                                            "value": ""
                                        },
                                        {
                                            "evaluation": "logical-and",
                                            "condition": [
                                                {
                                                    "property-name": "PPLTPA",
                                                    "evaluation": "property-equals",
                                                    "value": "on"
                                                },
                                                {
                                                    "property-name": "PPLTPAVersion",
                                                    "evaluation": "property-value-in-list",
                                                    "value": [
                                                        "LTPA",
                                                        "LTPA1FIPS",
                                                        "LTPA2",
                                                        "LTPA2WAS7"
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "label": "Key file password alias",
                            "cli-alias": "ltpa-key-file-password-alias",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-or",
                                    "condition": [
                                        {
                                            "property-name": "PPLTPA",
                                            "evaluation": "property-equals",
                                            "value": "off"
                                        },
                                        {
                                            "evaluation": "logical-and",
                                            "condition": [
                                                {
                                                    "property-name": "PPLTPAVersion",
                                                    "evaluation": "property-value-not-in-list",
                                                    "value": [
                                                        "LTPA",
                                                        "LTPA1FIPS",
                                                        "LTPA2",
                                                        "LTPA2WAS7"
                                                    ]
                                                },
                                                {
                                                    "property-name": "PPLTPAVersion",
                                                    "evaluation": "property-value-in-list",
                                                    "value": "LTPADomino"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            "summary": "The password alias of the password that decrypts the LTPA key file.",
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/PasswordAlias"
                                }
                            },
                            "display": "LTPA key file password alias",
                            "hoverhelp": "Enter the password alias of the password that decrypts the LTPA key file.",
                            "description": "The key file password decrypts certain entries in a WebSphere LTPA key file (v1 and v2). This password is not applicable to Domino key files."
                        },
                        {
                            "name": "PPJWT",
                            "default": "off",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "summary": "Specify whether to generate a JWT token.",
                            "cli-alias": "jwt",
                            "display": "Generate a JWT token",
                            "description": "Control whether to generate a JWT token."
                        },
                        {
                            "name": "PPJWTGenerator",
                            "required-when": {
                                "condition": {
                                    "property-name": "PPJWT",
                                    "evaluation": "property-equals",
                                    "value": "on"
                                }
                            },
                            "summary": "Configure the JWT Generator.",
                            "cli-alias": "generate-jwt",
                            "ignored-when": {
                                "condition": {
                                    "evaluation": "logical-true"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmReference",
                                "reference-to": {
                                    "href": "/mgmt/metadata/default/AAAJWTGenerator"
                                }
                            },
                            "display": "JWT Generator settings",
                            "description": "Configure settings for JWT Generator, such as the credentials and generating methods."
                        }
                    ]
                },
                "name": "dmAAAPPostProcess",
                "summary": "Postprocessing to perform."
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmSAMLAttributeNameAndValue"
                },
                "self": {
                    "href": "/mgmt/types/default/dmSAMLAttributeNameAndValue"
                }
            },
            "type": {
                "name": "dmSAMLAttributeNameAndValue",
                "properties": {
                    "property": [
                        {
                            "name": "URI",
                            "default": "",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-false"
                                }
                            },
                            "summary": "Namespace URI for the attribute.",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Namespace URI",
                            "description": "&lt;p>The Namespace URI for the attribute. The Namespace URI must match on a name. If blank, uses the null namespace.&lt;/p>&lt;p>For example, \"http://www.examples.com\" would match a message with the following attribute:&lt;/p>&lt;p>&amp;lt;Attribute AttributeName=\"cats\" AttributeNamespace=\"http://www.example.com\"> &amp;lt;AttributeValue>Winchester&amp;lt;/AttributeValue>&amp;lt;Attribute>&lt;/p>"
                        },
                        {
                            "description": "&lt;p>The local name of the attribute. For example, \"cats\" would match a message with the following attribute:&lt;/p>&lt;p>&amp;lt;Attribute AttributeName=\"cats\" AttributeNamespace=\"http://www.example.com\"> &amp;lt;AttributeValue>Winchester&amp;lt;/AttributeValue>&amp;lt;Attribute>&lt;/p>",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-false"
                                }
                            },
                            "summary": "Local name of the attribute.",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Local name",
                            "name": "LocalName"
                        },
                        {
                            "name": "Value",
                            "default": "",
                            "required-when": {
                                "condition": {
                                    "evaluation": "logical-false"
                                }
                            },
                            "summary": "Value for the attribute.",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "Attribute value",
                            "description": "&lt;p>The value for the attribute with the corresponding name. For example, \"Winchester\" would match the following attribute:&lt;/p>&lt;p>&amp;lt;Attribute AttributeName=\"cats\" AttributeNamespace=\"http://www.example.com\"> &amp;lt;AttributeValue>Winchester&amp;lt;/AttributeValue>&amp;lt;Attribute>&lt;/p>"
                        }
                    ]
                }
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmLTPAUserAttributeNameAndValue"
                },
                "self": {
                    "href": "/mgmt/types/default/dmLTPAUserAttributeNameAndValue"
                }
            },
            "type": {
                "name": "dmLTPAUserAttributeNameAndValue",
                "properties": {
                    "property": [
                        {
                            "description": "Specify the name of the user attribute included in the generated token. LTPA attributes are relevant for only WebSphere LTPA tokens.",
                            "required": "true",
                            "summary": "Name of the user attribute included in the LTPA token.",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "LTPA user attribute name",
                            "name": "LTPAUserAttributeName"
                        },
                        {
                            "display": "LTPA user attribute type",
                            "type": {
                                "href": "/mgmt/types/default/dmLTPAUserAttributeType"
                            },
                            "description": "Select the type of user attribute.",
                            "name": "LTPAUserAttributeType",
                            "summary": "Type of the LTPA user attribute."
                        },
                        {
                            "description": "Specify the fixed value of the LTPA user attribute. If the value contains the characters '$', ':', or '%', these characters are escaped.",
                            "summary": "Static value of the user attribute included in the LTPA token.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "LTPAUserAttributeType",
                                    "evaluation": "property-does-not-equal",
                                    "value": "static"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "display": "LTPA user attribute static value",
                            "name": "LTPAUserAttributeStaticValue"
                        },
                        {
                            "description": "Specify the XPath expression or use the XPath Tool to create the XPath expression to be evaluated against the input message at runtime. The result of which will be set as the value of the attribute.",
                            "summary": "XPath expression that evaluates to the value of the user attribute included in the LTPA token.",
                            "ignored-when": {
                                "condition": {
                                    "property-name": "LTPAUserAttributeType",
                                    "evaluation": "property-does-not-equal",
                                    "value": "xpath"
                                }
                            },
                            "type": {
                                "href": "/mgmt/types/default/dmXPathExpr"
                            },
                            "display": "LTPA user attribute XPath value",
                            "name": "LTPAUserAttributeXPathValue"
                        }
                    ]
                }
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmAAATransactionPriority"
                },
                "self": {
                    "href": "/mgmt/types/default/dmAAATransactionPriority"
                }
            },
            "type": {
                "name": "dmAAATransactionPriority",
                "properties": {
                    "property": [
                        {
                            "display": "Credential name",
                            "required": "true",
                            "type": {
                                "href": "/mgmt/types/default/dmString"
                            },
                            "description": "Mapped credential name",
                            "name": "Credential"
                        },
                        {
                            "display": "Transaction priority",
                            "required": "true",
                            "type": {
                                "href": "/mgmt/types/default/dmSchedulerPriority"
                            },
                            "description": "Control the transaction scheduling priority. When system resources are in high demand. High priority services are favored over lower priority services.",
                            "name": "Priority"
                        },
                        {
                            "default": "off",
                            "display": "Require authorization",
                            "type": {
                                "href": "/mgmt/types/default/dmToggle"
                            },
                            "description": "Require authorization",
                            "name": "Authorization"
                        }
                    ]
                }
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmCryptoHashAlgorithm"
                },
                "self": {
                    "href": "/mgmt/types/default/dmCryptoHashAlgorithm"
                }
            },
            "type": {
                "display": "Message Digest Algorithm",
                "description": "The hash algorithm for the generated message digest.",
                "value-list": {
                    "value": [
                        {
                            "display": "sha1",
                            "description": "http://www.w3.org/2000/09/xmldsig#sha1",
                            "name": "sha1"
                        },
                        {
                            "display": "sha256",
                            "description": "http://www.w3.org/2001/04/xmlenc#sha256",
                            "name": "sha256"
                        },
                        {
                            "display": "sha512",
                            "description": "http://www.w3.org/2001/04/xmlenc#sha512",
                            "name": "sha512"
                        },
                        {
                            "display": "ripemd160",
                            "description": "http://www.w3.org/2001/04/xmlenc#ripemd160",
                            "name": "ripemd160"
                        },
                        {
                            "display": "sha224",
                            "description": "http://www.w3.org/2001/04/xmldsig-more#sha224",
                            "name": "sha224"
                        },
                        {
                            "display": "sha384",
                            "description": "http://www.w3.org/2001/04/xmldsig-more#sha384",
                            "name": "sha384"
                        },
                        {
                            "display": "md5",
                            "description": "http://www.w3.org/2001/04/xmldsig-more#md5",
                            "name": "md5"
                        }
                    ]
                },
                "name": "dmCryptoHashAlgorithm"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmCryptoSigningAlgorithm"
                },
                "self": {
                    "href": "/mgmt/types/default/dmCryptoSigningAlgorithm"
                }
            },
            "type": {
                "value-list": {
                    "value": [
                        {
                            "display": "rsa-sha1",
                            "description": "http://www.w3.org/2000/09/xmldsig#rsa-sha1",
                            "name": "rsa-sha1"
                        },
                        {
                            "display": "dsa-sha1",
                            "description": "http://www.w3.org/2000/09/xmldsig#dsa-sha1",
                            "name": "dsa-sha1"
                        },
                        {
                            "display": "rsa-sha256",
                            "description": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
                            "name": "rsa-sha256"
                        },
                        {
                            "display": "rsa-sha384",
                            "description": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha384",
                            "name": "rsa-sha384"
                        },
                        {
                            "display": "rsa-sha512",
                            "description": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha512",
                            "name": "rsa-sha512"
                        },
                        {
                            "display": "rsa-ripemd160",
                            "description": "http://www.w3.org/2001/04/xmldsig-more/rsa-ripemd160",
                            "name": "rsa-ripemd160"
                        },
                        {
                            "display": "rsa-ripemd160-2010",
                            "description": "http://www.w3.org/2001/04/xmldsig-more#rsa-ripemd160",
                            "name": "rsa-ripemd160-2010"
                        },
                        {
                            "display": "rsa-md5",
                            "description": "http://www.w3.org/2001/04/xmldsig-more#rsa-md5",
                            "name": "rsa-md5"
                        },
                        {
                            "display": "rsa",
                            "description": "http://www.w3.org/2000/09/xmldsig#rsa-sha1",
                            "name": "rsa"
                        },
                        {
                            "display": "dsa",
                            "description": "http://www.w3.org/2000/09/xmldsig#dsa-sha1",
                            "name": "dsa"
                        }
                    ]
                },
                "display": "Signing algorithm",
                "description": "The signature method for signing.",
                "name": "dmCryptoSigningAlgorithm",
                "summary": "Signature method for signing."
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
                            "name": "on",
                            "display": "on"
                        },
                        {
                            "name": "off",
                            "display": "off"
                        }
                    ]
                }
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmLogLevel"
                },
                "self": {
                    "href": "/mgmt/types/default/dmLogLevel"
                }
            },
            "type": {
                "display": "Log Level",
                "name": "dmLogLevel",
                "value-list": {
                    "value": [
                        {
                            "display": "emergency",
                            "description": "An emergency-level message. The system is unusable.",
                            "name": "emerg",
                            "summary": "System unusable"
                        },
                        {
                            "display": "alert",
                            "description": "An alert-level message. Immediate action must be taken.",
                            "name": "alert",
                            "summary": "Immediate action required"
                        },
                        {
                            "display": "critical",
                            "description": "A critical message. Immediate action should be taken.",
                            "name": "critic",
                            "summary": "Critical condition"
                        },
                        {
                            "display": "error",
                            "description": "An error message. Processing might continue, but action should be taken.",
                            "name": "error",
                            "summary": "Error condition"
                        },
                        {
                            "display": "warning",
                            "description": "A warning message. Processing should continue, but action should be taken.",
                            "name": "warn",
                            "summary": "Warning condition"
                        },
                        {
                            "display": "notice",
                            "description": "A notice message. Processing continues, but action might need to be taken.",
                            "name": "notice",
                            "summary": "Normal but significant condition"
                        },
                        {
                            "display": "information",
                            "description": "An information message. No action required.",
                            "name": "info",
                            "summary": "Informational message"
                        },
                        {
                            "display": "debug",
                            "description": "A debug message for processing information to help during troubleshooting.",
                            "name": "debug",
                            "summary": "Debug message"
                        }
                    ]
                },
                "summary": "Log level"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmFSFile"
                },
                "self": {
                    "href": "/mgmt/types/default/dmFSFile"
                }
            },
            "type": {
                "cli-arg": "file",
                "name": "dmFSFile"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmUInt16"
                },
                "self": {
                    "href": "/mgmt/types/default/dmUInt16"
                }
            },
            "type": {
                "cli-arg": "number",
                "minimum": 0,
                "name": "dmUInt16",
                "maximum": "0xFFFF"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmLDAPVersion"
                },
                "self": {
                    "href": "/mgmt/types/default/dmLDAPVersion"
                }
            },
            "type": {
                "name": "dmLDAPVersion",
                "value-list": {
                    "value": [
                        {
                            "display": "v2",
                            "name": "v2",
                            "summary": "LDAP v2"
                        },
                        {
                            "display": "v3",
                            "name": "v3",
                            "summary": "LDAP v3"
                        }
                    ]
                },
                "summary": "LDAP Version"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmDynConfigType"
                },
                "self": {
                    "href": "/mgmt/types/default/dmDynConfigType"
                }
            },
            "type": {
                "name": "dmDynConfigType",
                "value-list": {
                    "value": [
                        {
                            "display": "None",
                            "description": "Do not use dynamic configuration. Users must define the configuration of the AAA policy at commit time.",
                            "name": "none",
                            "summary": ""
                        },
                        {
                            "display": "Current AAA policy as template",
                            "description": "Use dynamic configuration and use the configuration of the current AAA policy as the template. When selected, the properties that the dynamic configuration custom URL returns overwrite those in the current AAA policy.",
                            "name": "current-aaa",
                            "summary": ""
                        },
                        {
                            "display": "External AAA policy as template",
                            "description": "Use dynamic configuration and use the configuration of an external AAA policy as the template. When selected, the external AAA policy overwrites the current AAA policy. Then the properties that the dynamic configuration URL returns overwrite those in the specified external AAA policy.",
                            "name": "external-aaa",
                            "summary": ""
                        }
                    ]
                },
                "display": "Dynamic configuration"
            }
        },
        {
            "_links": {
                "doc": {
                    "href": "/mgmt/docs/types/dmURL"
                },
                "self": {
                    "href": "/mgmt/types/default/dmURL"
                }
            },
            "type": {
                "cli-arg": "url",
                "name": "dmURL"
            }
        }
    ],
    "metadata": {
        "object": {
            "licensed-feature": "IDG",
            "name": "AAAPolicy",
            "display": "AAA Policy",
            "property-group": [
                {
                    "member": [
                        {
                            "name": "mAdminState"
                        },
                        {
                            "name": "UserSummary"
                        },
                        {
                            "name": "DynConfig"
                        },
                        {
                            "name": "ExternalAAATemplate"
                        },
                        {
                            "name": "DynConfigCustomURL"
                        },
                        {
                            "name": "AuthorizedCounter"
                        },
                        {
                            "name": "RejectedCounter"
                        },
                        {
                            "name": "SAMLValcred"
                        },
                        {
                            "name": "SAMLSigningKey"
                        },
                        {
                            "name": "SAMLSigningCert"
                        },
                        {
                            "name": "SAMLSigningHashAlg"
                        },
                        {
                            "name": "SAMLSigningAlg"
                        },
                        {
                            "name": "LDAPsuffix"
                        },
                        {
                            "name": "LogAllowed"
                        },
                        {
                            "name": "LogAllowedLevel"
                        },
                        {
                            "name": "LogRejected"
                        },
                        {
                            "name": "LogRejectedLevel"
                        },
                        {
                            "name": "WSSecureConversationCryptoKey"
                        },
                        {
                            "name": "SAMLSourceIDMappingFile"
                        },
                        {
                            "name": "PingIdentityCompatibility"
                        },
                        {
                            "name": "SAML2MetadataFile"
                        },
                        {
                            "name": "DoSValve"
                        },
                        {
                            "name": "LDAPVersion"
                        },
                        {
                            "name": "EnforceSOAPActor"
                        },
                        {
                            "name": "WSSecActorRoleID"
                        }
                    ],
                    "name": "main",
                    "display": "Main"
                },
                {
                    "member": {
                        "name": "UserSummary"
                    },
                    "name": "summary"
                },
                {
                    "member": {
                        "name": "ExtractIdentity"
                    },
                    "name": "Identity",
                    "display": "Identity extraction"
                },
                {
                    "member": [
                        {
                            "name": "Authenticate"
                        },
                        {
                            "name": "AUSMHTTPHeader"
                        }
                    ],
                    "name": "Authenticate",
                    "display": "Authentication"
                },
                {
                    "member": {
                        "name": "MapCredentials"
                    },
                    "name": "MapCredentials",
                    "display": "Credential mapping"
                },
                {
                    "member": {
                        "name": "ExtractResource"
                    },
                    "name": "Resource",
                    "display": "Resource extraction"
                },
                {
                    "member": {
                        "name": "MapResource"
                    },
                    "name": "MapResource",
                    "display": "Resource mapping"
                },
                {
                    "member": [
                        {
                            "name": "Authorize"
                        },
                        {
                            "name": "AZSMHTTPHeader"
                        }
                    ],
                    "name": "Authorize",
                    "display": "Authorization"
                },
                {
                    "member": {
                        "name": "PostProcess"
                    },
                    "name": "PostProcessing",
                    "display": "Postprocessing"
                }
            ],
            "uri": "xml/aaapolicy",
            "actions": {
                "action": {
                    "name": "FlushAAACache",
                    "parameters": {
                        "parameter": {
                            "name": "PolicyName",
                            "select": "dmObjectName"
                        }
                    },
                    "display": "Flush cache"
                }
            },
            "summary": "A description of the policy for doing authentication and authorization.",
            "cmd-group": "aaapolicy",
            "cli-alias": "aaapolicy",
            "properties": {
                "property": [
                    {
                        "name": "mAdminState",
                        "default": "enabled",
                        "type": {
                            "href": "/mgmt/types/default/dmAdminState"
                        },
                        "label": "Enable administrative state",
                        "summary": "Set the administrative state of this configuration.",
                        "cli-alias": "admin-state",
                        "display": "Administrative state",
                        "hoverhelp": "&lt;p>Set the administrative state of the configuration.&lt;/p>&lt;ul>&lt;li>To make active, set the check box.&lt;/li>&lt;li>To make inactive, clear the check box.&lt;/li>&lt;/ul>",
                        "description": "&lt;p>The administrative state of the configuration.&lt;/p>&lt;ul>&lt;li>To make active, set to enabled.&lt;/li>&lt;li>To make inactive, set to disabled.&lt;/li>&lt;/ul>"
                    },
                    {
                        "type": {
                            "href": "/mgmt/types/default/dmString"
                        },
                        "display": "Comments",
                        "cli-alias": "summary",
                        "name": "UserSummary",
                        "summary": "Brief summary for user annotation."
                    },
                    {
                        "type": {
                            "href": "/mgmt/types/default/dmReference",
                            "reference-to": {
                                "href": "/mgmt/metadata/default/CountMonitor"
                            }
                        },
                        "display": "Authorized counter",
                        "cli-alias": "authorized-counter",
                        "name": "AuthorizedCounter",
                        "summary": "Monitor for authorized messages. The count monitor should be configured with an XPath as the measure."
                    },
                    {
                        "type": {
                            "href": "/mgmt/types/default/dmReference",
                            "reference-to": {
                                "href": "/mgmt/metadata/default/CountMonitor"
                            }
                        },
                        "display": "Rejected counter",
                        "cli-alias": "rejected-counter",
                        "name": "RejectedCounter",
                        "summary": "Monitor for rejected messages. The count monitor should be configured with an XPath as the measure."
                    },
                    {
                        "name": "NamespaceMapping",
                        "type": {
                            "href": "/mgmt/types/default/dmNamespaceMapping"
                        },
                        "summary": "Map namespaces to Namespace URIs.",
                        "array": "true",
                        "cli-alias": "namespace-mapping",
                        "display": "Namespace mapping",
                        "description": "Establishes namespace mappings for namespaces that might be encountered in requests. A mapping is a prefix and URI."
                    },
                    {
                        "name": "ExtractIdentity",
                        "type": {
                            "href": "/mgmt/types/default/dmAAAPExtractIdentity"
                        },
                        "required": "true",
                        "summary": "How to extract identity information.",
                        "cli-alias": "extract-identity",
                        "display": "Identity extraction",
                        "description": "Select a method to extract the identity claimed or asserted in the service request."
                    },
                    {
                        "name": "Authenticate",
                        "type": {
                            "href": "/mgmt/types/default/dmAAAPAuthenticate"
                        },
                        "required": "true",
                        "summary": "How to authenticate the identity.",
                        "cli-alias": "authenticate",
                        "display": "Authentication",
                        "description": "Select a method to authenticate the extracted identity."
                    },
                    {
                        "name": "MapCredentials",
                        "type": {
                            "href": "/mgmt/types/default/dmAAAPMapCredentials"
                        },
                        "required": "true",
                        "summary": "How to map credentials to what can be used for authorization.",
                        "cli-alias": "map-credentials",
                        "display": "Credential mapping"
                    },
                    {
                        "name": "ExtractResource",
                        "type": {
                            "href": "/mgmt/types/default/dmAAAPExtractResource"
                        },
                        "required": "true",
                        "summary": "How to extract resource information.",
                        "cli-alias": "extract-resource",
                        "display": "Resource extraction"
                    },
                    {
                        "name": "MapResource",
                        "type": {
                            "href": "/mgmt/types/default/dmAAAPMapResource"
                        },
                        "required": "true",
                        "summary": "How to map resources to what can be used for authorization.",
                        "cli-alias": "map-resource",
                        "display": "Resource mapping"
                    },
                    {
                        "name": "Authorize",
                        "type": {
                            "href": "/mgmt/types/default/dmAAAPAuthorize"
                        },
                        "required": "true",
                        "summary": "How to grant or deny a request.",
                        "cli-alias": "authorize",
                        "display": "Authorization"
                    },
                    {
                        "name": "PostProcess",
                        "type": {
                            "href": "/mgmt/types/default/dmAAAPPostProcess"
                        },
                        "required": "true",
                        "summary": "Which postprocessing activities to perform.",
                        "cli-alias": "post-process",
                        "display": "Postprocessing"
                    },
                    {
                        "name": "SAMLAttribute",
                        "type": {
                            "href": "/mgmt/types/default/dmSAMLAttributeNameAndValue"
                        },
                        "summary": "Namespace URI, local name, and expected value of SAML attributes.",
                        "array": "true",
                        "cli-alias": "saml-attribute",
                        "display": "SAML attributes"
                    },
                    {
                        "name": "LTPAAttributes",
                        "type": {
                            "href": "/mgmt/types/default/dmLTPAUserAttributeNameAndValue"
                        },
                        "summary": "User attribute name-value pairs encoded in the generated LTPA token.",
                        "array": "true",
                        "cli-alias": "ltpa-attribute",
                        "display": "LTPA user attributes"
                    },
                    {
                        "name": "TransactionPriority",
                        "type": {
                            "href": "/mgmt/types/default/dmAAATransactionPriority"
                        },
                        "summary": "Transaction priority.",
                        "array": "true",
                        "cli-alias": "transaction-priority",
                        "display": "Transaction priority"
                    },
                    {
                        "type": {
                            "href": "/mgmt/types/default/dmReference",
                            "reference-to": {
                                "href": "/mgmt/metadata/default/CryptoValCred"
                            }
                        },
                        "display": "SAML signature validation credentials",
                        "cli-alias": "saml-valcred",
                        "name": "SAMLValcred",
                        "summary": "SAML signature validation credentials."
                    },
                    {
                        "type": {
                            "href": "/mgmt/types/default/dmReference",
                            "reference-to": {
                                "href": "/mgmt/metadata/default/CryptoKey"
                            }
                        },
                        "display": "SAML message signing key",
                        "cli-alias": "saml-sign-key",
                        "name": "SAMLSigningKey",
                        "summary": "SAML message signing key."
                    },
                    {
                        "type": {
                            "href": "/mgmt/types/default/dmReference",
                            "reference-to": {
                                "href": "/mgmt/metadata/default/CryptoCertificate"
                            }
                        },
                        "display": "SAML message signing certificate",
                        "cli-alias": "saml-sign-cert",
                        "name": "SAMLSigningCert",
                        "summary": "SAML message signing certificate."
                    },
                    {
                        "type": {
                            "href": "/mgmt/types/default/dmCryptoHashAlgorithm"
                        },
                        "display": "SAML signing message digest algorithm",
                        "cli-alias": "saml-sign-hash",
                        "name": "SAMLSigningHashAlg",
                        "summary": "The hash algorithm used for SAML signing message."
                    },
                    {
                        "description": "Select the algorithm to sign SAML messages. rsa and dsa are supported by older releases. rsa is same as rsa-sha1. dsa is same as dsa-sha1.",
                        "type": {
                            "href": "/mgmt/types/default/dmCryptoSigningAlgorithm"
                        },
                        "summary": "Algorithm to sign SAML messages.",
                        "cli-alias": "saml-sign-alg",
                        "display": "SAML message signing algorithm",
                        "name": "SAMLSigningAlg"
                    },
                    {
                        "name": "LDAPsuffix",
                        "default": "",
                        "type": {
                            "href": "/mgmt/types/default/dmString"
                        },
                        "summary": "LDAP suffix.",
                        "cli-alias": "ldap-suffix",
                        "display": "LDAP suffix",
                        "description": "The string to added to the username (separated by a comma) to form a distinguished name (DN) for LDAP authentication. For example, if the string value is \"O=example.com\" and the username is \"Bob\", the LDAP DN is \"CN=Bob,O=example.com\"."
                    },
                    {
                        "name": "LogAllowed",
                        "default": "on",
                        "type": {
                            "href": "/mgmt/types/default/dmToggle"
                        },
                        "required": "true",
                        "summary": "Log allowed AAA attempts.",
                        "cli-alias": "log-allowed",
                        "display": "Log allowed",
                        "description": "Determines whether to log messages about allowed AAA attempts."
                    },
                    {
                        "name": "LogAllowedLevel",
                        "default": "info",
                        "required-when": {
                            "condition": {
                                "property-name": "LogAllowed",
                                "evaluation": "property-equals",
                                "value": "on"
                            }
                        },
                        "summary": "Level to log allowed AAA attempts.",
                        "cli-alias": "log-allowed-level",
                        "ignored-when": {
                            "condition": {
                                "evaluation": "logical-true"
                            }
                        },
                        "type": {
                            "href": "/mgmt/types/default/dmLogLevel"
                        },
                        "display": "Log allowed level",
                        "description": "The level to log messages about allowed AAA attempts."
                    },
                    {
                        "name": "LogRejected",
                        "default": "on",
                        "type": {
                            "href": "/mgmt/types/default/dmToggle"
                        },
                        "required": "true",
                        "summary": "Log rejected AAA attempts.",
                        "cli-alias": "log-rejected",
                        "display": "Log rejected",
                        "description": "Determines whether to log messages about rejected AAA attempts."
                    },
                    {
                        "name": "LogRejectedLevel",
                        "default": "warn",
                        "required-when": {
                            "condition": {
                                "property-name": "LogRejected",
                                "evaluation": "property-equals",
                                "value": "on"
                            }
                        },
                        "summary": "Level to log rejected Level.",
                        "cli-alias": "log-rejected-level",
                        "ignored-when": {
                            "condition": {
                                "evaluation": "logical-true"
                            }
                        },
                        "type": {
                            "href": "/mgmt/types/default/dmLogLevel"
                        },
                        "display": "Log rejected level",
                        "description": "The level to log messages about rejected AAA attempts."
                    },
                    {
                        "description": "When generating a WS-Trust token associated with a secret key (such as a WS-SecureConversation token), use this key to encrypt the initial secret.",
                        "type": {
                            "href": "/mgmt/types/default/dmReference",
                            "reference-to": {
                                "href": "/mgmt/metadata/default/CryptoCertificate"
                            }
                        },
                        "summary": "Certificate that corresponds to the key that encrypts a WS-Trust secret.",
                        "cli-alias": "wstrust-encrypt-key",
                        "display": "WS-Trust encryption recipient certificate",
                        "name": "WSSecureConversationCryptoKey"
                    },
                    {
                        "name": "SAMLSourceIDMappingFile",
                        "type": {
                            "href": "/mgmt/types/default/dmFSFile"
                        },
                        "locations": {
                            "location": [
                                "local",
                                "store"
                            ]
                        },
                        "summary": "File that contains the SAML Artifact mapping.",
                        "cli-alias": "saml-artifact-mapping",
                        "display": "SAML Artifact mapping file",
                        "description": "The file that contains a mapping of SAML Artifact source IDs to artifact retrieval endpoints. This file is required only if artifacts are retrieved from multiple endpoints and the source ID for these endpoints are encoded in the artifact itself, as per the SAML specification. If there is only one artifact retrieval URL, it can be specified by the SAML Artifact responder URL in the authentication phase."
                    },
                    {
                        "name": "PingIdentityCompatibility",
                        "default": "off",
                        "type": {
                            "href": "/mgmt/types/default/dmToggle"
                        },
                        "summary": "PingIdentity compatibility.",
                        "cli-alias": "ping-identity-compatibility",
                        "display": "PingIdentity compatibility",
                        "description": "Enable PingIdentity compatibility when using SAML for authentication or authorization."
                    },
                    {
                        "name": "SAML2MetadataFile",
                        "type": {
                            "href": "/mgmt/types/default/dmFSFile"
                        },
                        "locations": {
                            "location": [
                                "local",
                                "store"
                            ]
                        },
                        "summary": "File that contains SAML 2.0 metadata.",
                        "cli-alias": "saml2-metadata",
                        "display": "SAML 2.0 metadata file",
                        "description": "The file that contains metadata used in SAML 2.0 protocol message exchanges. This metadata is used to identify Identity Provider endpoints and certificates needed to secure SAML 2.0 message exchanges. This file must have a &amp;lt;md:EntitiesDescriptor> top-level element, with one or more &amp;lt;EntityDescriptor> child elements (one per Identity Provider)."
                    },
                    {
                        "name": "DoSValve",
                        "default": 3,
                        "cli-alias": "dos-valve",
                        "maximum": 1000,
                        "summary": "Value to filter out denial-of-service (DoS) attacks.",
                        "minimum": 1,
                        "type": {
                            "href": "/mgmt/types/default/dmUInt16"
                        },
                        "display": "DoS flooding attack valve",
                        "description": "Set the maximum times of same XML processing that AAA policy allows for each user request. The AAA policy assumes that more than this value of the same processing is caused by potential DoS flooding attacks. The AAA policy limits the number of times to process the same request. These processes can include encryption, decryption, message signing, or signature verification. Currently, only identity extraction with subject DN from certificate in message signature and authorization with signer certificate for digitally signed messages support this setting. These methods designate the number of signatures or signing reference URIs. &lt;p>The default value is 3. This value means that the AAA policy processes only the first 3 signature and each signature can contain up to 3 reference URIs. Additional signatures or reference URIs are ignored.&lt;/p>"
                    },
                    {
                        "name": "LDAPVersion",
                        "default": "v2",
                        "type": {
                            "href": "/mgmt/types/default/dmLDAPVersion"
                        },
                        "summary": "Version of the LDAP protocol for bind.",
                        "cli-alias": "ldap-version",
                        "display": "LDAP version",
                        "description": "Select the LDAP protocol version to use for the bind operation. The default value is v2."
                    },
                    {
                        "name": "EnforceSOAPActor",
                        "default": "on",
                        "type": {
                            "href": "/mgmt/types/default/dmToggle"
                        },
                        "summary": "Enforce the S11::actor or S12:role when the message is a WS-Security message.",
                        "cli-alias": "enforce-actor-role",
                        "display": "Enforce actor or role for WS-Security message",
                        "description": "Most of the times a WS-Security message has an S11:actor or S12:role attribute for its wsse:Security header, we can enforce those attributes when AAA tries to utilize wsse:Security header, for example, there should be only one wsse:Security element having same actor/role, and AAA should only process the wsse:Security header for the designated Actor/Role Identifier. This setting takes effect for all AAA steps except postprocessing, which generally generate new message for next SOAP node. The default value for this setting is 'on', enabling SOAP actor/role enforcement."
                    },
                    {
                        "name": "WSSecActorRoleID",
                        "default": "",
                        "type": {
                            "href": "/mgmt/types/default/dmString"
                        },
                        "summary": "The assumed S11:actor or S12:role identifier that the AAA policy act as.",
                        "ignored-when": {
                            "condition": {
                                "property-name": "EnforceSOAPActor",
                                "evaluation": "property-equals",
                                "value": "off"
                            }
                        },
                        "cli-alias": "actor-role-id",
                        "display": "WS-Security actor or role identifier",
                        "description": "If specified, the AAA policy acts as the assumed actor or role when it consumes the wsse:Security headers. This setting takes effect only when the AAA policy tries to process the incoming WS-Security message before making an authorization decision. Postprocessing does not use this setting. Postprocessing uses its own setting in generating WS-Security messages for the next SOAP node. Some well-known values are as follows: &lt;table border=\"1\">&lt;tr>&lt;td valign=\"left\">http://schemas.xmlsoap.org/soap/actor/next&lt;/td>&lt;td>Every one, including the intermediary and ultimate receiver, receives the message should be able to processing the Security header.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">http://www.w3.org/2003/05/soap-envelope/role/none&lt;/td>&lt;td>No one should process the Security Header.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">http://www.w3.org/2003/05/soap-envelope/role/next&lt;/td>&lt;td>Every one, including the intermediary and ultimate receiver, receives the message should be able to processing the Security header.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">http://www.w3.org/2003/05/soap-envelope/role/ultimateReceiver&lt;/td>&lt;td>The message ultimate receiver can process the Security header. This is the default value if such setting is not configured.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">&amp;lt;blank or empty string>&lt;/td>&lt;td>The empty string \"\" (without quotes) indicates that no \"actor/role\" identifier is configured. if there is no actor/role setting configured, the ultimateReceiver is assumed when processing the message, and no actor/role attribute will be added when generating the WS-Security header. There should not be more than one Security headers omitting the actor/role identifier.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">USE_MESSAGE_BASE_URI&lt;/td>&lt;td>The value \"USE_MESSAGE_BASE_URI\" without quotes indicates that the actor/role identifier will be the base URL of the message, if the SOAP message is transported using HTTP, the base URI is the Request-URI of the http request.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">any other customized string&lt;/td>&lt;td>You can input any string to identify the actor or role of the Security header.&lt;/td>&lt;/tr>&lt;/table>&lt;p>The default value is a blank value.&lt;/p>"
                    },
                    {
                        "name": "AUSMHTTPHeader",
                        "type": {
                            "href": "/mgmt/types/default/dmString"
                        },
                        "summary": "HTTP headers of interest from CA Single Sign-on responses to include in responses or requests if configured",
                        "ignored-when": {
                            "condition": {
                                "property-name": "AUSMHeaderFlow",
                                "evaluation": "property-value-not-in-list",
                                "value": [
                                    "frontend",
                                    "backend",
                                    "frontend+backend"
                                ]
                            }
                        },
                        "array": "true",
                        "cli-alias": "au-sm-http-header",
                        "display": "HTTP headers",
                        "description": "Specifies the HTTP headers from CA Single Sign-On responses. When specified, these headers are included into the request or response headers based on the setting of the CA Single Sign-on header flow."
                    },
                    {
                        "name": "AZSMHTTPHeader",
                        "type": {
                            "href": "/mgmt/types/default/dmString"
                        },
                        "summary": "HTTP headers of interest from CA Single Sign-on responses to include in responses or requests if configured",
                        "ignored-when": {
                            "condition": {
                                "property-name": "AZSMHeaderFlow",
                                "evaluation": "property-value-not-in-list",
                                "value": [
                                    "frontend",
                                    "backend",
                                    "frontend+backend"
                                ]
                            }
                        },
                        "array": "true",
                        "cli-alias": "az-sm-http-header",
                        "display": "HTTP headers",
                        "description": "Specifies the HTTP headers from CA Single Sign-On responses. When specified, these headers are included into the request or response headers based on the setting of the CA Single Sign-on header flow."
                    },
                    {
                        "name": "DynConfig",
                        "default": "none",
                        "type": {
                            "href": "/mgmt/types/default/dmDynConfigType"
                        },
                        "required": "true",
                        "summary": "How to obtain the AAA policy configuration dynamically",
                        "cli-alias": "dyn-config",
                        "display": "Dynamic configuration type",
                        "description": "Specifies how to obtain the AAA policy configuration dynamically. Dynamic configuration enables users to configure AAA policy at run time. When enabled, the configuration of AAA is determined dynamically based on the template AAA policy and the parameters that the dynamic configuration custom URL returns."
                    },
                    {
                        "name": "ExternalAAATemplate",
                        "required-when": {
                            "condition": {
                                "property-name": "DynConfig",
                                "evaluation": "property-value-in-list",
                                "value": "external-aaa"
                            }
                        },
                        "summary": "The external AAA policy to use as the template",
                        "cli-alias": "external-aaa-template",
                        "ignored-when": {
                            "condition": {
                                "evaluation": "logical-true"
                            }
                        },
                        "type": {
                            "href": "/mgmt/types/default/dmReference",
                            "reference-to": {
                                "href": "/mgmt/metadata/default/AAAPolicy"
                            }
                        },
                        "display": "External AAA policy template",
                        "description": "Specifies an external AAA policy to use as the template. When specified, it overwrites the configuration of the current AAA policy."
                    },
                    {
                        "name": "DynConfigCustomURL",
                        "required-when": {
                            "condition": {
                                "evaluation": "logical-or",
                                "condition": [
                                    {
                                        "property-name": "DynConfig",
                                        "evaluation": "property-value-in-list",
                                        "value": "current-aaa"
                                    },
                                    {
                                        "property-name": "DynConfig",
                                        "evaluation": "property-value-in-list",
                                        "value": "external-aaa"
                                    }
                                ]
                            }
                        },
                        "summary": "The location of the custom stylesheet or GatewayScript file",
                        "cli-alias": "dyn-config-custom-url",
                        "ignored-when": {
                            "condition": {
                                "evaluation": "logical-true"
                            }
                        },
                        "type": {
                            "href": "/mgmt/types/default/dmURL"
                        },
                        "display": "Dynamic configuration custom URL",
                        "description": "&lt;p>Specifies the location of the custom stylesheet or GatewayScript file where to obtain the AAA policy configuration. The obtained configuration overwrites the configuration that is defined in the template AAA policy. In the custom stylesheet or GatewayScript file, it is recommended that you modify only those properties to be dynamically overwritten in the template AAA policy.&lt;/p>&lt;p>See the &lt;tt>ModifyAAAPolicy&lt;/tt> element in the store:///xml-mgmt.xsd schema to construct a schema-compliant AAA configuration. For the nodeset that the custom URL is expected to return and a sample stylesheet, see the topic in IBM Knowledge Center.&lt;/p>"
                    }
                ]
            },
            "description": "An AAA policy establishes the configuration to support the authentication and authorization of users requesting resources from the back-end servers. An AAA policy consists of the following components. &lt;table>&lt;tr>&lt;td valign=\"top\">Identity extraction&lt;/td>&lt;td>One of many methods that discovers which identity is asserted in the service request. This processing phase answers the question, \"What is your name?\"&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Authentication&lt;/td>&lt;td>One of many methods that authenticates the asserted identity. Methods include communication with external authorities, such as an LDAP server. The identity is accepted as authentic or rejected. When authenticated successfully, the identity is used as a credential.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Resource extraction&lt;/td>&lt;td>One of many methods that discovers which resource service is requested (such as query an account or perform an update) This processing phase answers the question, \"What do you want to do?\"&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Credential mapping&lt;/td>&lt;td>While an identity can be authenticated by one authority as valid, this identity or credential might not be known to the authority that authorizes the requested resource. This processing phase allows the mapping of credentials from one form to another for interoperability between systems.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Resource mapping&lt;/td>&lt;td>While a resource can be identified from the service request, this resource name might not be known to the authority that authorizes use of the requested resource. This processing phase allows the mapping of resource names from one form to another for interoperability between systems.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Authorization&lt;/td>&lt;td>The combination of the authenticated and possibly remapped credential with the requested and possibly remapped resource are submitted to an authority for authorization. That authority could reside elsewhere on the network. The request for service is accepted or rejected.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Postprocessing&lt;/td>&lt;td>Additional processing to perform after authorization, such as the generation of a WS-Trust token or SAML assertion.&lt;/td>&lt;/tr>&lt;/table>"
        },
        "_links": {
            "doc": {
                "href": "/mgmt/docs/metadata/AAAPolicy"
            },
            "self": {
                "href": "/mgmt/metadata/default/AAAPolicy"
            }
        }
    }

}

valcred_schema_response = {
            "types": [
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
            "metadata": {
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
