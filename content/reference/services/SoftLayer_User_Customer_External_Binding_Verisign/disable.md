---
title: "disable"
description: "Disabling an external binding will allow you to keep the external binding on your SoftLayer account, but will not requir... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Verisign"
aliases:
    - "/reference/services/softlayer_user_customer_external_binding_verisign/disable"
---
# [SoftLayer_User_Customer_External_Binding_Verisign](/reference/services/SoftLayer_User_Customer_External_Binding_Verisign)::disable

Disable an external binding.


## Overview 
Disabling an external binding will allow you to keep the external binding on your SoftLayer account, but will not require you to authentication with our trusted 2 form factor vendor when logging into the SoftLayer customer portal. 

You may supply one of the following reason when you disable an external binding: 
*Unspecified
*TemporarilyUnavailable
*Lost
*Stolen

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|reason| string| The reason a credential is being disabled.|


### Required Headers
* authenticate
* SoftLayer_User_Customer_External_Binding_VerisignInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the error "The provided disable reason must be one of the following: Unspecified, TemporarilyUnavailable, Lost, or Stolen." when the provided reason does not match an acceptable option. 



