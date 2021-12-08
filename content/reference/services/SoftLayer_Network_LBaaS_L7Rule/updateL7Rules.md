---
title: "updateL7Rules"
description: "This function updates multiple Rules to a given policy with all the details for rules."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Rule"
aliases:
    - "/reference/services/softlayer_network_lbaas_l7rule/updateL7Rules"
---
# [SoftLayer_Network_LBaaS_L7Rule](/reference/services/SoftLayer_Network_LBaaS_L7Rule)::updateL7Rules


Update one or more rules associated with the same policy. 


## Overview 
This function updates multiple Rules to a given policy with all the details for rules. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|policyUuid| string| |
|rules| <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Rule'>SoftLayer_Network_LBaaS_L7Rule[] </a>| |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_LBaaS_L7RuleObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>




