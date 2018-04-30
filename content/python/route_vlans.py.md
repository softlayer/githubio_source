---
title: "route_vlans.py"
description: "route_vlans.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
tags:
    - "gateway"
---


```
"""
Route the vlans in a gateway device.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getInsideVlans
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/unbypassVlans
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

gatewayId = 127643
vlanIdsToRemove = [1054267, 822929]

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
gatewayService = client['SoftLayer_Network_Gateway']

objectFilter = {"insideVlans": {"networkVlanId": {"operation": "in", "options": [{"name": "data", "value": vlanIdsToRemove}]}}}

try:
    gatewayVlans = gatewayService.getInsideVlans(id=gatewayId, filter=objectFilter)
    result = gatewayService.unbypassVlans(gatewayVlans, id=gatewayId)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to route the VLANs. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
