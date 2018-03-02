---
title: "addLoadBalancerMembers"
description: "Add server instances as members to load balancer and return it with listeners, pools and members populated"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Member"
---
# SoftLayer_Network_LBaaS_Member::addLoadBalancerMembers
## Overview 
Add server instances as members to load balancer and return it with listeners, pools and members populated 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancerUuid| string| |
|serverInstances| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancerServerInstanceInfo'>SoftLayer_Network_LBaaS_LoadBalancerServerInstanceInfo[] </a>| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_LBaaS_MemberObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>

