---
title: "deleteObject"
description: "Delete this group. This can only be done on an empty, active group. This means that minimumMemberCount must be 0 since i... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group"
aliases:
    - "/reference/services/softlayer_scale_group/deleteObject"
---
# [SoftLayer_Scale_Group](/reference/services/SoftLayer_Scale_Group)::deleteObject


Delete this group. This can only be done on an empty, active group. 


## Overview 
Delete this group. This can only be done on an empty, active group. This means that minimumMemberCount must be 0 since it is the only way for a group to have no group members. To delete a group and all of its members at the same time, use forceDeleteObject. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Scale_GroupInitParameters


### Return Values
* boolean




