---
title: "editObject"
description: "Allows a user to modify the name and description of an existing customer permission role. Customer permission roles must... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Role"
aliases:
    - "/reference/services/softlayer_user_permission_role/editObject"
---
# [SoftLayer_User_Permission_Role](/reference/services/SoftLayer_User_Permission_Role)::editObject


Edit an existing customer permission role


## Overview 
Allows a user to modify the name and description of an existing customer permission role. Customer permission roles must set the systemFlag attribute to false.  The SYSTEM type is reserved for internal use. The account id supplied in the template permission role must match account id of the user who is creating the permission role.  The user who is creating the permission role must have the permission to manage users. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_User_Permission_Role'>SoftLayer_User_Permission_Role </a>| A skeleton SoftLayer_User_Permission_Role object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_RoleInitParameters


### Optional Headers
* SoftLayer_User_Permission_RoleObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Permission_Role'>SoftLayer_User_Permission_Role </a>



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot edit role: Permission Denied." if a customer user attempts to edit a permission role without the proper permission. 



