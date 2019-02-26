---
title: "getItemPricesFromSoftwareDescriptions"
description: "Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
aliases:
    - "/reference/services/softlayer_product_package/getItemPricesFromSoftwareDescriptions"
---
# [SoftLayer_Product_Package](/reference/services/SoftLayer_Product_Package)::getItemPricesFromSoftwareDescriptions

Returns a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description that are available for the service offering (package). 


## Overview 
Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|softwareDescriptions| <a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description[] </a>| The software that the item prices will be returned for.|
|includeTranslationsFlag| boolean| The flag to specify whether software translations should be considered when looking at the software descriptions.|
|returnAllPricesFlag| boolean| The flag to specify whether all item prices or just the first price for the software descriptions.|


### Required Headers
* authenticate
* SoftLayer_Product_PackageInitParameters


### Optional Headers
* SoftLayer_Product_PackageObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> <<< EOT 



