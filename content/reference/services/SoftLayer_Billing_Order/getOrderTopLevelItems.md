---
title: "getOrderTopLevelItems"
description: "Retrieve an order's top level items. This normally includes the server line item and any non-server additional services... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
---
# [SoftLayer_Billing_Order](/reference/services/SoftLayer_Billing_Order)::getOrderTopLevelItems

Retrieve an order's top level items. This normally includes the server line item and any non-server additional services such as NAS or ISCSI.


## Overview 
Retrieve an order's top level items. This normally includes the server line item and any non-server additional services such as NAS or ISCSI.

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
<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item[] </a>

