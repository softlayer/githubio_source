---
title: "editObject"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group"
---
# [SoftLayer_Scale_Group](/reference/services/SoftLayer_Scale_Group)::editObject

Edit this group. The name can be edited at any time. The minimumMemberCount and maximumMemberCount fields can also be edited at any time provided they don't force a scale up or scale down to bring the group into the proper range. Otherwise, the group's status must be active to set those fields. If the group member count is less than the new minimumMemberCount and the group is active, it will scale up the group members to reach the new minimum. Similarly if the group member count is greater than the new maximumMemberCount and the group is active, it will scale down the group members to reach the new maximum. 

When editing an active group, a special field can be provided: desiredMemberCount. When given, the group members are automatically scaled up or down to reach that number. 


## Overview 


### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Scale_Group'>SoftLayer_Scale_Group </a>| A skeleton SoftLayer_Scale_Group object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Scale_GroupInitParameters

### Optional Headers

### Return Values
boolean

