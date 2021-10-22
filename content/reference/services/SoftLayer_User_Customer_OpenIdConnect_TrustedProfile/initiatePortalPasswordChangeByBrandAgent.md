---
title: "initiatePortalPasswordChangeByBrandAgent"
description: "A Brand Agent that has permissions to Add Customer Accounts will be able to request the password email be sent to the Ma... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/initiatePortalPasswordChangeByBrandAgent"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::initiatePortalPasswordChangeByBrandAgent

Allows a Brand Agent to request password reset email to be sent to


## Overview 
A Brand Agent that has permissions to Add Customer Accounts will be able to request the password email be sent to the Master User of a Customer Account created by the same Brand as the agent making the request. Due to security reasons, the number of reset requests are limited within an undisclosed timeframe. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| The username of the user to receive the password reset email|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::initiatePortalPasswordChange](/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChange )
*  [SoftLayer_User_Customer::getUserIdForPasswordSet](/reference/services/SoftLayer_User_Customer/getUserIdForPasswordSet )
*  [SoftLayer_User_Customer::getRequirementsForPasswordSet](/reference/services/SoftLayer_User_Customer/getRequirementsForPasswordSet )
*  [SoftLayer_User_Customer::processPasswordSetRequest](/reference/services/SoftLayer_User_Customer/processPasswordSetRequest )
*  [SoftLayer_User_Customer::checkPhoneFactorAuthenticationForPasswordSet](/reference/services/SoftLayer_User_Customer/checkPhoneFactorAuthenticationForPasswordSet )



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception "Access is denied" if user does not have access to perform this action. 

* SoftLayer_Exception_Public 

> Throws the exception "Your account is not a Brand Master Account" if user is not a user of a brand master account. 

* SoftLayer_Exception_Public 

> Throws the exception "You do not have permission to request password reset for another user" if user does not have the permission to request password reset for another user. 

* SoftLayer_Exception_Public 

> Throws the exception "You do not have permission to request password reset for this user" if user is attempting to request password reset on a user that is not a master user and/or user on an account that is not owned by this brand. 

* SoftLayer_Exception_InvalidValue 

> Throws the exception "Invalid value provided for Username" if no username is provided. 

* SoftLayer_Exception_Public 

> Throws the exception "Username does not exist" if provided username does not exist. 

* SoftLayer_Exception_Public 

> Throws the exception "This user is authenticated by OpenIdConnect and must use the OpenIdConnect provider to change their password" if the user of the username provided is authenticated by OpenIdConnect. 

* SoftLayer_Exception_Public 

> Throws the exception "This user is authenticated by SAML Federation and must use the SAML Federation provider to change their password" if the user of the username provided is authenticated by SAML. 

* SoftLayer_Exception_Public 

> Throws the exception "You must have security questions set on your account before changing your password"s if a master user who has successfully logged into the portal is attempting to initiate a password reset and security questions are not defined. 

* SoftLayer_Exception_Public 

> Throws the exception "Your request cannot be processed. Please contact support" if the username does not belong to an active user. 

* SoftLayer_Exception_Public 

> Throws the exception "SoftLayer_Exception_User_Customer_UnauthorizedBrand" if the user does not have access to the portal. 



