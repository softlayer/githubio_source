---
title: "editObject"
description: "Allows a user to modify the name and description of an existing customer permission group. Customer permission groups mu... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
aliases:
    - "/reference/services/softlayer_user_permission_group/editObject"
---
# [SoftLayer_User_Permission_Group](/reference/services/SoftLayer_User_Permission_Group)::editObject

Edit an existing customer permission group


## Overview 
Allows a user to modify the name and description of an existing customer permission group. Customer permission groups must be of type NORMAL.  The SYSTEM type is reserved for internal use. The account id supplied in the template permission group must match account id of the user who is creating the permission group.  The user who is creating the permission group must have the permission to manage users. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_User_Permission_Group'>SoftLayer_User_Permission_Group </a>| A skeleton SoftLayer_User_Permission_Group object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_GroupInitParameters


### Optional Headers
* SoftLayer_User_Permission_GroupObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Permission_Group'>SoftLayer_User_Permission_Group </a>



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot edit group: Permission Denied." if a customer user attempts to edit a permission group without the proper permission. 



