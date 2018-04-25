---
title: "disassociate_vlan.py"
description: "disassociate_vlan.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Gateway"
    - "SoftLayer_Network_Gateway_Vlan"
tags:
    - "gateway"
---


```
"""
Disassociate vlans in a gateway device.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan/deleteObject
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway/getInsideVlans
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

gatewayId = 127643
vlanIdToRemove = 1054265

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
gatewayService = client['SoftLayer_Network_Gateway']
gatewayVlanService = client['SoftLayer_Network_Gateway_Vlan']

objectFilter = {"insideVlans": {"networkVlanId": {"operation": vlanIdToRemove}}}

try:
    gatewayVlan = gatewayService.getInsideVlans(id=gatewayId, filter=objectFilter)
    if len(gatewayVlan) == 0:
        print("The Vlan id: " + str(vlanIdToRemove) + " is not associated to the gateway id: " + str(gatewayId))
        exit(1)
    result = gatewayVlanService.deleteObject(id=gatewayVlan[0]['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to remove VLAN. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

```
