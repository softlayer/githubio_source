---
title: "getVip"
description: "Retrieve the load balancer that this service belongs to."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
---
# SoftLayer_Network_LoadBalancer_Service::getVip
## Overview 
Retrieve the load balancer that this service belongs to.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_LoadBalancer_ServiceInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_LoadBalancer_ServiceObjectMask
* SoftLayer_Network_LoadBalancer_ServiceObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress </a>
