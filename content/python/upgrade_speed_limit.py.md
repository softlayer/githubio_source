---
title: "upgrade_speed_limit.py"
description: "upgrade_speed_limit.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
tags:
    - "loadbalancers"
---


```
"""
Upgrade the connection limit for a load balancer

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/upgradeConnectionLimit

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

loadBalancerId = 79945

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
loadBalancerService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress']

try:
    result = loadBalancerService.upgradeConnectionLimit(id=loadBalancerId)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to upgrade . faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
