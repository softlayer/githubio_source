---
title: "linkGroup"
description: "Links a SoftLayer_User_Permission_Group object to the role."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Role"
aliases:
    - "/reference/services/softlayer_user_permission_role/linkGroup"
---
# [SoftLayer_User_Permission_Role](/reference/services/SoftLayer_User_Permission_Role)::linkGroup

Links a permission group to the role.


## Overview 
Links a SoftLayer_User_Permission_Group object to the role. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|group| <a href='/reference/datatypes/SoftLayer_User_Permission_Group'>SoftLayer_User_Permission_Group </a>| Link role to provided group.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_RoleInitParameters


### Return Values
* void



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "Can't link role and group: Permission Denied." if a customer user attempts this request without the proper permission. 

* SoftLayer_Exception_User_Permission_Inaccessible 

> Throws the exception "Invalid group" if the permission group does not exist. 



