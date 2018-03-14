---
title: "getActiveAssociatedChildren"
description: "Retrieve a billing item's active associated child billing items. This includes 'floating' items that are not necessarily... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item"
aliases:
    - "/reference/services/softlayer_billing_item/getActiveAssociatedChildren"
---
# [SoftLayer_Billing_Item](/reference/services/SoftLayer_Billing_Item)::getActiveAssociatedChildren

Retrieve a billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item.


## Overview 
Retrieve a billing item's active associated child billing items. This includes "floating" items that are not necessarily child items of this billing item.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_ItemInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_ItemObjectMask
* SoftLayer_Billing_ItemObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>

