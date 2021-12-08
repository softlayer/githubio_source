---
title: "deleteObject"
description: "Customer users can only delete permission roles with systemFlag set to false.  The SYSTEM type is reserved for internal... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Role"
aliases:
    - "/reference/services/softlayer_user_permission_role/deleteObject"
---
# [SoftLayer_User_Permission_Role](/reference/services/SoftLayer_User_Permission_Role)::deleteObject


Delete a new customer permission role


## Overview 
Customer users can only delete permission roles with systemFlag set to false.  The SYSTEM type is reserved for internal use. The user who is creating the permission role must have the permission to manage users. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_Permission_RoleInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot delete role: Permission Denied." if a customer user attempts to delete a permission role without the proper permission. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot delete system role" if a customer user attempts to delete a SYSTEM permission role. 



