---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_LoadBalancer_VirtualIpAddress object whose ID number corresponds to the ID num... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
---
# [SoftLayer_Network_LoadBalancer_VirtualIpAddress](/reference/services/SoftLayer_Network_LoadBalancer_VirtualIpAddress)::getObject

Retrieve a SoftLayer_Network_LoadBalancer_VirtualIpAddress record.


## Overview 
getObject retrieves the SoftLayer_Network_LoadBalancer_VirtualIpAddress object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_LoadBalancer_VirtualIpAddress service. You can only retrieve Load Balancers assigned to your account. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_LoadBalancer_VirtualIpAddressInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_LoadBalancer_VirtualIpAddressObjectMask
* SoftLayer_Network_LoadBalancer_VirtualIpAddressObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress </a>

