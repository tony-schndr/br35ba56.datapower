# Ansible Collection - community.datapower

The Ansible DataPower collection includes a variety of modules to automate
the management of IBM DataPower Appliances.


## Modules
Name | Description
--- | ---
[community.datapower.files]()|Manage files within a domain's local/cert/sharedcert directory.
[community.datapower.config]()|Manage configuration within a domain
[community.datapower.get_config]()|Get object configuration from a domain.
[community.datapower.list_objects]()|List config objects (use to find config names)
[community.datapower.export_domains]()|Export a domain(s) in ZIP format.
[community.datapower.import_domains]()|Import a domain(s)
[community.datapower.export_objects]()|Export configuration from a domain (Output used "load_objects" module)
[community.datapower.load_objects]()|Import configuration into a domain
[community.datapower.action]()|Execute actions against a domain
[community.datapower.get_action_schema]()|Get the schema of an action.
[community.datapower.list_actions]()|List supported actions (use to find available actions)
[community.datapower.status]()|Retrieve various statuses
[community.datapower.list_status]()|List status types (use to determine name of status for status module)


## Installing this collection

### Dependencies
Python: 3.6, 3.7, 3.8, 3.9

Docker - For a developer version of IBM DataPower runtime.

### Python Modules
Name | Version
--- | ---
[dictdiffer](https://github.com/inveniosoftware/dictdiffer)| latest

```bash
pip3 install -r ansible_collections/community/datapower/requirements.txt
```

This collection is still in development and is not on ansible galaxy.  Follow the instructions [here](https://cn-ansibledoc.readthedocs.io/zh_CN/latest/user_guide/collections_using.html) to install.

You will either build / install the collection manually using ansible galaxy.

OR

Make a directory for storing playbooks outside this repository, create a directory called collections inside the directory you create.  Then create a symlink using `ln -s collections/ansible_collections <path to repository>/ansible_collections`

For Example
 ```
ansible-playbooks % tree
.
├── collections
│   └── ansible_collections -> ../../ansible-datapower/ansible_collections
├── inventory.networking
└── play.yml
 ```
If done correctly this collection will be found when running playbooks.

## Using this collection
This collection uses an httpapi plugin that utilizes the DataPower REST Management Interface.  The files `docker-compose.yml`,  `dp/Dockerfile` and files in the directory `dp/config` provide a runtime environment with the Web Management Interface and Rest Management Interface configured to listen on your local machine at https://localhost:9090 and https://localhost:5554.  If you are running this collection against some other environment you will need to ensure the DataPower Rest Management Interface is enabled, below are the instructions to do so.
Log into the datapower CLI and execute the following to enable the Rest Management Interface on its default port.
```
co; rest-mgmt; admin-state enabled; port 5554; exit;
write mem;
```
### Inventory Setup

```
ansible_connection=httpapi
ansible_httpapi_use_ssl=yes
ansible_httpapi_port=<rest management port, default is 5554>
ansible_network_os=community.datapower.rest_mgmt
ansible_user=< DataPower user >
ansible_httpapi_password=< DataPower user password >
```
Review the inventory located at `ansible_collections/community/datapower/tests/integration/inventory.networking`.  You will need to add the variable `ansible_python_interpreter=<path to python3 interpreter>` to the bottom of the inventory file prior to running any plays or executing integration tests.  WARNING, `ansible_httpapi_validate_certs` is turned off, this is for development purposes only.  Ensure that it is set to on in non-development environments.

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
## Adding a new module

All additional modules MUST include **Integration Tests** and pass **Sanity Tests**

DataPower actions (actions can be discovered using the list_action module) should/could have a module that specifically targets the action.  For an example of this review export_domains, export_objects, and load_objects modules.

### Module Utilities

If your changing `plugins/module_utils/datapower/` add/update **Unit Tests**.

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.