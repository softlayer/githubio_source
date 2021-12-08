---
title: "addL7Policies"
description: "This function creates multiple policies with rules for the given listener."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Policy"
aliases:
    - "/reference/services/softlayer_network_lbaas_l7policy/addL7Policies"
---
# [SoftLayer_Network_LBaaS_L7Policy](/reference/services/SoftLayer_Network_LBaaS_L7Policy)::addL7Policies


Create layer 7 policies with rules for the given listener. 


## Overview 
This function creates multiple policies with rules for the given listener. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|listenerUuid| string| |
|policiesRules| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_PolicyRule'>SoftLayer_Network_LBaaS_PolicyRule[] </a>| |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_LBaaS_L7PolicyObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>




