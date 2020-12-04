---
title: "linkRole"
description: "Links a SoftLayer_User_Permission_Role object to the group."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
aliases:
    - "/reference/services/softlayer_user_permission_group/linkRole"
---
# [SoftLayer_User_Permission_Group](/reference/services/SoftLayer_User_Permission_Group)::linkRole

Links a permission role to the group.


## Overview 
Links a SoftLayer_User_Permission_Role object to the group. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|role| <a href='/reference/datatypes/SoftLayer_User_Permission_Role'>SoftLayer_User_Permission_Role </a>| Permission Role to be linked.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_GroupInitParameters


### Return Values
* void



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "Can't link role and group: Permission Denied." if a customer user attempts this request without the proper permission. 

* SoftLayer_Exception_User_Permission_Inaccessible 

> Throws the exception "Invalid role" if the permission role does not exist. 



