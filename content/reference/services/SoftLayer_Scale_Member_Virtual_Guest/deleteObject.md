---
title: "deleteObject"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Member_Virtual_Guest"
---
# [SoftLayer_Scale_Member_Virtual_Guest](/reference/services/SoftLayer_Scale_Member_Virtual_Guest)::deleteObject

Delete this group member. Note, this can only be done on an active group when it wont cause the group to go below its minimumMemberCount. This is not the recommended way to delete members. Instead, users should invoke scale(-1) on SoftLayer_Scale_Group so it can choose the best guest member to remove. 


## Overview 


### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Scale_Member_Virtual_GuestInitParameters

### Optional Headers

### Return Values
boolean

