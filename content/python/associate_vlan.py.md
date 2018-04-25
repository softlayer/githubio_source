---
title: "associate_vlan.py"
description: "associate_vlan.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway_Vlan"
tags:
    - "gateway"
---


```
"""
Associate vlans in a gateway device.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan/createObjects
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway_Vlan/

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

gatewayId = 127643
vlanIdToAdd = 1054265

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
gatewayVlanService = client['SoftLayer_Network_Gateway_Vlan']

object = {
    "bypassFlag": True,
    "networkGatewayId": gatewayId,
    "networkVlanId": vlanIdToAdd
}

template = []
template.append(object)

try:
    result = gatewayVlanService.createObjects(template)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to associate VLAN. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
