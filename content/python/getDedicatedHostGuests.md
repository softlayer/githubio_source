---
title: "Get Dedicated Host Guests"
description: "Get a list of VSIs that have been deployed to a Dedicated Host. "
date: "2017-08-04"
classes: 
    - "SoftLayer_Virtual_DedicatedHost"
tags:
---


The first thing you need to get is a list of the Dedicated Hosts on your account. To list the Dedicated Hosts on your account you can use the following code:

```
import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()

dedicatedHosts = client['SoftLayer_Account'].getDedicatedHosts()
pp(dedicatedHosts)
```

Once you have the Dedicated Host ID you can use the following code to retrieve the Virtual Guests on the host. 


```python

"""
@service SoftLayer_Virtual_DedicatedHost
@author Ryan TIffany
"""
import SoftLayer
from pprint import pprint as pp

dhId = 10001
client = SoftLayer.Client()
getGuests = client['SoftLayer_Virtual_DedicatedHost'].getGuests(id=dhId)
pp(getGuests)
```