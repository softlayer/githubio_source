---
title: "addL7PoolMembers"
description: "Add server instances as members to a L7pool and return the LoadBalancer Object with listeners, pools and members populat... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Member"
aliases:
    - "/reference/services/softlayer_network_lbaas_l7member/addL7PoolMembers"
---
# [SoftLayer_Network_LBaaS_L7Member](/reference/services/SoftLayer_Network_LBaaS_L7Member)::addL7PoolMembers


Add load balancer L7 members


## Overview 
Add server instances as members to a L7pool and return the LoadBalancer Object with listeners, pools and members populated 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|l7PoolUuid| string| |
|memberInstances| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Member'>SoftLayer_Network_LBaaS_L7Member[] </a>| |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_LBaaS_L7MemberObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>




