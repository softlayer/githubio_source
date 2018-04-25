---
title: "cancel_load_balancer.py"
description: "cancel_load_balancer.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
    - "SoftLayer_Billing_Item_Cancellation_Request"
tags:
    - "loadbalancers"
---


```
"""
Cancel load balancer.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item_Cancellation_Request
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item_Cancellation_Request
http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item_Cancellation_Request/createObject
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

loadBalancerId = 109225

immediateCancellationFlag = True

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
loadBalancerService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress']
cancellationService = client['SoftLayer_Billing_Item_Cancellation_Request']

objectMask = "mask[accountId, dedicatedFlag,dedicatedBillingItem[id],billingItem[id]]"

try:
    loadBalancer = loadBalancerService.getObject(id=loadBalancerId, mask=objectMask)
    billingItemId = 0
    if loadBalancer['dedicatedFlag']:
        billingItemId = loadBalancer['dedicatedBillingItem']['id']
    else:
        billingItemId = loadBalancer['billingItem']['id']
    cancelTemplate = {
        'accountId': loadBalancer['accountId'],
        'items': [
            {
                'billingItemId': billingItemId,
                'immediateCancellationFlag': immediateCancellationFlag
            }
        ]
    }
    result = cancellationService.createObject(cancelTemplate)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to cancel the load balancer. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
