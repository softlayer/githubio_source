---
title: "get_graph_image_connections_for_a_service_group.py"
description: "get_graph_image_connections_for_a_service_group.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group"
tags:
    - "loadbalancers"
---


```
"""
Get graph image connections for a service group.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group/getGraphImage

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

serviceGroupId = 138193

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
serviceGroupService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group']

graphType = 'connections'

# The metric can be 'day', 'week', or 'month'.
metric = 'day'

try:
    result = serviceGroupService.getGraphImage(graphType, metric, id=serviceGroupId)
    print("The graph image has been retrieved successfully")
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the graph image. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
