---
title: "createOpenIdConnectUserAndCompleteInvitation"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/createOpenIdConnectUserAndCompleteInvitation"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::createOpenIdConnectUserAndCompleteInvitation

Completes invitation processing when a new OpenIdConnect user must be created.


## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type. Currently "IBMid" is the only supported provider.|
|user| <a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>| user|
|password| string| The password user inputted for their account|
|registrationCode| string| The registration code or token received from the system where the user identity|


### Required Headers


### Return Values
* void



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Error completing registration." if there was an error completing registration. 



