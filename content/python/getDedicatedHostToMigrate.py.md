---
title: "getDedicatedHostToMigrate.py"
description: "getDedicatedHostToMigrate.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_DedicatedHost"
tags:
    - "dedicatedhost"
---


```
"""
Get valid dedicated host for migration.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getDedicatedHosts
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_DedicatedHost
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getDedicatedHost
http://sldn.softlayer.com/article/object-masks
http://sldn.softlayer.com/article/object-filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

virtualGuestIdToMigrate = 37117661

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']
virtualGuestService = client['SoftLayer_Virtual_Guest']

try:
    dedicatedHostSource = virtualGuestService.getDedicatedHost(id=virtualGuestIdToMigrate, mask="mask[backendRouter]")
    objectFilter = {
        "dedicatedHosts": {
            "backendRouter": {
                "id": {
                    "operation": dedicatedHostSource["backendRouter"]["id"]
                }
            }
        }
    }
    response = accountService.getDedicatedHosts(filter=objectFilter)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the Dedicated servers to migrate. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
