---
title: "getOrders"
description: "Retrieve the orders ([[SoftLayer_Billing_Order]]) associated with this presale event that were created for the customer'... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Sales"
classes:
    - "SoftLayer_Sales_Presale_Event"
---
# SoftLayer_Sales_Presale_Event::getOrders
## Overview 
Retrieve the orders ([[SoftLayer_Billing_Order]]) associated with this presale event that were created for the customer's account.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Sales_Presale_EventInitParameters
* authenticate

### Optional Headers
* SoftLayer_Sales_Presale_EventObjectMask
* SoftLayer_Sales_Presale_EventObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order[] </a>

