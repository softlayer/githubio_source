---
title: "get_regions.py"
description: "get_regions.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Location_Group"
tags:
    - "bandwidthpools"
---


```
"""
Get the valid regions to order a bandwidth pool.

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group/getAllObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client
client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
locationService = client['SoftLayer_Location_Group']

objectFilter = {"locationGroupType": {"name": {"operation": "VDR"}}}

try:
    regions = locationService.getAllObjects(filter=objectFilter)
    print(json.dumps(regions, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the regions. " % (e.faultCode, e.faultString))
    exit(1)

```
