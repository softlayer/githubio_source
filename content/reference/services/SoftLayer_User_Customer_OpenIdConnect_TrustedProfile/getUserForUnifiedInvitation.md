---
title: "getUserForUnifiedInvitation"
description: "Returns an IMS User Object from the provided OpenIdConnect User ID or IBMid Unique Identifier for the Account of the act... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/getUserForUnifiedInvitation"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::getUserForUnifiedInvitation


Get the IMS User Object for the provided OpenIdConnect User ID, or (Optional) IBMid Unique Identifier. 


## Overview 
Returns an IMS User Object from the provided OpenIdConnect User ID or IBMid Unique Identifier for the Account of the active user. Enforces the User Management permissions for the Active User. An exception will be thrown if no matching IMS User is found. NOTE that providing IBMid Unique Identifier is optional, but it will be preferred over OpenIdConnect User ID if provided. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|openIdConnectUserId| string| The OpenId Connect user id to use for the IMS User lookup|
|uniqueIdentifier| string| The Optional unique identifier (in IAMid format) to use for the IMS user lookup, when provided as a second parameter.|
|searchInvitationsNotLinksFlag| string| Optional|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile'>SoftLayer_User_Customer_OpenIdConnect_TrustedProfile </a>




