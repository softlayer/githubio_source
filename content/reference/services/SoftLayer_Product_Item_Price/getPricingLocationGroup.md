---
title: "getPricingLocationGroup"
description: "Retrieve the pricing location group that this price is applicable for. Prices that have a pricing location group will on... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Price"
aliases:
    - "/reference/services/softlayer_product_item_price/getPricingLocationGroup"
---
# [SoftLayer_Product_Item_Price](/reference/services/SoftLayer_Product_Item_Price)::getPricingLocationGroup

Retrieve the pricing location group that this price is applicable for. Prices that have a pricing location group will only be available for ordering with the locations specified on the location group.


## Overview 
Retrieve the pricing location group that this price is applicable for. Prices that have a pricing location group will only be available for ordering with the locations specified on the location group.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Product_Item_PriceInitParameters
* authenticate


### Optional Headers
* SoftLayer_Product_Item_PriceObjectMask
* SoftLayer_Product_Item_PriceObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Location_Group_Pricing'>SoftLayer_Location_Group_Pricing </a>




