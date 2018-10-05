---
title: "assignNewParentId"
description: "This method can be used in place of [[SoftLayer_User_Customer::editObject]] to change the parent user of this user. 

Th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/assignNewParentId"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::assignNewParentId

Assign a different parent to this user. 


## Overview 
This method can be used in place of [[SoftLayer_User_Customer::editObject]] to change the parent user of this user. 

The new parent must be a user on the same account, and must not be a child of this user.  A user is not allowed to change their own parent. 

If the cascadeFlag is set to false, then an exception will be thrown if the new parent does not have all of the permissions that this user possesses.  If the cascadeFlag is set to true, then permissions will be removed from this user and the descendants of this user as necessary so that no children of the parent will have permissions that the parent does not possess. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|parentId| integer| the id of the parent to be assigned to the user|
|cascadePermissionsFlag| boolean| |


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers
* SoftLayer_User_Customer_OpenIdConnectObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_User_Customer_OpenIdConnect'>SoftLayer_User_Customer_OpenIdConnect </a>

