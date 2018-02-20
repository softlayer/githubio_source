---
title: "createCustomerAccount"
description: "Create a new customer account record."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand"
---
# SoftLayer_Brand::createCustomerAccount
## Overview 
Create a new customer account record. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|account| <a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>| The template of the account object to be created.|
|bypassDuplicateAccountCheck| boolean| Bypass validation for duplicate account(s).|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_BrandObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>
