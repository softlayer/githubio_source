---
title: "scaleTo"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group"
---
# [SoftLayer_Scale_Group](/reference/services/SoftLayer_Scale_Group)::scaleTo

Scale this group up or down to the number given. This call will add or remove as many guests as necessary, but will NOT go beyond the limits set by minimumMemberCount and maximumMemberCount. This call and its result are the equivalent of calling scale(number - virtualGuestMemberCount). This call can only be invoked on an active group and does not respect cooldown (i.e. even if in a cooldown period, the scaling will still occur). 


## Overview 


### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|number| integer| The number to reach|


### Required Headers
* authenticate
* SoftLayer_Scale_GroupInitParameters

### Optional Headers
* SoftLayer_Scale_GroupObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Scale_Member'>SoftLayer_Scale_Member[] </a>

