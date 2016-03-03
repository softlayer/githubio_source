---
title: "Attach and Detach a Block Device to a Virtual_Guest"
description: "Attaching and detaching secondary block devices on Virtual Guests"
date: "2016-03-03"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "attachDiskImage"
    - "detachDiskImage"
---

Attaching a currently detached block device.
```python

import SoftLayer
from pprint import pprint as pp
client = SoftLayer.Client()

vsi_id = '11111111'
disk_id = '8888888'
attach = client['SoftLayer_Virtual_Guest'].attachDiskImage(disk_id,id=vsi_id)
```

Detaching a currently attached block device.
```python

import SoftLayer
from pprint import pprint as pp
client = SoftLayer.Client()

vsi_id = '11111111'
disk_id = '8888888'
attach = client['SoftLayer_Virtual_Guest'].detachDiskImage(disk_id,id=vsi_id)
```
