---
title: "scale"
description: "Scale this group up or down by the amount given. If the number is negative, the given amount of guest members are remove... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group"
aliases:
    - "/reference/services/softlayer_scale_group/scale"
---
# [SoftLayer_Scale_Group](/reference/services/SoftLayer_Scale_Group)::scale


Scale this group up or down by the amount given. 


## Overview 
Scale this group up or down by the amount given. If the number is negative, the given amount of guest members are removed. Similarly, if the number is positive, the given amount of guest members are added. Note, this call will add or remove as much as asked for, but will NOT go beyond the limits set by minimumMemberCount and maximumMemberCount. The result is a collection of SoftLayer_Scale_Member instances that were either removed or added. This call can only be invoked on an active group and does not respect cooldown (i.e. even if in a cooldown period, the scaling will still occur). 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|delta| integer| Positive or negative value to scale.|


### Required Headers
* authenticate
* SoftLayer_Scale_GroupInitParameters


### Optional Headers
* SoftLayer_Scale_GroupObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Scale_Member'>SoftLayer_Scale_Member[] </a>




