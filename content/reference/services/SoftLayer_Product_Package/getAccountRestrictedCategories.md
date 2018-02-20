---
title: "getAccountRestrictedCategories"
description: "Retrieve the results from this call are similar to [[SoftLayer_Product_Package/getCategories|getCategories]], but these... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
---
# SoftLayer_Product_Package::getAccountRestrictedCategories
## Overview 
Retrieve the results from this call are similar to [[SoftLayer_Product_Package/getCategories|getCategories]], but these ONLY include account-restricted prices. Not all accounts have restricted pricing.

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
<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>
