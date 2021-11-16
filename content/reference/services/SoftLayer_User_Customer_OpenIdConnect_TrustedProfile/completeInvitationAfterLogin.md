---
title: "completeInvitationAfterLogin"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/completeInvitationAfterLogin"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::completeInvitationAfterLogin


Completes invitation processing after logging on an existing OpenIdConnect user identity and return an access token


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type. Currently "IBMid" is the only supported provider.|
|accessToken| string| The access token from an OpenIdConnect login|
|emailRegistrationCode| string| The registration code from OpenIdConnect process|


### Required Headers


### Return Values
* void



### Error Handling

* SoftLayer_Exception_NotFound 

> Throw the exception "BlueID email code not found in state parameter." if no BlueID email code is provided. 

* SoftLayer_Exception_NotFound 

> Throw the exception "No invitation record for BlueID email code found." if no invitation record is found. 



