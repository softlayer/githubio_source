---
title: "getOrderTotalOneTime"
description: "Retrieve an order's total one time amount summing all the set up fees, the labor fees and the one time fees. Taxes will... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
---
# [SoftLayer_Billing_Order](/reference/services/SoftLayer_Billing_Order)::getOrderTotalOneTime

Retrieve an order's total one time amount summing all the set up fees, the labor fees and the one time fees. Taxes will be applied for non-tax-exempt. This amount represents the initial fees that will be charged.


## Overview 
Retrieve an order's total one time amount summing all the set up fees, the labor fees and the one time fees. Taxes will be applied for non-tax-exempt. This amount represents the initial fees that will be charged.

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

