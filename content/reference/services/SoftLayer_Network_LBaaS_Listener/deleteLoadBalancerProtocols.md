---
title: "deleteLoadBalancerProtocols"
description: "Delete load balancers front- and backend protocols and return load balancer object with listeners (frontend), pools (bac... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Listener"
---
# [SoftLayer_Network_LBaaS_Listener](/reference/services/SoftLayer_Network_LBaaS_Listener)::deleteLoadBalancerProtocols

Delete load balancers front- and backend protocols


## Overview 
Delete load balancers front- and backend protocols and return load balancer object with listeners (frontend), pools (backend), server instances (members) and datacenter populated. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancerUuid| string| $loadBalancerUuid|
|listenerUuids| array of strings| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_LBaaS_ListenerObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>

