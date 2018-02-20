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
---
# SoftLayer_User_Customer_OpenIdConnect::initiateExternalAuthentication
## Overview 
The service initiates an external authentication with the given external authentication vendor. The authentication container and its content will be verified before an attempt is made to initiate an external authentication. [[SoftLayer_Container_User_Customer_External_Binding_Phone|Phone external binding]] container can be used for this service. 

This service returns a unique authentication request token. You can use [[SoftLayer_User_Customer::checkExternalAuthenticationStatus|checkExternalAuthenticationStatus]] service to check if the authentication request is complete or not. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|authenticationContainer| <a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding'>SoftLayer_Container_User_Customer_External_Binding </a>| The authentication container with the external authentication information.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
string
