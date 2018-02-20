---
title: "getUserStatus"
description: "Retrieve a portal user's status, which controls overall access to the SoftLayer customer portal and VPN access to the pr... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::getUserStatus
## Overview 
Retrieve a portal user's status, which controls overall access to the SoftLayer customer portal and VPN access to the private network.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_User_Customer_OpenIdConnectInitParameters
* authenticate

### Optional Headers
* SoftLayer_User_Customer_OpenIdConnectObjectMask
* SoftLayer_User_Customer_OpenIdConnectObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_User_Customer_Status'>SoftLayer_User_Customer_Status </a>
