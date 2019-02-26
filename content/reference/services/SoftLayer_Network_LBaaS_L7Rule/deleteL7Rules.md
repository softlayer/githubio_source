---
title: "deleteL7Rules"
description: "This function deletes multiple rules aassociated with the same policy."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Rule"
aliases:
    - "/reference/services/softlayer_network_lbaas_l7rule/deleteL7Rules"
---
# [SoftLayer_Network_LBaaS_L7Rule](/reference/services/SoftLayer_Network_LBaaS_L7Rule)::deleteL7Rules

Delete one or more rules associated with the same policy. 


## Overview 
This function deletes multiple rules aassociated with the same policy. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|policyUuid| string| |
|ruleUuids| array of strings| |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_LBaaS_L7RuleObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>




