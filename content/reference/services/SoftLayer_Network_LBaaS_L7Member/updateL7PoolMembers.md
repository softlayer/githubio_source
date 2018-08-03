---
title: "updateL7PoolMembers"
description: "Update L7 members weight and port."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Member"
aliases:
    - "/reference/services/softlayer_network_lbaas_l7member/updateL7PoolMembers"
---
# [SoftLayer_Network_LBaaS_L7Member](/reference/services/SoftLayer_Network_LBaaS_L7Member)::updateL7PoolMembers

Update l7 members weight and port


## Overview 
Update L7 members weight and port. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|l7PoolUuid| string| |
|members| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Member'>SoftLayer_Network_LBaaS_L7Member[] </a>| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_LBaaS_L7MemberObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>

