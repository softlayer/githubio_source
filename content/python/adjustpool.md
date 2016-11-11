---
title: "Adding/Removing Servers in a Bandwidth Pool"
description: "Adding and removing Virtual Guests and Bare Metal Servers in an existing Bandwidth Pool"
date: "2016-04-28"
classes: ["SoftLayer_Network_Bandwidth_Version1_Allotment"]
tags:
    - "BandwidthPool"
---

The following script allows you to add and remove servers in an existing bandwidth pool. The script requires empty arrays when not specifying a Bare Metal or Virtual Guest Id. 

```python
import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()

hardwareToAdd = [{"id": 123456 }] # ID's for any bare metal servers to add to the pool
hardwareToRemove = [] # ID's for any bare metal servers to remove from the pool
cloudsToAdd = [] #  ID's for any virtual guests to add to the pool
cloudsToRemove = [{"id": 987654 }] #  ID's for any virtual guests to remove from the pool

pool_id = '11111111' # Bandwidth Pool ID
adjustpool = client['SoftLayer_Network_Bandwidth_Version1_Allotment'].requestVdrContentUpdates(hardwareToAdd, hardwareToRemove, cloudsToAdd, cloudsToRemove, id=pool_id)
pp(adjustpool)
```
