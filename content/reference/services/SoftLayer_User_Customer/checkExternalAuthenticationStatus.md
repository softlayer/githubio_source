---
title: "checkExternalAuthenticationStatus"
description: "This service checks the result of a previously requested external authentication. [SoftLayer_Container_User_Customer_Ext... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
aliases:
    - "/reference/services/softlayer_user_customer/checkExternalAuthenticationStatus"
---
# [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer)::checkExternalAuthenticationStatus


Checks if an external authentication is complete or not


## Overview 
This service checks the result of a previously requested external authentication. [SoftLayer_Container_User_Customer_External_Binding_Phone]({{<ref "reference/datatypes/SoftLayer_Container_User_Customer_External_Binding_Phone">}}) service. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|authenticationContainer| <a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding'>SoftLayer_Container_User_Customer_External_Binding </a>| The authentication container with the external authentication information.|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_User_Customer_Portal_Token'>SoftLayer_Container_User_Customer_Portal_Token </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw the error "Invalid external authentication container is provided." when you have provide an invalid authentication container. 

* SoftLayer_Exception_User_Customer_External_Binding_InvalidAuthenticationToken 

> Throw the error "Failed to find an valid authentication request." when you have provide incorrect authentication request token or your request is expired. 

* SoftLayer_Exception_User_Customer_External_Binding_AuthenticationFailed 

> Throw the error "External authentication failed." when the external authentication failed. 

* SoftLayer_Exception_User_Customer_External_Binding_AwaitingResponse 

> Throw the error "Waiting on the external authentication response." when pending result from the external authentication. 



