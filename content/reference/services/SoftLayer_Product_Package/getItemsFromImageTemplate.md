---
title: "getItemsFromImageTemplate"
description: "Return a collection of [SoftLayer_Product_Item]({{<ref 'reference/datatypes/SoftLayer_Product_Item'>}}) objects from a [... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package"
aliases:
    - "/reference/services/softlayer_product_package/getItemsFromImageTemplate"
---
# [SoftLayer_Product_Package](/reference/services/SoftLayer_Product_Package)::getItemsFromImageTemplate


Return a collection of [SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}}) objects from a [SoftLayer_Virtual_Guest_Block_Device_Template_Group]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group">}}) object


## Overview 
Return a collection of [SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}}) objects from a [SoftLayer_Virtual_Guest_Block_Device_Template_Group]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group">}}) object

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|imageTemplate| <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group </a>| The image template that the items will be returned for.|


### Required Headers
* authenticate
* SoftLayer_Product_PackageInitParameters


### Optional Headers
* SoftLayer_Product_PackageObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'Software description is not available with the the service offering on this server.' when the product item cannot be determined. 



