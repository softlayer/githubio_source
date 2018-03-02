---
title: "getRecalculatedOrderContainer"
description: "Generate an [[SoftLayer_Container_Product_Order|order container]] from a billing order. This will take into account prom... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
---
# SoftLayer_Billing_Order::getRecalculatedOrderContainer
## Overview 
Generate an [[SoftLayer_Container_Product_Order|order container]] from a billing order. This will take into account promotions, reseller status, estimated taxes and all other standard order verification processes. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|message| string| Message to return with the verified order|
|ignoreDiscountsFlag| boolean| This flag is set and used internally|


### Required Headers
* authenticate
* SoftLayer_Billing_OrderInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Product_Order'>SoftLayer_Container_Product_Order </a>

