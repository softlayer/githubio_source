---
title: "cancel_cdn.py"
description: "cancel_cdn.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item_Cancellation_Request"
tags:
    - "cdn"
---


```
"""
Cancel CDN.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item_Cancellation_Request/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account/
http://sldn.softlayer.com/article/Object-Filters
http://sldn.softlayer.com/article/Object-Masks

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer.API
import json

USERNAME = 'set me'
API_KEY = 'set me'

# The name of the CDN to cancel.
cdnAccountName = "14793"
immediateCancellation = True


client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
billingService = client['SoftLayer_Billing_Item_Cancellation_Request']
accountService = client['SoftLayer_Account']

# Set an object mask to get the billing item associated to the CDNN.
objectMask = "mask[billingItem]"

# Set an object filter to get only the configured CDN to delete in the result.
objectFilter = {"cdnAccounts": {"cdnAccountName": {"operation": cdnAccountName}}}

try:
    # Geting the CDN to delete
    cdns = accountService.getCdnAccounts(filter=objectFilter, mask=objectMask)
    if len(cdns) == 0:
        print ("The configured CDN: " + cdnAccountName + " does not exist in the account")
        exit(1)
    # Create the SoftLayer_Billing_Item_Cancellation_Request skeleton to create the cancelation request
    template = {
        "accountId": cdns[0]['accountId'],
        "items": [
            {
                "billingItemId": cdns[0]['billingItem']['id'],
                "immediateCancellationFlag": immediateCancellation
            }
        ]
    }
    result = billingService.createObject(template)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to create the cancel request"
          % (e.faultCode, e.faultString))
    exit(1)

```
