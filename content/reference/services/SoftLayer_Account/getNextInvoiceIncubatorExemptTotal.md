---
title: "getNextInvoiceIncubatorExemptTotal"
description: "Retrieve the pre-tax total amount exempt from incubator credit for the account's next invoice. This field is now depreca... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::getNextInvoiceIncubatorExemptTotal
## Overview 
Retrieve the pre-tax total amount exempt from incubator credit for the account's next invoice. This field is now deprecated and will soon be removed. Please update all references to instead use nextInvoiceTotalAmount

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_AccountObjectMask
* SoftLayer_AccountObjectFilter
* SoftLayer_ObjectMask

### Return Values
decimal

