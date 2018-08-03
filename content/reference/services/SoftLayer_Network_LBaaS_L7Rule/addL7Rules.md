---
title: "addL7Rules"
description: "This function creates and adds multiple Rules to a given L7 policy with all the details provided for rules"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Rule"
aliases:
    - "/reference/services/softlayer_network_lbaas_l7rule/addL7Rules"
---
# [SoftLayer_Network_LBaaS_L7Rule](/reference/services/SoftLayer_Network_LBaaS_L7Rule)::addL7Rules

Create and add a L7 Rule to a given L7 policy with the provided rules details. 


## Overview 
This function creates and adds multiple Rules to a given L7 policy with all the details provided for rules 

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
<a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer'>SoftLayer_Network_LBaaS_LoadBalancer </a>

