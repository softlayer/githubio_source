---
title: "getStandardCategories"
description: "This call is similar to [[SoftLayer_Product_Package/getCategories|getCategories]], except that it does not include accou... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
aliases:
    - "/reference/services/softlayer_product_package/getStandardCategories"
---
# [SoftLayer_Product_Package](/reference/services/SoftLayer_Product_Package)::getStandardCategories

This call is similar to [[SoftLayer_Product_Package/getCategories|getCategories]], except that it does not include account-restricted pricing. Not all accounts have restricted pricing. 


## Overview 
This call is similar to [[SoftLayer_Product_Package/getCategories|getCategories]], except that it does not include account-restricted pricing. Not all accounts have restricted pricing. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Product_PackageInitParameters

### Optional Headers
* SoftLayer_Product_PackageObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category[] </a>

