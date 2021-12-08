---
title: "getL7PoolMemberHealth"
description: "Returns the health of all L7 pool's members which are created under load balancer. L7 members health status is available... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Pool"
aliases:
    - "/reference/services/softlayer_network_lbaas_l7pool/getL7PoolMemberHealth"
---
# [SoftLayer_Network_LBaaS_L7Pool](/reference/services/SoftLayer_Network_LBaaS_L7Pool)::getL7PoolMemberHealth


Return load balancer's all L7 pools members health


## Overview 
Returns the health of all L7 pool's members which are created under load balancer. L7 members health status is available only after a L7 pool is associated with the L7 policy and that L7 policy has at least one L7 rule. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancerUuid| string| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7PoolMembersHealth'>SoftLayer_Network_LBaaS_L7PoolMembersHealth[] </a>




