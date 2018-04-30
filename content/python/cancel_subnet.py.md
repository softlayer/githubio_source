---
title: "cancel_subnet.py"
description: "cancel_subnet.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Billing_Item"
tags:
    - "subnets"
---


```
"""
Cancel a Subnet. Cancel network subnet using its billing Item.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelItem
License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'
API_KEY = 'set me'

subnetId = 85467

client = SoftLayer.Client(
    username=API_USERNAME,
    api_key=API_KEY
)

try:
    subnetResult = client['SoftLayer_Network_Subnet'].getBillingItem(
        id=subnetId)
    billingItemId = subnetResult['id']

    try:
        result = client['SoftLayer_Billing_Item'].cancelItem(
            False,
            False,
            "No longer needed",
            "Api test",
            id=billingItemId)
        pp(result)
    except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get billing item information faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to cancel the subnets faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```
