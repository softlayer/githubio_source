---
title: "getSecurityAnswers"
description: "Retrieve a portal user's security question answers. Some portal users may not have security answers or may not be config... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/getSecurityAnswers"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::getSecurityAnswers

Retrieve a portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login.


## Overview 
Retrieve a portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_User_Customer_OpenIdConnectInitParameters
* authenticate

### Optional Headers
* SoftLayer_User_Customer_OpenIdConnectObjectMask
* SoftLayer_User_Customer_OpenIdConnectObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_User_Customer_Security_Answer'>SoftLayer_User_Customer_Security_Answer[] </a>

