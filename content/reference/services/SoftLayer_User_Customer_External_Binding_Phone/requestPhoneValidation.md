---
title: "requestPhoneValidation"
description: "Initiates a phone validation requests and returns a unique token. Use [SoftLayer_User_Customer_External_Binding_Phone::c... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Phone"
aliases:
    - "/reference/services/softlayer_user_customer_external_binding_phone/requestPhoneValidation"
---
# [SoftLayer_User_Customer_External_Binding_Phone](/reference/services/SoftLayer_User_Customer_External_Binding_Phone)::requestPhoneValidation

Initiates a phone validation requests and returns a unique token


## Overview 
Initiates a phone validation requests and returns a unique token. Use [SoftLayer_User_Customer_External_Binding_Phone::checkPhoneValidationResult]({{<ref "reference/services/SoftLayer_User_Customer_External_Binding_Phone/checkPhoneValidationResult">}}) to find the phone validation result. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|phoneData| <a href='/reference/datatypes/SoftLayer_Container_User_Data_Phone'>SoftLayer_Container_User_Data_Phone </a>| |


### Required Headers
* authenticate
* SoftLayer_User_Customer_External_Binding_PhoneInitParameters


### Return Values
* string



### Error Handling

* SoftLayer_Exception 

> Throw the error "You have exceeded the maximum phone validation requests. Please try again later." when you submitted too many phone validation requests. 



