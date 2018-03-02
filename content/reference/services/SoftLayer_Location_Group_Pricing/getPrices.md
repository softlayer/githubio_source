---
title: "getPrices"
description: "Retrieve the prices that this pricing location group limits. All of these prices will only be available in the locations... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Group_Pricing"
---
# SoftLayer_Location_Group_Pricing::getPrices
## Overview 
Retrieve the prices that this pricing location group limits. All of these prices will only be available in the locations defined by this pricing location group.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Location_Group_PricingInitParameters
* authenticate

### Optional Headers
* SoftLayer_Location_Group_PricingObjectMask
* SoftLayer_Location_Group_PricingObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>

