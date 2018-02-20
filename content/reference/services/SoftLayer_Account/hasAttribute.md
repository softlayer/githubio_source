---
title: "hasAttribute"
description: "Determine if an account has an [[SoftLayer_Account_Attribute|attribute]] associated with it. hasAttribute() returns fals... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::hasAttribute
## Overview 
Determine if an account has an [[SoftLayer_Account_Attribute|attribute]] associated with it. hasAttribute() returns false if the attribute does not exist or if it does not have a value. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|attributeType| string| The [[SoftLayer_Account_Attribute_Type]] key name associated with the account attribute you wish to determine exists.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean
