---
title: "getHardwareGenericComponent"
description: "Retrieve the component type tied to an order item. All hardware-specific items should have a generic hardware component."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Item"
---
# SoftLayer_Billing_Order_Item::getHardwareGenericComponent
## Overview 
Retrieve the component type tied to an order item. All hardware-specific items should have a generic hardware component.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Billing_Order_ItemInitParameters
* authenticate

### Optional Headers
* SoftLayer_Billing_Order_ItemObjectMask
* SoftLayer_Billing_Order_ItemObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic </a>
