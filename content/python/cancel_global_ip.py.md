---
title: "cancel_global_ip.py"
description: "cancel_global_ip.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Billing_Item"
tags:
    - "subnets"
---


```
"""
Cancel Global IP address. Cancel the global IP address resource using its billing Item.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/getGlobalIpRecord

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'

subnetId = 880617
mask = 'id,billingItem.id'

client = SoftLayer.Client(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    subnetResult = client['SoftLayer_Network_Subnet'].getGlobalIpRecord(
        id=subnetId,
        mask=mask)
    billingItemId = subnetResult['billingItem']['id']

    try:
        client['SoftLayer_Billing_Item'].cancelItem(
            False,
            False,
            "No longer needed",
            "Api test",
            id=billingItemId)
    except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get billing item information faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to cancel the item faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```
