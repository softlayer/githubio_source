---
title: "getInvoiceTotalOneTimeAmount"
description: "Retrieve the total one-time charges for this invoice. This is the sum of one-time charges + setup fees + labor fees. Thi... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice"
---
# SoftLayer_Billing_Invoice::getInvoiceTotalOneTimeAmount
## Overview 
Retrieve the total one-time charges for this invoice. This is the sum of one-time charges + setup fees + labor fees. This does not include taxes.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_InvoiceInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_InvoiceObjectMask
* SoftLayer_Billing_InvoiceObjectFilter
* SoftLayer_ObjectMask

### Return Values
decimal

