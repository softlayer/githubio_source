---
title: "Get Dedicated Host Allocation"
description: "Retrieve the CPU, Ram, Storage allocations on a dedicated host. "
date: "2017-08-04"
classes: 
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "getAllocationStatus"
---

The first thing you need to get is a list of the Dedicated Hosts on your account. To list the Dedicated Hosts on your account you can use the following code:

```python
import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()

dedicatedHosts = client['SoftLayer_Account'].getDedicatedHosts()
pp(dedicatedHosts)
```

Once you have the Dedicated Host ID you can use the following code to retrieve the resource allocations on the host. 

```python
"""
@author Ryan TIffany
"""
import SoftLayer
from pprint import pprint as pp

dedicatedHostId = 10501
client = SoftLayer.Client()

getAllocStats = client['SoftLayer_Virtual_DedicatedHost'].getAllocationStatus(id=dedicatedHostId)
pp(getAllocStats)
```
