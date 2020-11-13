---
title: "checkPhoneFactorAuthenticationForPasswordSet"
description: "Add a description here"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/checkPhoneFactorAuthenticationForPasswordSet"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::checkPhoneFactorAuthenticationForPasswordSet

Check the status of an outstanding Phone Factor Authentication for Password Set


## Overview 
Add a description here 



-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|passwordSet| <a href='/reference/datatypes/SoftLayer_Container_User_Customer_PasswordSet'>SoftLayer_Container_User_Customer_PasswordSet </a>| A container with the information required for setting customer password|
|authenticationContainer| <a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding'>SoftLayer_Container_User_Customer_External_Binding </a>| The authentication container with the external authentication information.|


### Required Headers
* SoftLayer_User_CustomerInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::initiatePortalPasswordChange](/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChange )
*  [SoftLayer_User_Customer::getUserIdForPasswordSet](/reference/services/SoftLayer_User_Customer/getUserIdForPasswordSet )
*  [SoftLayer_User_Customer::getRequirementsForPasswordSet](/reference/services/SoftLayer_User_Customer/getRequirementsForPasswordSet )
*  [SoftLayer_User_Customer::processPasswordSetRequest](/reference/services/SoftLayer_User_Customer/processPasswordSetRequest )



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception "Invalid password recovery key" if no password recovery key was provided, the provided key was invalid, the key has expired, or the recovery key does not belong to this user. 

* SoftLayer_Exception_Public 

> Throws the exception "Your portal password must" followed by a list of violated password rules if the given password fails to match any of the above restrictions. 

* SoftLayer_Exception_User_Customer_External_Binding_AwaitingResponse 

> Throws the exception "Waiting on the external authentication response" if phone-based authentication was requested. 

* SoftLayer_Exception_User_Customer_External_Binding_AuthenticationFailed 

> Throws the exception "External authentication failed" if phone-based authentication failed. 



