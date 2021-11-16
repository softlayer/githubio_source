---
title: "addUser"
description: "Assigns a SoftLayer_User_Customer object to the role."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Role"
aliases:
    - "/reference/services/softlayer_user_permission_role/addUser"
---
# [SoftLayer_User_Permission_Role](/reference/services/SoftLayer_User_Permission_Role)::addUser


Assign a user customer to the role.


## Overview 
Assigns a SoftLayer_User_Customer object to the role. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|user| <a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>| Add role to provided user.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_RoleInitParameters


### Return Values
* void



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "Can't add user to role: Permission Denied." if a customer user attempts this request without the proper permission. 

* SoftLayer_Exception_User_Permission_Inaccessible 

> Throws the exception "Invalid user" if the user customer does not exist. 



