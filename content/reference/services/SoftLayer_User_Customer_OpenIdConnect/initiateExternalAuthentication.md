---
title: "initiateExternalAuthentication"
description: "The service initiates an external authentication with the given external authentication vendor. The authentication conta... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/initiateExternalAuthentication"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::initiateExternalAuthentication

Initiates an external authentication using the given authentication container.


## Overview 
The service initiates an external authentication with the given external authentication vendor. The authentication container and its content will be verified before an attempt is made to initiate an external authentication. [SoftLayer_Container_User_Customer_External_Binding_Phone]({{<ref "reference/datatypes/SoftLayer_Container_User_Customer_External_Binding_Phone">}}) container can be used for this service. 

This service returns a unique authentication request token. You can use [SoftLayer_User_Customer::checkExternalAuthenticationStatus]({{<ref "reference/services/SoftLayer_User_Customer/checkExternalAuthenticationStatus">}}) service to check if the authentication request is complete or not. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|authenticationContainer| <a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding'>SoftLayer_Container_User_Customer_External_Binding </a>| The authentication container with the external authentication information.|


### Required Headers
* authenticate


### Return Values
* string



### Error Handling

* SoftLayer_Exception_Public 

> Throw the error "Invalid external authentication container is provided." when you have provide an invalid authentication container. 

* SoftLayer_Exception_Public 

> Throw the error "Invalid login credentials provided." when you have provide incorrect authentication information. 



