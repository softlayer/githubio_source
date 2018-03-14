---
title: "getCreditCardTransactions"
description: "Retrieve all credit card transactions associated with this order. If this order was not placed with a credit card, this... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
aliases:
    - "/reference/services/softlayer_billing_order/getCreditCardTransactions"
---
# [SoftLayer_Billing_Order](/reference/services/SoftLayer_Billing_Order)::getCreditCardTransactions

Retrieve all credit card transactions associated with this order. If this order was not placed with a credit card, this will be empty.


## Overview 
Retrieve all credit card transactions associated with this order. If this order was not placed with a credit card, this will be empty.

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
<a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction'>SoftLayer_Billing_Payment_Card_Transaction[] </a>

