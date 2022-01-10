---
title: "getSecurityAnswers"
description: "Retrieve a portal user's security question answers. Some portal users may not have security answers or may not be config... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/getSecurityAnswers"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::getSecurityAnswers


Retrieve a portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login.


## Overview 
Retrieve a portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters
* authenticate


### Optional Headers
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileObjectMask
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Customer_Security_Answer'>SoftLayer_User_Customer_Security_Answer[] </a>




