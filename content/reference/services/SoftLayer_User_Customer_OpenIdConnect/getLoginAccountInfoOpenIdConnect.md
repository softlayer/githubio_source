---
title: "getLoginAccountInfoOpenIdConnect"
description: "Validates a supplied OpenIdConnect access token to the SoftLayer customer portal and returns the default account name an... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::getLoginAccountInfoOpenIdConnect
## Overview 
Validates a supplied OpenIdConnect access token to the SoftLayer customer portal and returns the default account name and id for the active user. An exception will be thrown if no matching customer is found. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type. Currently "IBMid" is the only supported provider.|
|accessToken| string| The OpenID Connect access token which provides temporary access to a resource by the|


### Required Headers

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_User_Customer_OpenIdConnect_LoginAccountInfo'>SoftLayer_Container_User_Customer_OpenIdConnect_LoginAccountInfo </a>
