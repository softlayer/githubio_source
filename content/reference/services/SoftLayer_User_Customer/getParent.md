---
title: "getParent"
description: "Retrieve a portal user's parent user. If a SoftLayer_User_Customer has a null parentId property then it doesn't have a p... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::getParent
## Overview 
Retrieve a portal user's parent user. If a SoftLayer_User_Customer has a null parentId property then it doesn't have a parent user.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_User_CustomerInitParameters
* authenticate

### Optional Headers
* SoftLayer_User_CustomerObjectMask
* SoftLayer_User_CustomerObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>
