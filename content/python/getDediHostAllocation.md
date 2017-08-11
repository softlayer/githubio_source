---
title: "Get Dedicated Host Allocation"
description: "Retrieve the CPU, Ram, Storage allocations on a dedicated host. "
date: "2017-08-04"
classes: 
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "getAllocationStatus"
---


```
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
