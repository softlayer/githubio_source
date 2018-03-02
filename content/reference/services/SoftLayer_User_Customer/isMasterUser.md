---
title: "isMasterUser"
description: "Portal users are considered master users if they don't have an associated parent user. The only users who don't have par... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer::isMasterUser
## Overview 
Portal users are considered master users if they don't have an associated parent user. The only users who don't have parent users are users whose username matches their SoftLayer account name. Master users have special permissions throughout the SoftLayer customer portal. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_User_CustomerInitParameters

### Optional Headers

### Return Values
boolean

