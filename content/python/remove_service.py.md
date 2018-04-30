---
title: "remove_service.py"
description: "remove_service.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service"
tags:
    - "loadbalancers"
---


```
"""
Remove a service from a load balancer.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service/deleteObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# The service id to delete.
serviceId = 367111

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
service = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service']

try:
    result = service.deleteObject(id=serviceId)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to remove the service. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
