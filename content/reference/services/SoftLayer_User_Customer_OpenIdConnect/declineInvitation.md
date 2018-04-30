---
title: "declineInvitation"
description: "Declines an invitation to link an OpenIdConnect identity to a SoftLayer (Atlas) identity and account. Note that this use... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/declineInvitation"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::declineInvitation

Sets a customer invitation as declined.


## Overview 
Declines an invitation to link an OpenIdConnect identity to a SoftLayer (Atlas) identity and account. Note that this uses a registration code that is likely a one-time-use-only token, so if an invitation has already been processed (accepted or previously declined) it will not be possible to process it a second time. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type. Currently "IBMid" is the only supported provider.|
|registrationCode| string| The registration code or token received from the system where the user identity|


### Required Headers

### Optional Headers

### Return Values
void

