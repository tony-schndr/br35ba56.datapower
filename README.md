# DataPower Collection for Ansible
[![CI](https://github.com/br35ba56/ansible-datapower/workflows/CI/badge.svg?event=push)](https://github.com/br35ba56/ansible-datapower/actions)
[![Network Integration](https://github.com/Br35Ba56/ansible-datapower/actions/workflows/network-integration.yml/badge.svg)](https://github.com/Br35Ba56/ansible-datapower/actions/workflows/network-integration.yml)
[![codecov](https://codecov.io/gh/tony-schndr/ansible-datapower/branch/main/graph/badge.svg?token=0RY2TCSVLV)](https://codecov.io/gh/tony-schndr/ansible-datapower)
[![Roles](https://github.com/Br35Ba56/ansible-datapower/actions/workflows/test-roles.yml/badge.svg)](https://github.com/Br35Ba56/ansible-datapower/actions/workflows/test-roles.yml)

The Ansible DataPower collection includes a variety of modules to automate IBM DataPower Appliances.


## Tested with Ansible
2.9, 2.10, 2.11

<!-- List any external resources the collection depends on, for example minimum versions of an OS, libraries, or utilities. Do not list other Ansible collections here. -->

### Supported connections

The ansible datapower collection supports `httpapi` connections.

Ensure the DataPower's REST Mgmt Interface is enabled by logging into the DataPower CLI and executing the following:
```
co; rest-mgmt; admin-state enabled; port 5554; exit;
write mem;
```

Then define the following variables in an inventory file.
```
ansible_connection=httpapi
ansible_httpapi_use_ssl=yes
ansible_httpapi_port=<rest management port, default is 5554>
ansible_network_os=br35ba56.datapower.rest_mgmt
ansible_user=<DataPower user>
ansible_httpapi_password=<DataPower user password>
```



## Included content
Please see the module and plugin collection [here](https://br35ba56.github.io/ansible-datapower/).
Since the github pages documenation is rough around the edges for now, you could also use `ansible-doc` to retrieve module documentation.

```
ansible-doc plugin module br35ba56.datapower.config
```
## Using this collection

<!--Include some quick examples that cover the most common use cases for your collection content. It can include the following examples of installation and upgrade (change NAMESPACE.COLLECTION_NAME correspondingly):-->

```yaml=
- name: Save the DataPower 'default' domain.
  br35ba56.datapower.action:
    domain: default
    action: SaveConfig
```

```yaml=
- name: Export all domains and write it to local directory 'work/'
  br35ba56.datapower.backup_domains:
    dest: ./work/
  register: all_domains_export
```

```yaml=
- name: Restore a domain from a domain backup.
  br35ba56.datapower.restore_domains:
    overwrite_objects: yes
    overwrite_files: yes
    export_path: "{{all_domains_export.path}}"
```
```yaml=
- name: Export the GetStat_MPG service from the snafu domain
  br35ba56.datapower.export_zip:
    domain: snafu
    ref_objects: yes
    ref_files: yes
    dest: /var/tmp
    objects:
      - name: GetStat_MPG
        class: MultiProtocolGateway
  register: GetStat_export
```
```yaml=
- name: Import the service exported from snafu domain into foo domain
  br35ba56.datapower.import_zip:
    domain: foo
    export_path: "{{ GetStat_export.path }}"
```
### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible Galaxy command-line tool.

From Ansible Galaxy:

```bash
ansible-galaxy collection install br35ba56.datapower
```
Directly from GitHub repository:
```bash
ansible-galaxy collection install git+https://github.com/Br35Ba56/ansible-datapower.git
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:
```yaml
---
collections:
  - name: br35ba56.datapower
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the `ansible` package. To upgrade the collection to the latest available version, run the following command:
```bash
ansible-galaxy collection install br35ba56.datapower --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version `1.0.1`:

```bash
ansible-galaxy collection install br35ba56.datapower:==1.0.1
```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Release notes

See the [changelog](https://github.com/ansible-collections/REPONAMEHERE/tree/main/CHANGELOG.rst).

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

<!-- List out where the user can find additional information, such as working group meeting times, slack/IRC channels, or documentation for the product this collection automates. At a minimum, link to: -->

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/devel/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
- [Ansible Collections Checklist](https://github.com/ansible-collections/overview/blob/master/collection_requirements.rst)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html)
- [The Bullhorn (the Ansible Contributor newsletter)](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420)
- [Changes impacting Contributors](https://github.com/ansible-collections/overview/issues/45)


## Code of Conduct

We follow the [Ansible Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html) in all our interactions within this project.

If you encounter abusive behavior, please refer to the [policy violations](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html#policy-violations) section of the Code for information on how to raise a complaint.


## Contributing to this collection

<!--Describe how the community can contribute to your collection. At a minimum, fill up and include the CONTRIBUTING.md file containing how and where users can create issues to report problems or request features for this collection. List contribution requirements, including preferred workflows and necessary testing, so you can benefit from community PRs. If you are following general Ansible contributor guidelines, you can link to - [Ansible Community Guide](https://docs.ansible.com/ansible/devel/community/index.html). List the current maintainers (contributors with write or higher access to the repository). The following can be included:-->

The content of this collection is made by people like you, a community of individuals collaborating on making the world better through developing automation software.

We are actively accepting new contributors.

Any kind of contribution is very welcome.

You don't know how to start? Refer to our [contribution guide](CONTRIBUTING.md)!

We use the following guidelines:

* [CONTRIBUTING.md](CONTRIBUTING.md)
* [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md)
* [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html)
* [Ansible Development Guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
* [Ansible Collection Development Guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections)

<!--
## Collection maintenance

The current maintainers are listed in the [MAINTAINERS](MAINTAINERS) file. If you have questions or need help, feel free to mention them in the proposals.

To learn how to maintain / become a maintainer of this collection, refer to the [Maintainer guidelines](MAINTAINING.md).

-->

## Governance

<!--Describe how the collection is governed. Here can be the following text:-->


The process of decision making in this collection is based on discussing and finding consensus among participants.

Every voice is important. If you have something on your mind, create an issue or dedicated discussion and let's discuss it!


## Licensing

<!-- Include the appropriate license information here and a pointer to the full licensing details. If the collection contains modules migrated from the ansible/ansible repo, you must use the same license that existed in the ansible/ansible repo. See the GNU license example below. -->

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
