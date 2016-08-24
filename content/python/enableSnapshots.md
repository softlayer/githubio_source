---
title: "Create a snapshot schedule"
description: "Create a snapshot schedule for Endurance storage."
date: "2016-08-23"
classes: ["SoftLayer_Network_Storage"]
tags:
    - "enableSnapshots"
    - "blockStorage"
---

This method is not valid for Legacy iSCSI Storage Volumes. You need to have already purchased snapshot space for the script to work properly.

```python
import SoftLayer

client = SoftLayer.Client()
storageId = 11657445

# Define parameters for snapshot
scheduleType = 'WEEKLY'
retentionCount = '20'
minute = '1'
hour = '13'
dayOfWeek = 'SUNDAY'

try:
    result = client['SoftLayer_Network_Storage'].enableSnapshots(scheduleType, retentionCount, minute, hour, dayOfWeek, id=storageId)
    print (result)
except SoftLayer.SoftLayerAPIError as e:
    print("Error: "
          % (e.faultCode, e.faultString))
```
