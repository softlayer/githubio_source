---
title: "getPaypalTransactions"
description: "Retrieve all PayPal transactions associated with this order. If this order was not placed with PayPal, this will be empt... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
---
# [SoftLayer_Billing_Order](/reference/services/SoftLayer_Billing_Order)::getPaypalTransactions

Retrieve all PayPal transactions associated with this order. If this order was not placed with PayPal, this will be empty.


## Overview 
Retrieve all PayPal transactions associated with this order. If this order was not placed with PayPal, this will be empty.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_OrderInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_OrderObjectMask
* SoftLayer_Billing_OrderObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Payment_PayPal_Transaction'>SoftLayer_Billing_Payment_PayPal_Transaction[] </a>

