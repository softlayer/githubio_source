---
title: "get_load_balancer_by_order_id.py"
description: "get_load_balancer_by_order_id.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
tags:
    - "loadbalancers"
---


```
"""
Get a load balancer given the order id.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getAdcLoadBalancers
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

orderId = 5980963

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

filterDedicated = {"adcLoadBalancers": {"dedicatedBillingItem": {"orderItem": {"order": {"id":  {"operation": orderId}}}}}}
filter = {"adcLoadBalancers": {"billingItem": {"orderItem": {"order": {"id":  {"operation": orderId}}}}}}

try:
    loadBalancers = accountService.getAdcLoadBalancers(filter=filter)
    if len(loadBalancers) == 0:
        loadBalancers = accountService.getAdcLoadBalancers(filter=filterDedicated)
        if len(loadBalancers) == 0:
            print ("There is no a load balancer with an orderId: " + str(orderId))
        else:
            print(json.dumps(loadBalancers, sort_keys=True, indent=2, separators=(',', ': ')))
    else:
        print(json.dumps(loadBalancers, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the load balancer. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
