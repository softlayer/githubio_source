---
title: "getAttributeByType"
description: "Retrieve a single [[SoftLayer_Account_Attribute]] record by its [[SoftLayer_Account_Attribute_Type|types's]] key name."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getAttributeByType

Retrieve an account attribute by type key name.


## Overview 
Retrieve a single [[SoftLayer_Account_Attribute]] record by its [[SoftLayer_Account_Attribute_Type|types's]] key name. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|attributeType| string| The [[SoftLayer_Account_Attribute_Type]] key name associated with the account attribute you wish to retrieve.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Account_Attribute'>SoftLayer_Account_Attribute </a>


### associatedMethods

*  [SoftLayer_Account::hasAttribute](/reference/services/SoftLayer_Account/hasAttribute )
*  [SoftLayer_Account::getAttributes](/reference/services/SoftLayer_Account/getAttributes )

