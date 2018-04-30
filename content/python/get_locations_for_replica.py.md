---
title: "get_locations_for_replica.py"
description: "get_locations_for_replica.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Storage"
tags:
    - "endurance"
---


```
"""
Get valid datacenters to order a replica.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage/getValidReplicationTargetDatacenterLocations

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

USERNAME = 'set me'
API_KEY = 'set me'

# The id of the endurance storage you wish to create a replica.
enduranceStorageId = 6548079

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
storageService = client['SoftLayer_Network_Storage']

try:
    result = storageService.getValidReplicationTargetDatacenterLocations(id=enduranceStorageId)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the locations. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
