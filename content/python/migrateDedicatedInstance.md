---
title: "Migrate a VSI between dedicated hosts"
description: "Migrate a Dedicated Host instance to another Dedicated Host. You can migrate your dedicated host instances from one host to another within the same POD."
date: "2017-08-04"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
---

This script will kick of an immediate migration of the Virtual Guest. 

```
"""
@author Ryan TIffany
"""
import SoftLayer
from pprint import pprint as pp

destinationHostId = 987654
vsiId = 1234567
client = SoftLayer.Client()

migrateGuest = client['SoftLayer_Virtual_Guest'].migrateDedicatedHost(destinationHostId, id=vsiId)
```