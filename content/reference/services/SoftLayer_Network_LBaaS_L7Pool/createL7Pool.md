---
title: "createL7Pool"
description: "Create a backend to be used for L7 load balancing. This L7 pool has backend protocol, L7 members, L7 health monitor and... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Pool"
aliases:
    - "/reference/services/softlayer_network_lbaas_l7pool/createL7Pool"
---
# [SoftLayer_Network_LBaaS_L7Pool](/reference/services/SoftLayer_Network_LBaaS_L7Pool)::createL7Pool

create L7 pools


## Overview 
Create a backend to be used for L7 load balancing. This L7 pool has backend protocol, L7 members, L7 health monitor and session affinity. L7 pool is associated with L7 policies. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancerUuid| string| |
|l7Pool| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Pool'>SoftLayer_Network_LBaaS_L7Pool </a>| |
|l7Members| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Member'>SoftLayer_Network_LBaaS_L7Member[] </a>| |
|l7HealthMonitor| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7HealthMonitor'>SoftLayer_Network_LBaaS_L7HealthMonitor </a>| |
|l7SessionAffinity| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7SessionAffinity'>SoftLayer_Network_LBaaS_L7SessionAffinity </a>| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_LBaaS_L7PoolObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>

