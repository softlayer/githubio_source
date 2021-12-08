---
title: "hasAttribute"
description: "Determine if an account has an [SoftLayer_Account_Attribute]({{<ref 'reference/datatypes/SoftLayer_Account_Attribute'>}}... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/hasAttribute"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::hasAttribute


Determine if an account has a given attribute.


## Overview 
Determine if an account has an [SoftLayer_Account_Attribute]({{<ref "reference/datatypes/SoftLayer_Account_Attribute">}}) associated with it. hasAttribute() returns false if the attribute does not exist or if it does not have a value. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|attributeType| string| The [[SoftLayer_Account_Attribute_Type]] key name associated with the account attribute you wish to determine exists.|


### Required Headers
* authenticate


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Account::getAttributeByType](/reference/services/SoftLayer_Account/getAttributeByType )
*  [SoftLayer_Account::getAttributes](/reference/services/SoftLayer_Account/getAttributes )




