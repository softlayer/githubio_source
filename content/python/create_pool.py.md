---
title: "create_pool.py"
description: "create_pool.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Bandwidth_Version"
tags:
    - "bandwidthpools"
---


```
"""
Create a bandwidth pool.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/createObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

template = {
    "accountId": 307608,
    "bandwidthAllotmentTypeId": 2,
    "locationGroupId": 1,  # The region for the pool.
    "name": "testPoolApi"
}

# Declare the API client
client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
bandwidthService = client['SoftLayer_Network_Bandwidth_Version1_Allotment']

try:
    result = bandwidthService.createObject(template)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the bandwidth pool. " % (e.faultCode, e.faultString))
    exit(1)

```
