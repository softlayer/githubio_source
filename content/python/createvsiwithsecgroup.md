---
title: "Create a new virtual server and attach Security Groups"
description: "Creates a new virtual server (VSI) aand attach the public and private interfaces to respective Security Groups."
date: "2017-10-30"
classes:
  - "SoftLayer_Virtual_Guest"
tags:
  - "vsis"
  - "create"
  - "securitygroups"
---

```python

from __future__ import print_function
import SoftLayer
from SoftLayer.managers.vs import VSManager

def create_vsi():
    #Create a client to the SoftLayer_Account API service.
    #Note: currently set without the user ID and API key since
    #it will by default use the values set in the CLI
    #to use other values use SoftLayer.Client(sl_username, sl_api_key)
    client = SoftLayer.Client()
    vsi_mgr = VSManager(client)

   # common values
    datacenter = 'wdc07' 
    domain = 'cde.services' 
    os_code = 'UBUNTU_LATEST_64'
    local_disk = True 
    hourly = True 
    dedicated = False 
    nic_speed = 1000 
    disks = [100] 
    private = False 
    ssh_keys = [972047] 
    public_security_groups = [43507]
    private_security_groups = [43511]

    # server properties
    hostname = 'sgvsi'
    cpus = 2
    memory = 2048

    result = vsi_mgr.create_instance(hostname=hostname, domain=domain,
                                     cpus=cpus, memory=memory, datacenter=datacenter,
                                     os_code=os_code, local_disk=local_disk,
                                     hourly=hourly, dedicated=dedicated,
                                     disks=disks, nic_speed=nic_speed, private=private,
                                     ssh_keys=ssh_keys, public_security_groups=public_security_groups,
                                     private_security_groups=private_security_groups)
    print(result)

if __name__ == '__main__':
    create_vsi()
```