---
title: "unlinkGroup"
description: "Unlinks a SoftLayer_User_Permission_Group object to the role."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Role"
aliases:
    - "/reference/services/softlayer_user_permission_role/unlinkGroup"
---
# [SoftLayer_User_Permission_Role](/reference/services/SoftLayer_User_Permission_Role)::unlinkGroup

Unlinks a permission group to the role.


## Overview 
Unlinks a SoftLayer_User_Permission_Group object to the role. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|group| <a href='/reference/datatypes/SoftLayer_User_Permission_Group'>SoftLayer_User_Permission_Group </a>| Unink role to provided group.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_RoleInitParameters


### Return Values
* void



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "Can't unlink role and group: Permission Denied." if a customer user attempts this request without the proper permission. 

* SoftLayer_Exception_User_Permission_Inaccessible 

> Throws the exception "Invalid group" if the permission group does not exist. 



