---
title: "Migrate a VSI between dedicated hosts"
description: "Migrate a Dedicated Host instance to another Dedicated Host. You can migrate your dedicated host instances from one host to another within the same POD."
date: "2017-08-04"
classes: 
    - "SoftLayer_Virtual_Guest"
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


Once you have the Dedicated Host ID you want to migrate the Virtual Guest to you can use this script to kick of an immediate migration of the Virtual Guest. 

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

