---
title: "migrateDedicatedHost.py"
description: "migrateDedicatedHost.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "dedicatedhost"
---


```
"""
Create a transaction to migrate an instance from one dedicated host to another dedicated host.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/migrateDedicatedHost

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

virtualGuestIdToMigrate = 37117661
dedicatedHostTarget = 10201

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']

try:
    response = virtualGuestService.migrateDedicatedHost(dedicatedHostTarget, id=virtualGuestIdToMigrate)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to migrate the dedicated host. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
