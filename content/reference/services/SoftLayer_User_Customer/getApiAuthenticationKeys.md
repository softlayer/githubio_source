---
title: "getApiAuthenticationKeys"
description: "Retrieve a portal user's API Authentication keys. There is a max limit of two API keys per user."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::getApiAuthenticationKeys
## Overview 
Retrieve a portal user's API Authentication keys. There is a max limit of two API keys per user.

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
<a href='/reference/datatypes/SoftLayer_User_Customer_ApiAuthentication'>SoftLayer_User_Customer_ApiAuthentication[] </a>

