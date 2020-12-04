---
title: "deleteObject"
description: "Customer users can only delete permission groups of type NORMAL.  The SYSTEM type is reserved for internal use. The user... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
aliases:
    - "/reference/services/softlayer_user_permission_group/deleteObject"
---
# [SoftLayer_User_Permission_Group](/reference/services/SoftLayer_User_Permission_Group)::deleteObject

Delete a new customer permission group


## Overview 
Customer users can only delete permission groups of type NORMAL.  The SYSTEM type is reserved for internal use. The user who is creating the permission group must have the permission to manage users. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_Permission_GroupInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot delete group: Permission Denied." if a customer user attempts to delete a permission group without the proper permission. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot delete system group" if a customer user attempts to delete a SYSTEM permission group. 



