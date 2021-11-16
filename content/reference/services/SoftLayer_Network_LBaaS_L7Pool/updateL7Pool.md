---
title: "updateL7Pool"
description: "Updates an existing L7 pool, L7 health monitor and L7 session affinity."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Pool"
aliases:
    - "/reference/services/softlayer_network_lbaas_l7pool/updateL7Pool"
---
# [SoftLayer_Network_LBaaS_L7Pool](/reference/services/SoftLayer_Network_LBaaS_L7Pool)::updateL7Pool


updates L7 pools


## Overview 
Updates an existing L7 pool, L7 health monitor and L7 session affinity. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|l7PoolUuid| string| |
|l7Pool| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Pool'>SoftLayer_Network_LBaaS_L7Pool </a>| |
|l7HealthMonitor| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7HealthMonitor'>SoftLayer_Network_LBaaS_L7HealthMonitor </a>| |
|l7SessionAffinity| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7SessionAffinity'>SoftLayer_Network_LBaaS_L7SessionAffinity </a>| |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_LBaaS_L7PoolObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>




