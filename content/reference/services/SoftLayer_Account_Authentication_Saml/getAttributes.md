---
title: "getAttributes"
description: "Retrieve the saml attribute values for a SoftLayer customer account."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Authentication_Saml"
---
# SoftLayer_Account_Authentication_Saml::getAttributes
## Overview 
Retrieve the saml attribute values for a SoftLayer customer account.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Account_Authentication_SamlInitParameters
* authenticate

### Optional Headers
* SoftLayer_Account_Authentication_SamlObjectMask
* SoftLayer_Account_Authentication_SamlObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Account_Authentication_Attribute'>SoftLayer_Account_Authentication_Attribute[] </a>
