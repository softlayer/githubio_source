---
title: "requestPhoneValidation"
description: "Initiates a phone validation requests and returns a unique token. Use [[SoftLayer_User_Customer_External_Binding_Phone::... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Phone"
---
# [SoftLayer_User_Customer_External_Binding_Phone](/reference/services/SoftLayer_User_Customer_External_Binding_Phone)::requestPhoneValidation

Initiates a phone validation requests and returns a unique token


## Overview 
Initiates a phone validation requests and returns a unique token. Use [[SoftLayer_User_Customer_External_Binding_Phone::checkPhoneValidationResult|checkPhoneValidationResult]] to find the phone validation result. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|phoneData| <a href='/reference/datatypes/SoftLayer_Container_User_Data_Phone'>SoftLayer_Container_User_Data_Phone </a>| |


### Required Headers
* authenticate
* SoftLayer_User_Customer_External_Binding_PhoneInitParameters

### Optional Headers

### Return Values
string

