---
title: "get_vsis_in_a_region.py"
description: "get_vsis_in_a_region.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
tags:
    - "bandwidthpools"
---


```
"""
List the VSIs which belong to a region.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

regionId = "1"

# Declare the API client
client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

objectFilter = {"virtualGuests": {"datacenter": {"groups": {"locationGroupTypeId": {"operation": regionId}}}}}

try:
    vsis = accountService.getVirtualGuests(filter=objectFilter)
    print(json.dumps(vsis, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the VSIs. " % (e.faultCode, e.faultString))
    exit(1)

```
