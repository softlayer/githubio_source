---
title: "createObject"
description: "Customer created permission groups must be of type NORMAL.  The SYSTEM type is reserved for internal use. The account id... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
aliases:
    - "/reference/services/softlayer_user_permission_group/createObject"
---
# [SoftLayer_User_Permission_Group](/reference/services/SoftLayer_User_Permission_Group)::createObject


Create a new customer permission group


## Overview 
Customer created permission groups must be of type NORMAL.  The SYSTEM type is reserved for internal use. The account id supplied in the template permission group must match account id of the user who is creating the permission group.  The user who is creating the permission group must have the permission to manage users. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_User_Permission_Group'>SoftLayer_User_Permission_Group </a>| The SoftLayer_User_Permission_Group object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_User_Permission_GroupObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Permission_Group'>SoftLayer_User_Permission_Group </a>



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot create group: Permission Denied." if a customer user attempts to create a permission group without the proper permission. 

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot create system group" if a customer user attempts to create a SYSTEM permission group. 

* SoftLayer_Exception_User_Permission_AccountMismatch 

> Throws the exception "You cannot create Groups on other accounts." if a customer user attempts to create a permission group on an account other than their own. 



