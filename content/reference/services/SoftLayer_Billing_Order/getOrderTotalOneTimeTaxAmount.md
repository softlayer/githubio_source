---
title: "getOrderTotalOneTimeTaxAmount"
description: "Retrieve an order's total one time tax amount. This amount represents the tax that will be applied to the total charge,... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
aliases:
    - "/reference/services/softlayer_billing_order/getOrderTotalOneTimeTaxAmount"
---
# [SoftLayer_Billing_Order](/reference/services/SoftLayer_Billing_Order)::getOrderTotalOneTimeTaxAmount

Retrieve an order's total one time tax amount. This amount represents the tax that will be applied to the total charge, if the SoftLayer_Account tied to a SoftLayer_Billing_Order is a taxable account.


## Overview 
Retrieve an order's total one time tax amount. This amount represents the tax that will be applied to the total charge, if the SoftLayer_Account tied to a SoftLayer_Billing_Order is a taxable account.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_OrderInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_OrderObjectMask
* SoftLayer_Billing_OrderObjectFilter
* SoftLayer_ObjectMask

### Return Values
decimal

