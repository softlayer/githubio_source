---
title: "isMasterUser"
description: "Portal users are considered master users if they don't have an associated parent user. The only users who don't have par... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/isMasterUser"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::isMasterUser

<div class="deprecated"><span class="deprecation-label">Deprecated </span></div>

Determine if a portal user is a master user.


## Overview 
Portal users are considered master users if they don't have an associated parent user. The only users who don't have parent users are users whose username matches their SoftLayer account name. Master users have special permissions throughout the SoftLayer customer portal. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Return Values
* boolean




