int_type = {
    "cli-arg": "number",
    "maximum": "0xFFFF",
    "minimum": 0,
    "name": "dmUInt16"
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
    "_links": {
        "self": {
            "href": "/mgmt/metadata/default/AAAPolicy"
        },
        "doc": {
            "href": "/mgmt/docs/metadata/AAAPolicy"
        }
    },
    "object": {
        "name": "AAAPolicy",
        "uri": "xml/aaapolicy",
        "cli-alias": "aaapolicy",
        "cmd-group": "aaapolicy",
        "licensed-feature": "IDG",
        "property-group": [
            {
                "name": "main",
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
                "display": "Main"
            },
            {
                "name": "summary",
                "member": {
                    "name": "UserSummary"
                }
            },
            {
                "name": "Identity",
                "member": {
                    "name": "ExtractIdentity"
                },
                "display": "Identity extraction"
            },
            {
                "name": "Authenticate",
                "member": [
                    {
                        "name": "Authenticate"
                    },
                    {
                        "name": "AUSMHTTPHeader"
                    }
                ],
                "display": "Authentication"
            },
            {
                "name": "MapCredentials",
                "member": {
                    "name": "MapCredentials"
                },
                "display": "Credential mapping"
            },
            {
                "name": "Resource",
                "member": {
                    "name": "ExtractResource"
                },
                "display": "Resource extraction"
            },
            {
                "name": "MapResource",
                "member": {
                    "name": "MapResource"
                },
                "display": "Resource mapping"
            },
            {
                "name": "Authorize",
                "member": [
                    {
                        "name": "Authorize"
                    },
                    {
                        "name": "AZSMHTTPHeader"
                    }
                ],
                "display": "Authorization"
            },
            {
                "name": "PostProcessing",
                "member": {
                    "name": "PostProcess"
                },
                "display": "Postprocessing"
            }
        ],
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
        "display": "AAA Policy",
        "summary": "A description of the policy for doing authentication and authorization.",
        "description": "An AAA policy establishes the configuration to support the authentication and authorization of users requesting resources from the back-end servers. An AAA policy consists of the following components. &lt;table>&lt;tr>&lt;td valign=\"top\">Identity extraction&lt;/td>&lt;td>One of many methods that discovers which identity is asserted in the service request. This processing phase answers the question, \"What is your name?\"&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Authentication&lt;/td>&lt;td>One of many methods that authenticates the asserted identity. Methods include communication with external authorities, such as an LDAP server. The identity is accepted as authentic or rejected. When authenticated successfully, the identity is used as a credential.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Resource extraction&lt;/td>&lt;td>One of many methods that discovers which resource service is requested (such as query an account or perform an update) This processing phase answers the question, \"What do you want to do?\"&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Credential mapping&lt;/td>&lt;td>While an identity can be authenticated by one authority as valid, this identity or credential might not be known to the authority that authorizes the requested resource. This processing phase allows the mapping of credentials from one form to another for interoperability between systems.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Resource mapping&lt;/td>&lt;td>While a resource can be identified from the service request, this resource name might not be known to the authority that authorizes use of the requested resource. This processing phase allows the mapping of resource names from one form to another for interoperability between systems.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Authorization&lt;/td>&lt;td>The combination of the authenticated and possibly remapped credential with the requested and possibly remapped resource are submitted to an authority for authorization. That authority could reside elsewhere on the network. The request for service is accepted or rejected.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"top\">Postprocessing&lt;/td>&lt;td>Additional processing to perform after authorization, such as the generation of a WS-Trust token or SAML assertion.&lt;/td>&lt;/tr>&lt;/table>",
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
                    "name": "UserSummary",
                    "type": {
                        "href": "/mgmt/types/default/dmString"
                    },
                    "cli-alias": "summary",
                    "display": "Comments",
                    "summary": "Brief summary for user annotation."
                },
                {
                    "name": "AuthorizedCounter",
                    "type": {
                        "href": "/mgmt/types/default/dmReference",
                        "reference-to": {
                            "href": "/mgmt/metadata/default/CountMonitor"
                        }
                    },
                    "cli-alias": "authorized-counter",
                    "display": "Authorized counter",
                    "summary": "Monitor for authorized messages. The count monitor should be configured with an XPath as the measure."
                },
                {
                    "name": "RejectedCounter",
                    "type": {
                        "href": "/mgmt/types/default/dmReference",
                        "reference-to": {
                            "href": "/mgmt/metadata/default/CountMonitor"
                        }
                    },
                    "cli-alias": "rejected-counter",
                    "display": "Rejected counter",
                    "summary": "Monitor for rejected messages. The count monitor should be configured with an XPath as the measure."
                },
                {
                    "name": "NamespaceMapping",
                    "array": "true",
                    "type": {
                        "href": "/mgmt/types/default/dmNamespaceMapping"
                    },
                    "cli-alias": "namespace-mapping",
                    "display": "Namespace mapping",
                    "summary": "Map namespaces to Namespace URIs.",
                    "description": "Establishes namespace mappings for namespaces that might be encountered in requests. A mapping is a prefix and URI."
                },
                {
                    "name": "ExtractIdentity",
                    "type": {
                        "href": "/mgmt/types/default/dmAAAPExtractIdentity"
                    },
                    "required": "true",
                    "cli-alias": "extract-identity",
                    "display": "Identity extraction",
                    "summary": "How to extract identity information.",
                    "description": "Select a method to extract the identity claimed or asserted in the service request."
                },
                {
                    "name": "Authenticate",
                    "type": {
                        "href": "/mgmt/types/default/dmAAAPAuthenticate"
                    },
                    "required": "true",
                    "cli-alias": "authenticate",
                    "display": "Authentication",
                    "summary": "How to authenticate the identity.",
                    "description": "Select a method to authenticate the extracted identity."
                },
                {
                    "name": "MapCredentials",
                    "type": {
                        "href": "/mgmt/types/default/dmAAAPMapCredentials"
                    },
                    "required": "true",
                    "cli-alias": "map-credentials",
                    "display": "Credential mapping",
                    "summary": "How to map credentials to what can be used for authorization."
                },
                {
                    "name": "ExtractResource",
                    "type": {
                        "href": "/mgmt/types/default/dmAAAPExtractResource"
                    },
                    "required": "true",
                    "cli-alias": "extract-resource",
                    "display": "Resource extraction",
                    "summary": "How to extract resource information."
                },
                {
                    "name": "MapResource",
                    "type": {
                        "href": "/mgmt/types/default/dmAAAPMapResource"
                    },
                    "required": "true",
                    "cli-alias": "map-resource",
                    "display": "Resource mapping",
                    "summary": "How to map resources to what can be used for authorization."
                },
                {
                    "name": "Authorize",
                    "type": {
                        "href": "/mgmt/types/default/dmAAAPAuthorize"
                    },
                    "required": "true",
                    "cli-alias": "authorize",
                    "display": "Authorization",
                    "summary": "How to grant or deny a request."
                },
                {
                    "name": "PostProcess",
                    "type": {
                        "href": "/mgmt/types/default/dmAAAPPostProcess"
                    },
                    "required": "true",
                    "cli-alias": "post-process",
                    "display": "Postprocessing",
                    "summary": "Which postprocessing activities to perform."
                },
                {
                    "name": "SAMLAttribute",
                    "array": "true",
                    "type": {
                        "href": "/mgmt/types/default/dmSAMLAttributeNameAndValue"
                    },
                    "cli-alias": "saml-attribute",
                    "display": "SAML attributes",
                    "summary": "Namespace URI, local name, and expected value of SAML attributes."
                },
                {
                    "name": "LTPAAttributes",
                    "array": "true",
                    "type": {
                        "href": "/mgmt/types/default/dmLTPAUserAttributeNameAndValue"
                    },
                    "cli-alias": "ltpa-attribute",
                    "display": "LTPA user attributes",
                    "summary": "User attribute name-value pairs encoded in the generated LTPA token."
                },
                {
                    "name": "TransactionPriority",
                    "array": "true",
                    "type": {
                        "href": "/mgmt/types/default/dmAAATransactionPriority"
                    },
                    "cli-alias": "transaction-priority",
                    "display": "Transaction priority",
                    "summary": "Transaction priority."
                },
                {
                    "name": "SAMLValcred",
                    "type": {
                        "href": "/mgmt/types/default/dmReference",
                        "reference-to": {
                            "href": "/mgmt/metadata/default/CryptoValCred"
                        }
                    },
                    "cli-alias": "saml-valcred",
                    "display": "SAML signature validation credentials",
                    "summary": "SAML signature validation credentials."
                },
                {
                    "name": "SAMLSigningKey",
                    "type": {
                        "href": "/mgmt/types/default/dmReference",
                        "reference-to": {
                            "href": "/mgmt/metadata/default/CryptoKey"
                        }
                    },
                    "cli-alias": "saml-sign-key",
                    "display": "SAML message signing key",
                    "summary": "SAML message signing key."
                },
                {
                    "name": "SAMLSigningCert",
                    "type": {
                        "href": "/mgmt/types/default/dmReference",
                        "reference-to": {
                            "href": "/mgmt/metadata/default/CryptoCertificate"
                        }
                    },
                    "cli-alias": "saml-sign-cert",
                    "display": "SAML message signing certificate",
                    "summary": "SAML message signing certificate."
                },
                {
                    "name": "SAMLSigningHashAlg",
                    "type": {
                        "href": "/mgmt/types/default/dmCryptoHashAlgorithm"
                    },
                    "cli-alias": "saml-sign-hash",
                    "display": "SAML signing message digest algorithm",
                    "summary": "The hash algorithm used for SAML signing message."
                },
                {
                    "name": "SAMLSigningAlg",
                    "type": {
                        "href": "/mgmt/types/default/dmCryptoSigningAlgorithm"
                    },
                    "cli-alias": "saml-sign-alg",
                    "display": "SAML message signing algorithm",
                    "summary": "Algorithm to sign SAML messages.",
                    "description": "Select the algorithm to sign SAML messages. rsa and dsa are supported by older releases. rsa is same as rsa-sha1. dsa is same as dsa-sha1."
                },
                {
                    "name": "LDAPsuffix",
                    "type": {
                        "href": "/mgmt/types/default/dmString"
                    },
                    "cli-alias": "ldap-suffix",
                    "default": "",
                    "display": "LDAP suffix",
                    "summary": "LDAP suffix.",
                    "description": "The string to added to the username (separated by a comma) to form a distinguished name (DN) for LDAP authentication. For example, if the string value is \"O=example.com\" and the username is \"Bob\", the LDAP DN is \"CN=Bob,O=example.com\"."
                },
                {
                    "name": "LogAllowed",
                    "type": {
                        "href": "/mgmt/types/default/dmToggle"
                    },
                    "required": "true",
                    "cli-alias": "log-allowed",
                    "default": "on",
                    "display": "Log allowed",
                    "summary": "Log allowed AAA attempts.",
                    "description": "Determines whether to log messages about allowed AAA attempts."
                },
                {
                    "name": "LogAllowedLevel",
                    "type": {
                        "href": "/mgmt/types/default/dmLogLevel"
                    },
                    "cli-alias": "log-allowed-level",
                    "default": "info",
                    "required-when": {
                        "condition": {
                            "evaluation": "property-equals",
                            "property-name": "LogAllowed",
                            "value": "on"
                        }
                    },
                    "ignored-when": {
                        "condition": {
                            "evaluation": "logical-true"
                        }
                    },
                    "display": "Log allowed level",
                    "summary": "Level to log allowed AAA attempts.",
                    "description": "The level to log messages about allowed AAA attempts."
                },
                {
                    "name": "LogRejected",
                    "type": {
                        "href": "/mgmt/types/default/dmToggle"
                    },
                    "required": "true",
                    "cli-alias": "log-rejected",
                    "default": "on",
                    "display": "Log rejected",
                    "summary": "Log rejected AAA attempts.",
                    "description": "Determines whether to log messages about rejected AAA attempts."
                },
                {
                    "name": "LogRejectedLevel",
                    "type": {
                        "href": "/mgmt/types/default/dmLogLevel"
                    },
                    "cli-alias": "log-rejected-level",
                    "default": "warn",
                    "required-when": {
                        "condition": {
                            "evaluation": "property-equals",
                            "property-name": "LogRejected",
                            "value": "on"
                        }
                    },
                    "ignored-when": {
                        "condition": {
                            "evaluation": "logical-true"
                        }
                    },
                    "display": "Log rejected level",
                    "summary": "Level to log rejected Level.",
                    "description": "The level to log messages about rejected AAA attempts."
                },
                {
                    "name": "WSSecureConversationCryptoKey",
                    "type": {
                        "href": "/mgmt/types/default/dmReference",
                        "reference-to": {
                            "href": "/mgmt/metadata/default/CryptoCertificate"
                        }
                    },
                    "cli-alias": "wstrust-encrypt-key",
                    "display": "WS-Trust encryption recipient certificate",
                    "summary": "Certificate that corresponds to the key that encrypts a WS-Trust secret.",
                    "description": "When generating a WS-Trust token associated with a secret key (such as a WS-SecureConversation token), use this key to encrypt the initial secret."
                },
                {
                    "name": "SAMLSourceIDMappingFile",
                    "type": {
                        "href": "/mgmt/types/default/dmFSFile"
                    },
                    "cli-alias": "saml-artifact-mapping",
                    "locations": {
                        "location": [
                            "local",
                            "store"
                        ]
                    },
                    "display": "SAML Artifact mapping file",
                    "summary": "File that contains the SAML Artifact mapping.",
                    "description": "The file that contains a mapping of SAML Artifact source IDs to artifact retrieval endpoints. This file is required only if artifacts are retrieved from multiple endpoints and the source ID for these endpoints are encoded in the artifact itself, as per the SAML specification. If there is only one artifact retrieval URL, it can be specified by the SAML Artifact responder URL in the authentication phase."
                },
                {
                    "name": "PingIdentityCompatibility",
                    "type": {
                        "href": "/mgmt/types/default/dmToggle"
                    },
                    "cli-alias": "ping-identity-compatibility",
                    "default": "off",
                    "display": "PingIdentity compatibility",
                    "summary": "PingIdentity compatibility.",
                    "description": "Enable PingIdentity compatibility when using SAML for authentication or authorization."
                },
                {
                    "name": "SAML2MetadataFile",
                    "type": {
                        "href": "/mgmt/types/default/dmFSFile"
                    },
                    "cli-alias": "saml2-metadata",
                    "locations": {
                        "location": [
                            "local",
                            "store"
                        ]
                    },
                    "display": "SAML 2.0 metadata file",
                    "summary": "File that contains SAML 2.0 metadata.",
                    "description": "The file that contains metadata used in SAML 2.0 protocol message exchanges. This metadata is used to identify Identity Provider endpoints and certificates needed to secure SAML 2.0 message exchanges. This file must have a &amp;lt;md:EntitiesDescriptor> top-level element, with one or more &amp;lt;EntityDescriptor> child elements (one per Identity Provider)."
                },
                {
                    "name": "DoSValve",
                    "type": {
                        "href": "/mgmt/types/default/dmUInt16"
                    },
                    "cli-alias": "dos-valve",
                    "minimum": 1,
                    "maximum": 1000,
                    "default": 3,
                    "display": "DoS flooding attack valve",
                    "summary": "Value to filter out denial-of-service (DoS) attacks.",
                    "description": "Set the maximum times of same XML processing that AAA policy allows for each user request. The AAA policy assumes that more than this value of the same processing is caused by potential DoS flooding attacks. The AAA policy limits the number of times to process the same request. These processes can include encryption, decryption, message signing, or signature verification. Currently, only identity extraction with subject DN from certificate in message signature and authorization with signer certificate for digitally signed messages support this setting. These methods designate the number of signatures or signing reference URIs. &lt;p>The default value is 3. This value means that the AAA policy processes only the first 3 signature and each signature can contain up to 3 reference URIs. Additional signatures or reference URIs are ignored.&lt;/p>"
                },
                {
                    "name": "LDAPVersion",
                    "type": {
                        "href": "/mgmt/types/default/dmLDAPVersion"
                    },
                    "cli-alias": "ldap-version",
                    "default": "v2",
                    "display": "LDAP version",
                    "summary": "Version of the LDAP protocol for bind.",
                    "description": "Select the LDAP protocol version to use for the bind operation. The default value is v2."
                },
                {
                    "name": "EnforceSOAPActor",
                    "type": {
                        "href": "/mgmt/types/default/dmToggle"
                    },
                    "cli-alias": "enforce-actor-role",
                    "default": "on",
                    "display": "Enforce actor or role for WS-Security message",
                    "summary": "Enforce the S11::actor or S12:role when the message is a WS-Security message.",
                    "description": "Most of the times a WS-Security message has an S11:actor or S12:role attribute for its wsse:Security header, we can enforce those attributes when AAA tries to utilize wsse:Security header, for example, there should be only one wsse:Security element having same actor/role, and AAA should only process the wsse:Security header for the designated Actor/Role Identifier. This setting takes effect for all AAA steps except postprocessing, which generally generate new message for next SOAP node. The default value for this setting is 'on', enabling SOAP actor/role enforcement."
                },
                {
                    "name": "WSSecActorRoleID",
                    "type": {
                        "href": "/mgmt/types/default/dmString"
                    },
                    "cli-alias": "actor-role-id",
                    "default": "",
                    "ignored-when": {
                        "condition": {
                            "evaluation": "property-equals",
                            "property-name": "EnforceSOAPActor",
                            "value": "off"
                        }
                    },
                    "display": "WS-Security actor or role identifier",
                    "summary": "The assumed S11:actor or S12:role identifier that the AAA policy act as.",
                    "description": "If specified, the AAA policy acts as the assumed actor or role when it consumes the wsse:Security headers. This setting takes effect only when the AAA policy tries to process the incoming WS-Security message before making an authorization decision. Postprocessing does not use this setting. Postprocessing uses its own setting in generating WS-Security messages for the next SOAP node. Some well-known values are as follows: &lt;table border=\"1\">&lt;tr>&lt;td valign=\"left\">http://schemas.xmlsoap.org/soap/actor/next&lt;/td>&lt;td>Every one, including the intermediary and ultimate receiver, receives the message should be able to processing the Security header.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">http://www.w3.org/2003/05/soap-envelope/role/none&lt;/td>&lt;td>No one should process the Security Header.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">http://www.w3.org/2003/05/soap-envelope/role/next&lt;/td>&lt;td>Every one, including the intermediary and ultimate receiver, receives the message should be able to processing the Security header.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">http://www.w3.org/2003/05/soap-envelope/role/ultimateReceiver&lt;/td>&lt;td>The message ultimate receiver can process the Security header. This is the default value if such setting is not configured.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">&amp;lt;blank or empty string>&lt;/td>&lt;td>The empty string \"\" (without quotes) indicates that no \"actor/role\" identifier is configured. if there is no actor/role setting configured, the ultimateReceiver is assumed when processing the message, and no actor/role attribute will be added when generating the WS-Security header. There should not be more than one Security headers omitting the actor/role identifier.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">USE_MESSAGE_BASE_URI&lt;/td>&lt;td>The value \"USE_MESSAGE_BASE_URI\" without quotes indicates that the actor/role identifier will be the base URL of the message, if the SOAP message is transported using HTTP, the base URI is the Request-URI of the http request.&lt;/td>&lt;/tr>&lt;tr>&lt;td valign=\"left\">any other customized string&lt;/td>&lt;td>You can input any string to identify the actor or role of the Security header.&lt;/td>&lt;/tr>&lt;/table>&lt;p>The default value is a blank value.&lt;/p>"
                },
                {
                    "name": "AUSMHTTPHeader",
                    "array": "true",
                    "type": {
                        "href": "/mgmt/types/default/dmString"
                    },
                    "cli-alias": "au-sm-http-header",
                    "ignored-when": {
                        "condition": {
                            "evaluation": "property-value-not-in-list",
                            "property-name": "AUSMHeaderFlow",
                            "value": [
                                "frontend",
                                "backend",
                                "frontend+backend"
                            ]
                        }
                    },
                    "display": "HTTP headers",
                    "summary": "HTTP headers of interest from CA Single Sign-on responses to include in responses or requests if configured",
                    "description": "Specifies the HTTP headers from CA Single Sign-On responses. When specified, these headers are included into the request or response headers based on the setting of the CA Single Sign-on header flow."
                },
                {
                    "name": "AZSMHTTPHeader",
                    "array": "true",
                    "type": {
                        "href": "/mgmt/types/default/dmString"
                    },
                    "cli-alias": "az-sm-http-header",
                    "ignored-when": {
                        "condition": {
                            "evaluation": "property-value-not-in-list",
                            "property-name": "AZSMHeaderFlow",
                            "value": [
                                "frontend",
                                "backend",
                                "frontend+backend"
                            ]
                        }
                    },
                    "display": "HTTP headers",
                    "summary": "HTTP headers of interest from CA Single Sign-on responses to include in responses or requests if configured",
                    "description": "Specifies the HTTP headers from CA Single Sign-On responses. When specified, these headers are included into the request or response headers based on the setting of the CA Single Sign-on header flow."
                },
                {
                    "name": "DynConfig",
                    "type": {
                        "href": "/mgmt/types/default/dmDynConfigType"
                    },
                    "required": "true",
                    "cli-alias": "dyn-config",
                    "default": "none",
                    "display": "Dynamic configuration type",
                    "summary": "How to obtain the AAA policy configuration dynamically",
                    "description": "Specifies how to obtain the AAA policy configuration dynamically. Dynamic configuration enables users to configure AAA policy at run time. When enabled, the configuration of AAA is determined dynamically based on the template AAA policy and the parameters that the dynamic configuration custom URL returns."
                },
                {
                    "name": "ExternalAAATemplate",
                    "type": {
                        "href": "/mgmt/types/default/dmReference",
                        "reference-to": {
                            "href": "/mgmt/metadata/default/AAAPolicy"
                        }
                    },
                    "cli-alias": "external-aaa-template",
                    "required-when": {
                        "condition": {
                            "evaluation": "property-value-in-list",
                            "property-name": "DynConfig",
                            "value": "external-aaa"
                        }
                    },
                    "ignored-when": {
                        "condition": {
                            "evaluation": "logical-true"
                        }
                    },
                    "display": "External AAA policy template",
                    "summary": "The external AAA policy to use as the template",
                    "description": "Specifies an external AAA policy to use as the template. When specified, it overwrites the configuration of the current AAA policy."
                },
                {
                    "name": "DynConfigCustomURL",
                    "type": {
                        "href": "/mgmt/types/default/dmURL"
                    },
                    "cli-alias": "dyn-config-custom-url",
                    "required-when": {
                        "condition": {
                            "evaluation": "logical-or",
                            "condition": [
                                {
                                    "evaluation": "property-value-in-list",
                                    "property-name": "DynConfig",
                                    "value": "current-aaa"
                                },
                                {
                                    "evaluation": "property-value-in-list",
                                    "property-name": "DynConfig",
                                    "value": "external-aaa"
                                }
                            ]
                        }
                    },
                    "ignored-when": {
                        "condition": {
                            "evaluation": "logical-true"
                        }
                    },
                    "display": "Dynamic configuration custom URL",
                    "summary": "The location of the custom stylesheet or GatewayScript file",
                    "description": "&lt;p>Specifies the location of the custom stylesheet or GatewayScript file where to obtain the AAA policy configuration. The obtained configuration overwrites the configuration that is defined in the template AAA policy. In the custom stylesheet or GatewayScript file, it is recommended that you modify only those properties to be dynamically overwritten in the template AAA policy.&lt;/p>&lt;p>See the &lt;tt>ModifyAAAPolicy&lt;/tt> element in the store:///xml-mgmt.xsd schema to construct a schema-compliant AAA configuration. For the nodeset that the custom URL is expected to return and a sample stylesheet, see the topic in IBM Knowledge Center.&lt;/p>"
                }
            ]
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
