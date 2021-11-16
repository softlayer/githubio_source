---
title: "updateLoadBalancerMembers"
description: "Update members weight and return load balancer object with listeners, pools and members populated"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Member"
aliases:
    - "/reference/services/softlayer_network_lbaas_member/updateLoadBalancerMembers"
---
# [SoftLayer_Network_LBaaS_Member](/reference/services/SoftLayer_Network_LBaaS_Member)::updateLoadBalancerMembers


Update members weight


## Overview 
Update members weight and return load balancer object with listeners, pools and members populated 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancerUuid| string| |
|members| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_Member'>SoftLayer_Network_LBaaS_Member[] </a>| |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_LBaaS_MemberObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>




