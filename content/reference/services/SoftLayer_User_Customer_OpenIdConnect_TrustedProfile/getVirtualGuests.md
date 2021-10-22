---
title: "getVirtualGuests"
description: "Retrieve a portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/getVirtualGuests"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::getVirtualGuests

Retrieve a portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal.


## Overview 
Retrieve a portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal.

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
* <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>




