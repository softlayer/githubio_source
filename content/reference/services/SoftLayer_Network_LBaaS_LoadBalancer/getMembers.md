---
title: "getMembers"
description: "Retrieve members assigned to load balancer."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancer"
---
# SoftLayer_Network_LBaaS_LoadBalancer::getMembers
## Overview 
Retrieve members assigned to load balancer.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_LBaaS_LoadBalancerInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_LBaaS_LoadBalancerObjectMask
* SoftLayer_Network_LBaaS_LoadBalancerObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LBaaS_Member'>SoftLayer_Network_LBaaS_Member[] </a>
