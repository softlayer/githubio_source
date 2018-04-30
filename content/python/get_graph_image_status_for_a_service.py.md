---
title: "get_graph_image_status_for_a_service.py"
description: "get_graph_image_status_for_a_service.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service"
tags:
    - "loadbalancers"
---


```
"""
Get graph image status for a service.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service/getGraphImage

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

serviceId = 367025

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
service = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service']

graphType = 'status'

# The metric can be 'day', 'week', or 'month'.
metric = 'day'

try:
    result = service.getGraphImage(graphType, metric, id=serviceId)
    print("The graph image has been retrieved successfully")
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the graph image. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
