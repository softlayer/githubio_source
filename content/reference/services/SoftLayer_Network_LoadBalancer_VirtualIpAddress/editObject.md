---
title: "editObject"
description: "Like any other API object, the load balancers can have their exposed properties edited by passing in a modified version... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
aliases:
    - "/reference/services/softlayer_network_loadbalancer_virtualipaddress/editObject"
---
# [SoftLayer_Network_LoadBalancer_VirtualIpAddress](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress)::editObject

Edit the object by passing in a modified instance of the object


## Overview 
Like any other API object, the load balancers can have their exposed properties edited by passing in a modified version of the object.  The load balancer object also can modify its services in this way.  Simply request the load balancer object you wish to edit, then modify the objects in the services array and pass the modified object to this function.  WARNING:  Services cannot be deleted in this manner, you must call deleteObject() on the service to physically remove them from the load balancer. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress </a>| A skeleton SoftLayer_Network_LoadBalancer_VirtualIpAddress object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_VirtualIpAddressInitParameters

### Optional Headers

### Return Values
boolean

