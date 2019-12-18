---
title: "getOrderPremiums"
description: "Retrieve the premium price modifiers associated with the [SoftLayer_Product_Item_Price]({{<ref 'reference/datatypes/Soft... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
aliases:
    - "/reference/services/softlayer_product_package/getOrderPremiums"
---
# [SoftLayer_Product_Package](/reference/services/SoftLayer_Product_Package)::getOrderPremiums

Retrieve the premium price modifiers associated with the [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) and [SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) objects in a package.


## Overview 
Retrieve the premium price modifiers associated with the [SoftLayer_Product_Item_Price]({{<ref "reference/datatypes/SoftLayer_Product_Item_Price">}}) and [SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) objects in a package.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Product_PackageInitParameters
* authenticate


### Optional Headers
* SoftLayer_Product_PackageObjectMask
* SoftLayer_Product_PackageObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item_Price_Premium'>SoftLayer_Product_Item_Price_Premium[] </a>




