---
title: "VSIs and security groups"
description: "Examples for associating and disassociating VSIs with security groups"
date: "2017-10-18"
classes: 
    - "SoftLayer_Network_SecurityGroup"
tags:
    - "securitygroups"

---

## Creating a VSI with security groups

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the VSManager
client = SoftLayer.Client()
vs_mgr = SoftLayer.VSManager(client)

http_sg_id = 384757
ssh_sg_id = 576973

# Allow only HTTP on the public interface of the VSI
public_groups = [http_sg_id]

# Allow HTTP and SSH on the private interface of the VSI
private_groups = [http_sg_id, ssh_sg_id]

# If we didn't want to set any security groups on an interface
# (which allows all traffic), we don't set the associated
# creation kwarg

create_kwargs = {
    'hostname': 'sg-vsi',
    'domain': 'mycompany.com',
    'os_code': 'UBUNTU_LATEST_64',
    'datacenter': 'dal13',
    'cpus': 1,
    'memory': 1024,
    'hourly': True,
    'disks': ('100',),
    'public_security_groups': public_groups,
    'private_security_groups': private_groups,
}

try:
    vsi = vs_mgr.create_instance(**create_kwargs)
    pp(vsi)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed... Unable to create VSI with security group: faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

## Attach an existing VSI to security groups

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the NetworkManager and VSManager
client = SoftLayer.Client()
net_mgr = SoftLayer.NetworkManager(client)
vs_mgr = SoftLayer.VSManager(client)

http_sg_id = 384757
vsi_id = 4018735
private_interface = False
port_number = 0 if private_interface else 1
network_component_mask = 'networkComponents[id, port]'

try:
    vsi_components = vs_mgr.get_instance(vsi_id, mask=network_component_mask)
    component_to_attach = [comp for comp in vsi_components['networkComponents']
                           if comp['port'] == port_number][0]
    result = net_mgr.attach_securitygroup_component(http_sg_id,
                                                    component_to_attach['id'])
    pp(result)
    
    # If this is the first time the server is being associated with security groups,
    # a reboot is required for the security group to take effect on the VSI
    client['Virtual_Guest'].rebootSoft(id=vsi_id)
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed... Unable to associate VSI with security group: faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```

## Detach a VSI from a security group

```python
import SoftLayer
# For nice debug output
from pprint import pprint as pp

# Create a client for use with the NetworkManager and VSManager
client = SoftLayer.Client()
net_mgr = SoftLayer.NetworkManager(client)
vs_mgr = SoftLayer.VSManager(client)

http_sg_id = 384757
vsi_id = 4018735
private_interface = False
port_number = 0 if private_interface else 1
network_component_mask = 'networkComponents[id, port]'

try:
    vsi_components = vs_mgr.get_instance(vsi_id, mask=network_component_mask)
    component_to_detach = [comp for comp in vsi_components['networkComponents']
                           if comp['port'] == port_number][0]
    net_mgr.detach_securitygroup_component(http_sg_id,
                                           component_to_detach['id'])
    
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed... Unable to disassociate VSI with security group: faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))
```
