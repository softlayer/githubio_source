---
title: "deleteL7PoolMembers"
description: "Delete given members from load balancer and return load balancer object with listeners, pools and members populated"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Member"
aliases:
    - "/reference/services/softlayer_network_lbaas_l7member/deleteL7PoolMembers"
---
# [SoftLayer_Network_LBaaS_L7Member](/reference/services/SoftLayer_Network_LBaaS_L7Member)::deleteL7PoolMembers


Delete load balancer members


## Overview 
Delete given members from load balancer and return load balancer object with listeners, pools and members populated 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|l7PoolUuid| string| |
|memberUuids| array of strings| |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_LBaaS_L7MemberObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>




