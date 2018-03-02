---
title: "getAllRecurringTopLevelBillingItemsUnfiltered"
description: "Retrieve the billing items that will be on an account's next invoice. Does not consider associated items."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::getAllRecurringTopLevelBillingItemsUnfiltered
## Overview 
Retrieve the billing items that will be on an account's next invoice. Does not consider associated items.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_AccountObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>

