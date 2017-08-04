---
title: "Get Dedicated Host Guests"
description: "Get a list of VSIs that have been deployed to a Dedicated Host. "
date: "2017-08-04"
classes: 
    - "SoftLayer_Virtual_DedicatedHost"
tags:
---


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