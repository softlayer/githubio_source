---
title: "editObject"
description: "Edit the properties of an address record by passing in a modified instance of a SoftLayer_Account_Address object. Users... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Address"
aliases:
    - "/reference/services/softlayer_account_address/editObject"
---
# [SoftLayer_Account_Address](/reference/services/SoftLayer_Account_Address)::editObject


Edit an address record.


## Overview 
Edit the properties of an address record by passing in a modified instance of a SoftLayer_Account_Address object. Users will be restricted to modifying addresses for their account. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a>| A skeleton SoftLayer_Account_Address object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Account_AddressInitParameters


### Return Values
* boolean




