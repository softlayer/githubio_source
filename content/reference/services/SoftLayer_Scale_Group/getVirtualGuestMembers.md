---
title: "getVirtualGuestMembers"
description: "Retrieve collection of guests that have been scaled with the group. When this group is active, the count of guests here... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group"
aliases:
    - "/reference/services/softlayer_scale_group/getVirtualGuestMembers"
---
# [SoftLayer_Scale_Group](/reference/services/SoftLayer_Scale_Group)::getVirtualGuestMembers

Retrieve collection of guests that have been scaled with the group. When this group is active, the count of guests here is guaranteed to be between minimumMemberCount and maximumMemberCount inclusively.


## Overview 
Retrieve collection of guests that have been scaled with the group. When this group is active, the count of guests here is guaranteed to be between minimumMemberCount and maximumMemberCount inclusively.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Scale_GroupInitParameters
* authenticate

### Optional Headers
* SoftLayer_Scale_GroupObjectMask
* SoftLayer_Scale_GroupObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Scale_Member'>SoftLayer_Scale_Member[] </a>

