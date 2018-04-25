---
title: "delet_origin_mapping.py"
description: "delet_origin_mapping.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping"
tags:
    - "cdn"
---


```
"""
Delete an origin mappings in a CDN.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/deleteOriginPullRule
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

cdnid = 30393
originid = "co616979"

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
cdnService = client['SoftLayer_Network_ContentDelivery_Account']

try:
    response = cdnService.deleteOriginPullRule(originid, id=cdnid)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to delete the origin mappings. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
