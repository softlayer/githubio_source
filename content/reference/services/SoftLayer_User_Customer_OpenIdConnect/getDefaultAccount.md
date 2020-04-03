---
title: "getDefaultAccount"
description: "This API gets the account associated with the default user for the OpenIdConnect identity that is linked to the current... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/getDefaultAccount"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::getDefaultAccount

Retrieve the default account for the OpenIdConnect identity that is linked to the current active SoftLayer user identity. 


## Overview 
This API gets the account associated with the default user for the OpenIdConnect identity that is linked to the current active SoftLayer user identity. When a single active user is found for that IAMid, it becomes the default user and the associated account is returned. When multiple default users are found only the first is preserved and the associated account is returned (remaining defaults see their default flag unset). If the current SoftLayer user identity isn't linked to any OpenIdConnect identity, or if none of the linked users were found as defaults, the API returns null. Invoke this only on IAMid-authenticated users. 

-----

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
* <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>




