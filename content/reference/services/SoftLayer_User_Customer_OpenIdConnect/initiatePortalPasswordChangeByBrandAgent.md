---
title: "initiatePortalPasswordChangeByBrandAgent"
description: "A Brand Agent that has permissions to Add Customer Accounts will be able to request the password email be sent to the Ma... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::initiatePortalPasswordChangeByBrandAgent

Allows a Brand Agent to request password reset email to be sent to


## Overview 
A Brand Agent that has permissions to Add Customer Accounts will be able to request the password email be sent to the Master User of a Customer Account created by the same Brand as the agent making the request. Due to security reasons, the number of reset requests are limited within an undisclosed timeframe. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| The username of the user to receive the password reset email|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_User_Customer::initiatePortalPasswordChange](/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChange )
*  [SoftLayer_User_Customer::getUserIdForPasswordSet](/reference/services/SoftLayer_User_Customer/getUserIdForPasswordSet )
*  [SoftLayer_User_Customer::getRequirementsForPasswordSet](/reference/services/SoftLayer_User_Customer/getRequirementsForPasswordSet )
*  [SoftLayer_User_Customer::processPasswordSetRequest](/reference/services/SoftLayer_User_Customer/processPasswordSetRequest )
*  [SoftLayer_User_Customer::checkPhoneFactorAuthenticationForPasswordSet](/reference/services/SoftLayer_User_Customer/checkPhoneFactorAuthenticationForPasswordSet )

