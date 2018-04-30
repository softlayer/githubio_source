---
title: "getAvailableRouters.py"
description: "getAvailableRouters.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "dedicatedhost"
---


```
"""
Get the available backend routers to order a dedicated host.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_DedicatedHost/getAvailableRouters
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_DedicatedHost

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# API credentials
USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
dedicatedHostService = client['SoftLayer_Virtual_DedicatedHost']

# Skeleton of the dedicated host to specify datacenter and configuration sizes
templateDedicatedHost = {
    "cpuCount": 56,
    "diskCapacity": 1200,
    "memoryCapacity": 242,
    "datacenter": {
        "id": 814994
    }
}

try:
    response = dedicatedHostService.getAvailableRouters(templateDedicatedHost)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the backend routers. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
