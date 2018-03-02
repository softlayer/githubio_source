---
title: "getVirtualGuests"
description: "Retrieve a portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::getVirtualGuests
## Overview 
Retrieve a portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_User_CustomerInitParameters
* authenticate

### Optional Headers
* SoftLayer_User_CustomerObjectMask
* SoftLayer_User_CustomerObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>

