---
title: "get_location_groups.py"
description: "get_location_groups.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Location_Group_Pricing"
tags:
    - "locationgroup"
---


```
"""
Get all the location groups pricing..

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group_Pricing
http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group_Pricing/getAllObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group_Pricing

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

# Declares the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
locationGroupService = client['SoftLayer_Location_Group_Pricing']

# Declares an object mask to see the location details
objectMask = "mask[locations]"

try:
    response = locationGroupService.getAllObjects(mask=objectMask)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the location groups. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
