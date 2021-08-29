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
[community.datapower.status]()|Retrieve various statuses

## Installing this collection
Download a release from this github repository or 

This collection is uses the package dictdiffer for dictionary comparisons.  Therefore you must have the dictdiffer package installed on the server that will be executing these modules.  For example if your running these modules on the ansible-controller using the local network connection (As it would be for most networking modules by default), it will need to be installed on the ansible-controller.  If delegating play execution to another server, you would need the dictdiffer package installed on the delegated server.

```bash
pip3 install -r requirements.txt
```

Install the DataPower collection with the Ansible Galaxy CLI:
```
ansible-galaxy collection install community-datapower-1.0.0.tar.gz
```


## Using this collection
This collection uses an httpapi plugin that utilizes the DataPower REST Management Interface, ensure the interface is configured, ref IBM DataPower Documentation

Log into the datapower CLI and run:
```
co; rest-mgmt; admin-state enabled; port 5554; exit;
write mem; 
```

# Using modules from this collection in your playbooks

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

# Contributing to this collection

# Clone the playbook directory to assist with testing modules against playbooks.
git clone https://github.com/Br35Ba56/ansible-datapower-playbooks.git

cd ansible-datapower-playbooks

mkdir -p collections/ansible_collections/community/

cd collections/ansible_collections/community/

git clone https://github.com/Br35Ba56/ansible-datapower.git

mv ansible-datapower datapower
```

The path `collections/ansible_collection/community/datapower` is ansible default search path for installed collections, refer to 
[Using Collections](https://docs.ansible.com/ansible/2.9/user_guide/collections_using.html)
 
```bash
tree -L 5
.
├── action.yml
├── collections
│   └── ansible_collections
│       └── community
│           └── datapower
│               ├── LICENSE
│               ├── README.md
│               ├── build.sh
│               ├── deploy.yml
│               ├── export.yml
│               ├── galaxy.yml
│               ├── get_latest.sh
│               ├── install.sh
│               ├── meta
│               ├── plugins
│               ├── requirements.txt
│               ├── roles
│               ├── scripts
│               └── tests
├── config.yml
├── demo.txt
├── demo2.txt
├── directories.yml
├── export.yml
├── files.yml
├── get_config.yml
├── inventory
│   └── dp_hosts.yml
├── list_objects.yml
├── lists.yml
├── logtarget.yml
├── requirements.txt
└── test.yml
```

## DataPower Runtime
DataPower runtime can be provided through docker.
[Docker DataPower Runtime](https://github.com/Br35Ba56/ansible-datapower-runtime)

## Adding a new module
If want to add a new module to this collection review and familiarize yourself with the existing modules in `plugins/modules/`.  Find a module to copy to keep the formatting and code style consistent throughout all modules.

### Module tests
All additional modules MUST include **Sanity Tests** and **Integration Tests**

### Module Utilities
If your adding to `plugins/module_utils/datapower/` you MUST include **Unit Tests**.

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.