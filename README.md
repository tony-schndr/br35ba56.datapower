# Ansible Collection - community.datapower

The Ansible DataPower collection includes a variety of Ansible modules to automate the management of IBM DataPower Appliances.


### Modules
Name | Description
--- | ---
[community.datapower.action]()|Execute actions against a domain
[community.datapower.config]()|Manage configuration objects in a domain
[community.datapower.export_domains]()|Export a domain(s)
[community.datapower.export_objects]()|Export configuration objects from a domain.
[community.datapower.files]()|Manage files within a domain's filestore.
[community.datapower.get_action_schema]()|Get the schema of an action. 
[community.datapower.get_config]()|Get object configuration from a domain.
[community.datapower.import_domains]()|Import a Domain(s)
[community.datapower.list_actions]()|List supported actions
[community.datapower.list_objects]()|List config objects
[community.datapower.list_status]()|List status types
[community.datapower.load_objects]()|Import objects/files into a domain
[community.datapower.status]()|Retreive various statuses

## Installing this collection
Download a release from this github repository.

Install the DataPower collection with the Ansible Galaxy CLI:
```
ansible-galaxy collection install community-datapower-1.0.0.tar.gz
```

## Using this collection
This collection uses an httpapi plugin that utilizes the DataPower REST Management Interface, ensure it is configured, ref IBM DataPower Documentation

Log into the datapower CLI and run:
```
co; rest-mgmt; admin-state enabled; port 5554; exit;
write mem; 
```



### Using modules from this collection in your playbooks

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `community.datapower.config`.
The following example task configures a log target.

```yaml
---
- name: Configure a log target
    community.datapower.config:
    domain: default
    state: present
    config:
        LogTarget:
        IdleTimeout: 15
        LocalAddress: 0.0.0.0
        LocalIdentifier: dp-1
        LogEvents:
            Class:
            value: all
            Priority: notice
        LogPrecision: second
        LongRetryInterval: 20
        Priority: normal
        RateLimit: 100
        RemoteAddress: 192.168.1.88
        RemotePort: 514
        RetryAttempts: 1
        RetryInterval: 1
        Rotate: 3
        SSLClientConfigType: proxy
        Size: 500
        SoapVersion: soap11
        SyslogFacility: user
        TimestampFormat: zulu
        Type: syslog-tcp
        UploadMethod: ftp
        UseANSIColor: 'off'
        mAdminState: enabled
        name: syslog_LogTarget
```

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.