---
title: "getMappedAccounts"
description: "An OpenIdConnect identity, for example an IBMid, can be linked or mapped to one or more individual SoftLayer users, but... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::getMappedAccounts
## Overview 
An OpenIdConnect identity, for example an IBMid, can be linked or mapped to one or more individual SoftLayer users, but no more than one SoftLayer user per account. This effectively links the OpenIdConnect identity to those accounts. This API returns a list of all the accounts for which there is a link between the OpenIdConnect identity and a SoftLayer user. Invoke this only on IBMid-authenticated users. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type. Currently "IBMid" is the only supported provider.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers
* SoftLayer_User_Customer_OpenIdConnectObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account[] </a>

