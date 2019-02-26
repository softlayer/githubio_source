---
title: "performExternalAuthentication"
description: "The perform external authentication method will authenticate the given external authentication container with an externa... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/performExternalAuthentication"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::performExternalAuthentication

Perform an external authentication using the given authentication container. 


## Overview 
The perform external authentication method will authenticate the given external authentication container with an external vendor.  The authentication container and its contents will be verified before an attempt is made to authenticate the contents of the container with an external vendor. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|authenticationContainer| <a href='/reference/datatypes/SoftLayer_Container_User_Customer_External_Binding'>SoftLayer_Container_User_Customer_External_Binding </a>| |


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_User_Customer_Portal_Token'>SoftLayer_Container_User_Customer_Portal_Token </a>



### Error Handling

* SoftLayer_Exception_User_Customer_External_Binding_Verisign_SecondSecurityCodeRequired 

> Throw the error "Your credential has become out of synchronization.  Please supply a second security code." if the given credential is out of synchronization. 

* SoftLayer_Exception_Public 

> Throw the error "Invalid login credentials provided." when you have provide incorrect authentication information. 



