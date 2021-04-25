log_targets = [
    {
        "LogTarget": {
            "ActiveTimeout": 0,
            "ArchiveMode": "rotate",
            "ConnectTimeout": 60,
            "FeedbackDetection": "off",
            "FixedFormat": "off",
            "Format": "text",
            "IdenticalEventPeriod": 10,
            "IdenticalEventSuppression": "off",
            "IdleTimeout": 15,
            "LocalAddress": "0.0.0.0",
            "LocalIdentifier": "tocdo30150-t1",
            "LogEvents": {
                "Class": {
                    "value": "all"
                },
                "Priority": "notice"
            },
            "LogPrecision": "second",
            "LongRetryInterval": 20,
            "Priority": "normal",
            "RateLimit": 100,
            "RemoteAddress": "192.168.168.88",
            "RemotePort": 514,
            "RetryAttempts": 1,
            "RetryInterval": 1,
            "Rotate": 3,
            "SSLClientConfigType": "proxy",
            "Size": 500,
            "SoapVersion": "soap11",
            "SyslogFacility": "user",
            "TimestampFormat": "zulu",
            "Type": "syslog-tcp",
            "UploadMethod": "ftp",
            "UseANSIColor": "off",
            "mAdminState": "enabled",
            "name": "syslog_LogTarget"
        }
    },
    {
        "LogTarget": {
            "IdleTimeout": 15,
            "LocalAddress": "0.0.0.0",
            "LocalIdentifier": "tocdo30150-t1",
            "LogEventFilter": [
                "0x080c00010",
                "0x08580005c",
                "0x85a0000a"
            ],
            "LogEvents": {
                "Class": {
                    "value": "all"
                },
                "Priority": "notice"
            },
            "LogPrecision": "second",
            "LongRetryInterval": 20,
            "Priority": "normal",
            "RateLimit": 100,
            "RemoteAddress": "192.168.168.88",
            "RemotePort": 514,
            "RetryAttempts": 1,
            "RetryInterval": 1,
            "Rotate": 3,
            "SSLClientConfigType": "proxy",
            "Size": 500,
            "SoapVersion": "soap11",
            "SyslogFacility": "user",
            "TimestampFormat": "zulu",
            "Type": "syslog-tcp",
            "UploadMethod": "ftp",
            "UseANSIColor": "off",
            "mAdminState": "enabled",
            "name": "syslog_LogTarget"
        }
    }
]
