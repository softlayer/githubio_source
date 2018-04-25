---
title: "list_origin_mapping.py"
description: "list_origin_mapping.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
"""
List all the origin pull mappings in the CDN.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/getOriginPullMappingInformation

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

cdnid = 30393

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
cdnService = client['SoftLayer_Network_ContentDelivery_Account']

try:
    response = cdnService.getOriginPullMappingInformation(id=cdnid)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list origin mappings. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
