# Ansible Role - dp_gateway_peering

Configure Gateway Peering objects on IBM DataPowers.

Requirements
------------

[Ansible Community DataPower Collection](https://github.com/tony-schndr/ansible-datapower)

Role Variables
--------------
```yaml
domain_name: '' # Specify the Domain to create gateway peering object in
gateway_peering_name: gateway-peer
gateway_peering_local_port: 16380
gateway_peering_monitor_port: 26380
gateway_peering_enable_group_mode: 'off'
gateway_peering_enable_ssl: 'off'
gateway_peering_local_address: eth0_ipv4_1 # default datapower docker host alias
gateway_peering_valcred: ""
gateway_peering_idcred: ""
```

Host Variables
--------------
```yaml
# For clustered gateway peering, this is a list of the OTHER peers in the cluster.
gw_peer_host_aliases: []
```
Dependencies
------------
None

Example Playbook
----------------
```yaml
- name: Execute role
  include_role:
    name: dp_gateway_peering

```

License
-------

GNU GPLv3

Author Information
------------------

tonyschndr@gmail.com
