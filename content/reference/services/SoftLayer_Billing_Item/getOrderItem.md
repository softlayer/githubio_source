---
title: "getOrderItem"
description: "Retrieve a billing item's original order item. Simply a reference to the original order from which this billing item was... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
---
# SoftLayer_Billing_Item::getOrderItem
## Overview 
Retrieve a billing item's original order item. Simply a reference to the original order from which this billing item was created.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_ItemInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_ItemObjectMask
* SoftLayer_Billing_ItemObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item </a>
