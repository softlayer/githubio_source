---
title: "getMappedAccounts"
description: "An OpenIdConnect identity, for example an IAMid, can be linked or mapped to one or more individual SoftLayer users, but... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/getMappedAccounts"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::getMappedAccounts

Retrieve a list of all active accounts that belong to this customer.


## Overview 
An OpenIdConnect identity, for example an IAMid, can be linked or mapped to one or more individual SoftLayer users, but no more than one SoftLayer user per account. This effectively links the OpenIdConnect identity to those accounts. This API returns a list of all active accounts for which there is a link between the OpenIdConnect identity and a SoftLayer user. Invoke this only on IAMid-authenticated users. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| A value representing the OpenID Connect provider type. Currently "IBMid" is the|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Optional Headers
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account[] </a>




