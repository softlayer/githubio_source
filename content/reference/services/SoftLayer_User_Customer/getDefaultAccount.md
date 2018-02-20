---
title: "getDefaultAccount"
description: "This API gets the default account for the OpenIdConnect identity that is linked to the current SoftLayer user identity.... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::getDefaultAccount
## Overview 
This API gets the default account for the OpenIdConnect identity that is linked to the current SoftLayer user identity. If there is no default present, the API returns null, except in the special case where we find one active user linked to the IBMid. In that case, we will set the link from the IBMid to that user as default, and return the account of which that user is a member. Invoke this only on IBMid-authenticated users. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type.|


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers
* SoftLayer_User_CustomerObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>
