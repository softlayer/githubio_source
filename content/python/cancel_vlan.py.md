---
title: "cancel_vlan.py"
description: "cancel_vlan.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlans"
---


```
"""
Example to cancel a VLAN

The script will get the Billing_Item id of the VLAN service
then it will cancel the VLAN service

Important manual pages
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API key and username.
USERNAME = 'set me'
API_KEY = 'set me'

# The VLAN id you wish to cancel
vlanId = 563298

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
networkVlanService = client['SoftLayer_Network_Vlan']
billingItemService = client['SoftLayer_Billing_Item']

# Declaring an object mask to get the billing item information
objectMask = 'mask[billingItem]'

try:
    # Getting the Billing Item to cancel the VLAN service.
    vlan = networkVlanService.getObject(mask=objectMask, id=vlanId)
    pp(vlan)
    # Canceling the VLAN service.
    result = billingItemService.cancelService(id=vlan['billingItem']['id'])
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to cancel the VLAN. faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
