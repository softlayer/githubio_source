---
title: "get_schedules.py"
description: "get_schedules.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Storage"
tags:
    - "endurance"
---


```
"""
Get all the schedules configured in the endurance storage.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/getSchedules

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

# The endurance storage id from where you wish to get the schedules
enduranceStorageId = 6548079

# Declares the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
storageService = client['SoftLayer_Network_Storage']

try:
    result = storageService.getSchedules(id=enduranceStorageId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the Schedules. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
