---
title: "add_service_group.py"
description: "add_service_group.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method"
tags:
    - "loadbalancers"
---


```
"""
Add a new service group.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/editObject
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type/getAllObjects
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method/getAllObjects

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

loadBalancerId = 79945

# The new allocation value for the service groups.
# The sum of the allocation of all your services group must be 100.
# If you add a new service group it is required to change the allocation
# value of the previous service groups into the load balancer.
# note: the last value is for the new service group you wish to add.
newAllocations = [40, 20, 20, 10, 10]

# The port must unique among the service groups into the load balancer
port = 4040

notes = 'my group note'

method = 'Shortest Response'

group = 'HTTP'

timeout = ""

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
loadBalancerService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress']
groupService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type']
methodService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method']
objectMask = "mask[virtualServers[serviceGroups]]"
groupFilter = {"name": {"operation": group}}
methodFilter = {"name": {"operation": method}}

try:
    group = groupService.getAllObjects(filter=groupFilter)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the group. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

try:
    method = methodService.getAllObjects(filter=methodFilter)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the method. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

try:
    virtualServer = {
        'port': port,
        'serviceGroups': [
            {
                'routingMethodId': group[0]['id'],
                'routingTypeId': method[0]['id'],
                'notes': notes,
                'timeout': timeout
            }
        ]
    }
    loadBalancer = loadBalancerService.getObject(id=loadBalancerId, mask=objectMask)
    result = loadBalancerService.editObject(loadBalancer, id=loadBalancerId)
    if 'virtualServers' not in loadBalancer:
         loadBalancer['virtualServers'] = []
    loadBalancer['virtualServers'].append(virtualServer)
    if len(loadBalancer['virtualServers']) == len(newAllocations):
        for index in range(len(newAllocations)):
            loadBalancer['virtualServers'][index]['allocation'] = newAllocations[index]
        result = loadBalancerService.editObject(loadBalancer, id=loadBalancerId)
        print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
    else:
        print ("Error the number of configured allocations is not the same as the service groups in the load balancer.")
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to add the service group. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
