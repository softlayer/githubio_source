---
title: "completeInvitationAfterLogin"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# SoftLayer_User_Customer_OpenIdConnect::completeInvitationAfterLogin
## Overview 


### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type. Currently "IBMid" is the only supported provider.|
|accessToken| string| The access token from an OpenIdConnect login|
|emailRegistrationCode| string| The registration code from OpenIdConnect process|


### Required Headers

### Optional Headers

### Return Values
void
