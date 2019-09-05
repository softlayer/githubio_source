---
title: "CDN Bandwidth Data"
description: "getBandwidthData"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_ContentDelivery_Account"
tags:
    - "cdn"
    - "bandwidth"
---


```
"""
Get bandwidth data in a CDN.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_ContentDelivery_Account/getBandwidthData

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

cdnid = 30393

startDate = "2014-10-10 00:00:00"
endDate = "2015-10-10 05:00:00"

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
cdnService = client['SoftLayer_Network_ContentDelivery_Account']

try:
    response = cdnService.getBandwidthData(startDate, endDate, id=cdnid)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the bandwidth data. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
