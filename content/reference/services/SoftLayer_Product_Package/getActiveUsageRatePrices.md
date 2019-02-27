---
title: "getActiveUsageRatePrices"
description: "This method returns a collection of active usage rate [[SoftLayer_Product_Item_Price]] objects for the current package a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
aliases:
    - "/reference/services/softlayer_product_package/getActiveUsageRatePrices"
---
# [SoftLayer_Product_Package](/reference/services/SoftLayer_Product_Package)::getActiveUsageRatePrices

Return the active usage rate prices for the current package. 


## Overview 
This method returns a collection of active usage rate [[SoftLayer_Product_Item_Price]] objects for the current package and specified datacenter. Optionally you can retrieve the active usage rate prices for a particular [[SoftLayer_Product_Item_Category]] by specifying a category code as the first parameter. This information is useful so that you can see "pay as you go" rates (if any) for the current package, location and optionally category. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|locationId| integer| Get the active usage rate prices associated with this location/datacenter|
|categoryCode| string| If provided, get the active usage rate prices for this category code|


### Required Headers
* authenticate
* SoftLayer_Product_PackageInitParameters


### Optional Headers
* SoftLayer_Product_PackageObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>




