---
title: "enable_snapshot_endurance.py"
description: "enable_snapshot_endurance.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Storage"
tags:
    - "endurance"
---


```
"""
Enable Snapshot for a endurance.

The example creates a daily snapshot  at 14:05

Important Manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/enableSnapshots
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

"""
Client configuration
Your SoftLayer API username and key.
"""
USERNAME = 'set me'
API_KEY = 'set me'

scheduleType = "DAILY"
retentionCount = 3
minute = 5
hour = 14

legacyIscsiId = 5805095

# Declaring the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
networkStorageService = client['SoftLayer_Network_Storage']

try:
    result = networkStorageService.enableSnapshots(scheduleType, retentionCount, minute, hour, id=legacyIscsiId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to enable snapshot faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
