---
title: "get_load_balancer_details.py"
description: "get_load_balancer_details.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
tags:
    - "loadbalancers"
---


```
"""
Get the details for a load balancer.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/getObject

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

objectMask = "mask[sslActiveFlag, notes, sslEnabledFlag, loadBalancerHardware[hostname,datacenterName,location,locationPathString], ipAddress, virtualServers[notes,port,id,allocation,serviceGroups[services[groupReferences[weight],healthChecks[type[id,name],attributes],ipAddress[id,ipAddress]],routingMethod,routingType]]]"

try:
    result = loadBalancerService.getObject(id=loadBalancerId, mask=objectMask)
    details = {}
    details['ip'] = result['ipAddress']['ipAddress']
    details['name'] = result['loadBalancerHardware'][0]['hostname']
    details['location'] = result['loadBalancerHardware'][0]['datacenterName']
    if result['sslEnabledFlag']:
        if result['sslActiveFlag']:
            details['ssl'] = "Enabled"
        else:
            details['ssl'] = "Disabled"
    else:
        details['ssl'] = "Not Supported"
    if 'notes' in result:
        details['notes'] = result['notes']
    else:
        details['notes'] = ""
    serviceGroups = []
    for virtualServer in result['virtualServers']:
        group = {}
        group['virtualPort'] = virtualServer['port']
        group['virtualServerId'] = virtualServer['id']
        group['allocation'] = virtualServer['allocation']
        group['notes'] = virtualServer['serviceGroups'][0]['notes']
        group['method'] = virtualServer['serviceGroups'][0]['routingMethod']['name']
        group['group'] = virtualServer['serviceGroups'][0]['routingType']['name']
        group['customTimeout'] = virtualServer['serviceGroups'][0]['timeout']
        group['serverGroupId'] = virtualServer['serviceGroups'][0]['id']
        serviceGroups.append(group)
        services = []
        for service in virtualServer['serviceGroups'][0]['services']:
            newService = {}
            newService['id'] = service['id']
            newService['enabled'] = service['enabled']
            newService['notes'] = service['notes']
            newService['destinationPort'] = service['port']
            newService['destinationIp'] = service['ipAddress']['ipAddress']
            newService['healthCheck'] = service['healthChecks'][0]['type']['name']
            if 'attributes' in service['healthChecks'][0]:
                if len(service['healthChecks'][0]['attributes']) > 0:
                    customHealth = {}
                    for attribute in service['healthChecks'][0]['attributes']:
                        if attribute['healthAttributeTypeId'] == 22:
                            customHealth['type'] = attribute['value']
                        if attribute['healthAttributeTypeId'] == 23:
                            customHealth['location'] = attribute['value']
                        if attribute['healthAttributeTypeId'] == 24:
                            customHealth['response'] = attribute['value']
                    newService['customHealthCheck'] = customHealth
            newService['weight'] = service['groupReferences'][0]['weight']
            services.append(newService)
        group['services'] = services
    details['serviceGroups'] = serviceGroups
    print(json.dumps(details, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the load balancer details. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
