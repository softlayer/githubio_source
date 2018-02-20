---
title: "deleteLoadBalancerMembers"
description: "Delete given members from load balancer and return load balancer object with listeners, pools and members populated"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Member"
---
# SoftLayer_Network_LBaaS_Member::deleteLoadBalancerMembers
## Overview 
Delete given members from load balancer and return load balancer object with listeners, pools and members populated 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancerUuid| string| |
|memberUuids| array of strings| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_LBaaS_MemberObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>
