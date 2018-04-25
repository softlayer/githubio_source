---
title: "cancel_storage.py"
description: "cancel_storage.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Storage"
tags:
    - "iscsi"
---


```
"""
Cancel Consistent Performance Storage iSCSI.
This script cancels the service of a Consistent Performance Storage iSCSI, passing a storage billing ID to
SoftLayer_Billing_Item::cancelService method.

See below references for more details.
Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
@License: http://sldn.softlayer.com/article/License
@Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# So we can talk to the SoftLayer API:
import SoftLayer

# For nice debug output:
import pprint

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'
API_KEY = 'set-me'
"""
Set storage Id to Cancel, you can get a list of network storage available in the account
using the SoftLayer_Account::getNetworkStorage method.
"""
storageId = 4471311
# Use the mask to get billing item from a network storage
billingMask = 'mask[billingItem]'
# Create a client instance
client = SoftLayer.Client(username=API_USERNAME, api_key=API_KEY)
storage = client['SoftLayer_Network_Storage'].getObject(mask=billingMask, id=storageId)

billingId = storage['billingItem']['id']
try:
    result = client['SoftLayer_Billing_Item'].cancelService(id=billingId)
    print("Service cancelled")
    pprint.pprint(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Error cannot cancel the service  faultCode=%s, faultString=%s"
          % (e.faultCode, e.faultString))
    exit(1)

```
