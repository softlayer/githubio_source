---
title: "checkPhoneFactorAuthenticationForPasswordSet"
description: "Add a description here"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/checkPhoneFactorAuthenticationForPasswordSet"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::checkPhoneFactorAuthenticationForPasswordSet

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
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_User_Customer::initiatePortalPasswordChange](/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChange )
*  [SoftLayer_User_Customer::getUserIdForPasswordSet](/reference/services/SoftLayer_User_Customer/getUserIdForPasswordSet )
*  [SoftLayer_User_Customer::getRequirementsForPasswordSet](/reference/services/SoftLayer_User_Customer/getRequirementsForPasswordSet )
*  [SoftLayer_User_Customer::processPasswordSetRequest](/reference/services/SoftLayer_User_Customer/processPasswordSetRequest )



### Error Handling

* SoftLayer_Exception_Public 

> <<< EOT 

* SoftLayer_Exception_Public 

> <<< EOT 

* SoftLayer_Exception_User_Customer_External_Binding_AwaitingResponse 

> <<< EOT 

* SoftLayer_Exception_User_Customer_External_Binding_AuthenticationFailed 

> <<< EOT 



