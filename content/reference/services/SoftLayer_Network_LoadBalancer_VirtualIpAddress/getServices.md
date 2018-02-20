---
title: "getServices"
description: "Retrieve the services on this load balancer."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
---
# SoftLayer_Network_LoadBalancer_VirtualIpAddress::getServices
## Overview 
Retrieve the services on this load balancer.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_LoadBalancer_VirtualIpAddressInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_LoadBalancer_VirtualIpAddressObjectMask
* SoftLayer_Network_LoadBalancer_VirtualIpAddressObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Service'>SoftLayer_Network_LoadBalancer_Service[] </a>
