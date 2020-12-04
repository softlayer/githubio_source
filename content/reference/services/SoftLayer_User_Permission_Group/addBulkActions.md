---
title: "addBulkActions"
description: "Assigns multiple SoftLayer_User_Permission_Action objects to the group."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
aliases:
    - "/reference/services/softlayer_user_permission_group/addBulkActions"
---
# [SoftLayer_User_Permission_Group](/reference/services/SoftLayer_User_Permission_Group)::addBulkActions

Adds a list of permission actions to the group.


## Overview 
Assigns multiple SoftLayer_User_Permission_Action objects to the group. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|actions| <a href='/reference/datatypes/SoftLayer_User_Permission_Action'>SoftLayer_User_Permission_Action[] </a>| Permission Actions to be added.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_GroupInitParameters


### Return Values
* void



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot add action to group: Permission Denied." if a customer user attempts this request without the proper permission. 

* SoftLayer_Exception_User_Permission_Inaccessible 

> Throws the exception "Can't access action" if the permission action does not exist. 



