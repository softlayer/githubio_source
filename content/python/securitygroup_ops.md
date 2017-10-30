---
title: "Create, list, get, and delete security groups"
description: "Examples for creating, listing, getting, and deleting security groups"
date: "2017-10-18"
classes: 
    - "SoftLayer_Network_SecurityGroup"
tags:
    - "securitygroups"

---

## Creating a security group

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the NetworkManager
client = SoftLayer.Client()
net_mgr = SoftLayer.NetworkManager(client)

name = 'pythonCreatedGroupExample'
description = 'Security Group created via python'
try:
    result = net_mgr.create_securitygroup(name=name, description=description)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed... Unable to create a new security group: faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

## Deleting a security group

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the NetworkManager
client = SoftLayer.Client()
net_mgr = SoftLayer.NetworkManager(client)

sg_id = 12045
try:
    result = net_mgr.delete_securitygroup(sg_id)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed... Unable to delete security group: faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

## Getting a security group

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the NetworkManager
client = SoftLayer.Client()
net_mgr = SoftLayer.NetworkManager(client)

sg_id = 12045
try:
    result = net_mgr.get_securitygroup(sg_id)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed... Unable to get security group: faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

## List all security groups in account

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the NetworkManager
client = SoftLayer.Client()
net_mgr = SoftLayer.NetworkManager(client)

result = net_mgr.list_securitygroups()
pp(result)
```
