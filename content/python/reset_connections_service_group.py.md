---
title: "reset_connections_service_group.py"
description: "reset_connections_service_group.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group"
tags:
    - "loadbalancers"
---


```
"""
Reset the connections for a service group.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group/kickAllConnections

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

serviceGroupId = 138193

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
serviceGroupService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group']

try:
    result = serviceGroupService.kickAllConnections(id=serviceGroupId)
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to reset the connections. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
