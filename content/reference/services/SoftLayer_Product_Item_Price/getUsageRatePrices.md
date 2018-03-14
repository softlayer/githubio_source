---
title: "getUsageRatePrices"
description: "Returns a collection of rate-based [[SoftLayer_Product_Item_Price]] objects associated with the [[SoftLayer_Product_Item... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Price"
aliases:
    - "/reference/services/softlayer_product_item_price/getUsageRatePrices"
---
# [SoftLayer_Product_Item_Price](/reference/services/SoftLayer_Product_Item_Price)::getUsageRatePrices

Get all the rate-based prices for the location and items specified. 


## Overview 
Returns a collection of rate-based [[SoftLayer_Product_Item_Price]] objects associated with the [[SoftLayer_Product_Item]] objects and the [[SoftLayer_Location]] specified. The location is required to get the appropriate rate-based prices because the usage rates may vary from datacenter to datacenter. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|location| <a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>| The [[SoftLayer_Location]] object|
|items| <a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>| Array of [[SoftLayer_Product_Item]] objects used to obtain rate-based prices|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Product_Item_PriceObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>

