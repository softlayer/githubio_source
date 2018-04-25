---
title: "load_balancer_edit.py"
description: "load_balancer_edit.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
tags:
    - "loadbalancers"
---


```
"""
Edit load balancer

The script edits the configuration of an existing load balancer,
it makes a single call to the
SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress::editObject
method. For more information please see below.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
http://sldn.softlayer.com/reference/services/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/editObject

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Creating an skeleton object SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
# which contains the configuration for our load balancer
templateObject = {
    'id': 35026,
    'virtualServers': [{
        'port': 30,
        'allocation': 100,
        'id': 83554,
        'virtualIpAddressId': 35026,
        'serviceGroups': [{
            'timeout': '',
            'notes': 'testhttp3',
            'id': 86554,
            'routingTypeId': 2,
            'routingMethodId': 10}],
    }]
}

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
service = client['SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress']

try:
    result = service.editObject(templateObject, id=35026)
    print(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to edit the load balancer faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
