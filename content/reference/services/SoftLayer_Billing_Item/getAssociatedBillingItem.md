---
title: "getAssociatedBillingItem"
description: "Retrieve a billing item's associated parent. This is to be used for billing items that are 'floating', and therefore are... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
aliases:
    - "/reference/services/softlayer_billing_item/getAssociatedBillingItem"
---
# [SoftLayer_Billing_Item](/reference/services/SoftLayer_Billing_Item)::getAssociatedBillingItem

Retrieve a billing item's associated parent. This is to be used for billing items that are "floating", and therefore are not child items of any parent billing item. If it is desired to associate an item to another, populate this with the SoftLayer_Billing_Item ID of that associated parent item.


## Overview 
Retrieve a billing item's associated parent. This is to be used for billing items that are "floating", and therefore are not child items of any parent billing item. If it is desired to associate an item to another, populate this with the SoftLayer_Billing_Item ID of that associated parent item.

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
<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>

