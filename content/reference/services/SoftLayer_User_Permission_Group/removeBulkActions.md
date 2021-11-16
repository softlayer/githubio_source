---
title: "removeBulkActions"
description: "Unassigns multiple SoftLayer_User_Permission_Action objects from the group."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Permission_Group"
aliases:
    - "/reference/services/softlayer_user_permission_group/removeBulkActions"
---
# [SoftLayer_User_Permission_Group](/reference/services/SoftLayer_User_Permission_Group)::removeBulkActions


Remove a list of permission actions from the group.


## Overview 
Unassigns multiple SoftLayer_User_Permission_Action objects from the group. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|actions| <a href='/reference/datatypes/SoftLayer_User_Permission_Action'>SoftLayer_User_Permission_Action[] </a>| Permission Actions to be removed.|


### Required Headers
* authenticate
* SoftLayer_User_Permission_GroupInitParameters


### Return Values
* void



### Error Handling

* SoftLayer_Exception_PermissionDenied 

> Throws the exception "You cannot remove action to group: Permission Denied." if a customer user attempts this request without the proper permission. 

* SoftLayer_Exception_User_Permission_Inaccessible 

> Throws the exception "Can't access action" if the permission action does not exist. 



