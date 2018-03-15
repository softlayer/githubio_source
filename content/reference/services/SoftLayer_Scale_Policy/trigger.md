---
title: "trigger"
description: "Manually trigger the actions on this policy. Returns members if the trigger has an effect, or an empty set of members if... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Policy"
aliases:
    - "/reference/services/softlayer_scale_policy/trigger"
---
# [SoftLayer_Scale_Policy](/reference/services/SoftLayer_Scale_Policy)::trigger

Manually trigger the actions on this policy. 


## Overview 
Manually trigger the actions on this policy. Returns members if the trigger has an effect, or an empty set of members if there is no effect. Sometimes this may not have an effect if the group is not active, in cooldown, or the result would violate the group range. If this call fails, the group is suspended, the failure logged, and a ticket is created. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Scale_PolicyInitParameters

### Optional Headers
* SoftLayer_Scale_PolicyObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Scale_Member'>SoftLayer_Scale_Member[] </a>

