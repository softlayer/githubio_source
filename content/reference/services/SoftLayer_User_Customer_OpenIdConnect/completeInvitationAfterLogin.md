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
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/completeInvitationAfterLogin"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::completeInvitationAfterLogin

Completes invitation processing after logging on an existing OpenIdConnect user identity and return an access token


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

