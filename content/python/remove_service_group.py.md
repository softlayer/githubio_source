---
title: "remove_service_group.py"
description: "remove_service_group.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer"
tags:
    - "loadbalancers"
---


```
"""
Remove a service group from a load balancer.

Important manual pages:
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer/
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer/deleteObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The virtual server which contains the service group to delete.
virtualServerId = 193563

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
virtualService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer']

try:
    result = virtualService.deleteObject(id=virtualServerId)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to remove the service group. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
