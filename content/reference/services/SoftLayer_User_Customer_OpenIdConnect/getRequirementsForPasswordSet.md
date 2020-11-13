---
title: "getRequirementsForPasswordSet"
description: "Retrieve the authentication requirements for an outstanding password set/reset request.  The requirements returned in th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/getRequirementsForPasswordSet"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::getRequirementsForPasswordSet

Retrieve the authentication requirements for a user when attempting


## Overview 
Retrieve the authentication requirements for an outstanding password set/reset request.  The requirements returned in the same SoftLayer_Container_User_Customer_PasswordSet container which is provided as a parameter into this request.  The SoftLayer_Container_User_Customer_PasswordSet::authenticationMethods array will contain an entry for each authentication method required for the user.  See SoftLayer_Container_User_Customer_PasswordSet for more details. 

If the user has required authentication methods, then authentication information will be supplied to the SoftLayer_User_Customer::processPasswordSetRequest method within this same SoftLayer_Container_User_Customer_PasswordSet container.  All existing information in the container must continue to exist in the container to complete the password set/reset process. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|passwordSet| <a href='/reference/datatypes/SoftLayer_Container_User_Customer_PasswordSet'>SoftLayer_Container_User_Customer_PasswordSet </a>| Container used to exchange information pertaining to the password reset process.|


### Required Headers
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_User_Customer_PasswordSet'>SoftLayer_Container_User_Customer_PasswordSet </a>


### Associated Methods

*  [SoftLayer_User_Customer::initiatePortalPasswordChange](/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChange )
*  [SoftLayer_User_Customer::getUserIdForPasswordSet](/reference/services/SoftLayer_User_Customer/getUserIdForPasswordSet )
*  [SoftLayer_User_Customer::processPasswordSetRequest](/reference/services/SoftLayer_User_Customer/processPasswordSetRequest )
*  [SoftLayer_User_Customer::checkPhoneFactorAuthenticationForPasswordSet](/reference/services/SoftLayer_User_Customer/checkPhoneFactorAuthenticationForPasswordSet )



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception "Your request cannot be processed" if changes to the account or user has invalidated the password reset request, such as a user's status changes and is no longer Active. 

* SoftLayer_Exception_Public 

> Throws the exception "Invalid password recovery key" if no password recovery key was provided, the provided key was invalid, the key has expired, or the recovery key does not belong to this user. 



