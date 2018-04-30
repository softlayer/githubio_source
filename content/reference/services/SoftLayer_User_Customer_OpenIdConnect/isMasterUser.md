---
title: "isMasterUser"
description: "Portal users are considered master users if they don't have an associated parent user. The only users who don't have par... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/isMasterUser"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::isMasterUser

Determine if a portal user is a master user.


## Overview 
Portal users are considered master users if they don't have an associated parent user. The only users who don't have parent users are users whose username matches their SoftLayer account name. Master users have special permissions throughout the SoftLayer customer portal. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers

### Return Values
boolean

