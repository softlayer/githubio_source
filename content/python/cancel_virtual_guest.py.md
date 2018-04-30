---
title: "cancel_virtual_guest.py"
description: "cancel_virtual_guest.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Billing_Item"
tags:
    - "virtualserver"
---


```
"""
Cancel a Virtual Guest.
It cancels the resource for a billing Item. The billing item will be cancelled
immediately and reclaim of the resource will begin shortly.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

virtualGuestId = 35747489

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY,
)

try:
    # Getting the billing item id
    mask = 'mask.billingItem.id'
    cci = client['SoftLayer_Virtual_Guest'].getObject(mask=mask, id=virtualGuestId)
    billingItemId = cci['billingItem']['id']

    try:
        # Canceling the Virtual Guest
        result = client['Billing_Item'].cancelService(id=billingItemId)
        pp(result)
    except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to cancel the VSI faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get the billing item id from VSI faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```
