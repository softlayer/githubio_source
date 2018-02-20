---
title: "getObject"
description: "Each product item price must be tied to a category for it to be sold. These categories describe how a particular product... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Category"
---
# SoftLayer_Product_Item_Category::getObject
## Overview 
Each product item price must be tied to a category for it to be sold. These categories describe how a particular product item is sold. For example, the 250GB hard drive can be sold as disk0, disk1, ... disk11. There are different prices for this product item depending on which category it is. This keeps down the number of products in total. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Product_Item_CategoryInitParameters
* authenticate

### Optional Headers
* SoftLayer_Product_Item_CategoryObjectMask
* SoftLayer_Product_Item_CategoryObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>
