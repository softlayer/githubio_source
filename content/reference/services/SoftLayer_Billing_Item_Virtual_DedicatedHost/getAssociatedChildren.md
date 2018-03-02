---
title: "getAssociatedChildren"
description: "Retrieve a Billing Item's associated child billing items. This includes 'floating' items that are not necessarily child... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Virtual_DedicatedHost"
---
# SoftLayer_Billing_Item_Virtual_DedicatedHost::getAssociatedChildren
## Overview 
Retrieve a Billing Item's associated child billing items. This includes "floating" items that are not necessarily child billing items of this billing item.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_Item_Virtual_DedicatedHostInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_Item_Virtual_DedicatedHostObjectMask
* SoftLayer_Billing_Item_Virtual_DedicatedHostObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>

