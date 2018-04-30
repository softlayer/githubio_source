---
title: "add_origin_mapping.py"
description: "add_origin_mapping.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping"
tags:
    - "cdn"
---


```
"""
Create an origin mappings in a CDN.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/createOriginPullMapping
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

cdnid = 30393

template = {
    "mediaType": "HTTP",
    "originUrl": "http://www.example.com",
    "cname": "cdn.example.com"
}

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
cdnService = client['SoftLayer_Network_ContentDelivery_Account']

try:
    response = cdnService.createOriginPullMapping(template, id=cdnid)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the origin mappings. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
