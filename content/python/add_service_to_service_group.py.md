---
title: "add_service_to_service_group.py"
description: "add_service_to_service_group.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type"
tags:
    - "loadbalancers"
---


```
"""
Add a new service to a service group.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/editObject
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type/getAllObjects
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet_IpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet_IpAddress/findByIpv4Address

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

loadBalancerId = 79945

serviceGroupId = 138193

destinationIpAddress = "169.53.15.53"

destinationPort = 40

weight = 10

notes = "my service group note"

enabled = True

healthCheck = "Ping"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
loadBalancerService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress']
healthService = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type']
ipService = client['SoftLayer_Network_Subnet_IpAddress']
heaqlthFilter = {"name": {"operation": healthCheck}}
objectMask = "mask[sslActiveFlag, notes, sslEnabledFlag, loadBalancerHardware[hostname,datacenterName,location,locationPathString], ipAddress, virtualServers[notes,port,id,allocation,serviceGroups[services[groupReferences[weight],healthChecks[type[id,name],attributes],ipAddress[id,ipAddress]],routingMethod,routingType]]]"

try:
    healthCheck = healthService.getAllObjects(filter=heaqlthFilter)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the health check. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

try:
    destinationIpAddress = ipService.findByIpv4Address(destinationIpAddress)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the IP address. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

try:
    loadBalancer = loadBalancerService.getObject(id=loadBalancerId, mask=objectMask)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the load balancer. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

serviceGroup = {}
for i in range(len(loadBalancer['virtualServers'])):
    for j in range(len(loadBalancer['virtualServers'][i]['serviceGroups'])):
        if loadBalancer['virtualServers'][i]['serviceGroups'][j]['id'] == serviceGroupId:
            serviceGroup = loadBalancer['virtualServers'][i]['serviceGroups'][j]
            break

if 'id' not in serviceGroup:
    print("Unable to get the service group id: " + str(serviceGroupId) + " in the load balancer")
else:
    newService = {}
    newService['enabled'] = enabled
    newService['groupReferences'] = []
    groupReferences = {}
    groupReferences['weight'] = weight
    newService['groupReferences'].append(groupReferences)
    newService['healthChecks'] = []
    healthChecks = {}
    healthChecks['healthCheckTypeId'] = healthCheck[0]['id']
    newService['healthChecks'].append(healthChecks)
    newService['ipAddressId'] = destinationIpAddress['id']
    newService['port'] = destinationPort
    newService['notes'] = notes
    loadBalancer['virtualServers'][i]['serviceGroups'][j]['services'].append(newService)
    try:
        result = loadBalancerService.editObject(loadBalancer, id=loadBalancerId)
        print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to add the service to the service group. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
