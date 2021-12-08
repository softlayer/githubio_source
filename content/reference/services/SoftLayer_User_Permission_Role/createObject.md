---
title: "createObject"
description: "Customer created permission roles must set the systemFlag attribute to false.  The SYSTEM type is reserved for internal... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Role"
aliases:
    - "/reference/services/softlayer_user_permission_role/createObject"
---
# [SoftLayer_User_Permission_Role](/reference/services/SoftLayer_User_Permission_Role)::createObject


Create a new customer permission role


## Overview 
Customer created permission roles must set the systemFlag attribute to false.  The SYSTEM type is reserved for internal use. The account id supplied in the template permission group must match account id of the user who is creating the permission group.  The user who is creating the permission group must have the permission to manage users. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_User_Permission_Role'>SoftLayer_User_Permission_Role </a>| The SoftLayer_User_Permission_Role object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_User_Permission_RoleObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Permission_Role'>SoftLayer_User_Permission_Role </a>



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot create role: Permission Denied." if a customer user attempts to create a permission role without the proper permission. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot create system role" if a customer user attempts to create a SYSTEM permission role. 

* SoftLayer_Exception_User_Permission_AccountMismatch 

> Throws the exception "You cannot create Roles on other accounts." if a customer user attempts to create a permission role on an account other than their own. 



