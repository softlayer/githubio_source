---
title: "updateSslCiphers"
description: "Updates the load balancer with the new cipher list. All new connections going forward will use the new set of ciphers se... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancer"
aliases:
    - "/reference/services/softlayer_network_lbaas_loadbalancer/updateSslCiphers"
---
# [SoftLayer_Network_LBaaS_LoadBalancer](/reference/services/SoftLayer_Network_LBaaS_LoadBalancer)::updateSslCiphers

Updates the cipher list of the load balancer


## Overview 
Updates the load balancer with the new cipher list. All new connections going forward will use the new set of ciphers selected by the user. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|loadBalancerUuid| string| |
|cipherList| array of integers| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_LBaaS_LoadBalancerObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>

