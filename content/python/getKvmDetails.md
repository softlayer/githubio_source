---
title: "Get Virtual Console Virtual Guest"
description: "Retrieve the IP, username, and password needed to access the KVM console for a Virtual Guest."
date: "2017-05-04"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "objectMask"
    - "getObject"
---


```python
"""
@author Ryan Tiffany
"""

import SoftLayer
from pprint import pprint as pp

client = SoftLayer.Client()

mask = "mask[consoleIpAddressRecord[ipAddress[ipAddress],port],operatingSystem[passwords]]"

getDetails = client['SoftLayer_Virtual_Guest'].getObject(mask=mask,id=31678643)
pp(getDetails)
```
