---
title: "Add, list, and remove security group rules"
description: "Examples for adding, listing, and removing rules from security groups"
date: "2017-10-18"
classes: 
    - "SoftLayer_Network_SecurityGroup"
tags:
    - "securitygroups"

---

## Adding a rule to a security group

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the NetworkManager
client = SoftLayer.Client()
net_mgr = SoftLayer.NetworkManager(client)

sg_id = 123045
direction = 'ingress'
ethertype = 'IPv4'
remote_ip = '169.148.34.0/24'
protocol = 'tcp'
port_min = 22
port_max = 22
try:
    result = net_mgr.add_securitygroup_rule(sg_id,
                                            direction=direction,
                                            ethertype=ethertype,
                                            remote_ip=remote_ip,
                                            protocol=protocol,
                                            port_min=port_min,
                                            port_max=port_max)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed... Unable to add a rule to the security group: faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

## Listing rules in a security group

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the NetworkManager
client = SoftLayer.Client()
net_mgr = SoftLayer.NetworkManager(client)

sg_id = 123045
try:
    result = net_mgr.list_securitygroup_rules(sg_id)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed... Unable to list rules in the security group: faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

## Removing a rule from a security group

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the NetworkManager
client = SoftLayer.Client()
net_mgr = SoftLayer.NetworkManager(client)

sg_id = 123045
rule_id = 475879
try:
    result = net_mgr.remove_securitygroup_rule(sg_id, rule_id)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed... Unable to remove rule from the security group: faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

## Remove all rules from a security group

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the NetworkManager
client = SoftLayer.Client()
net_mgr = SoftLayer.NetworkManager(client)

sg_id = 123045
try:
    rules = net_mgr.list_securitygroup_rules(sg_id)
    rules = [rule['id'] for rule in rules]
    result = net_mgr.remove_securitygroup_rules(sg_id, rules)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed... Unable to remove rules from the security group: faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```
