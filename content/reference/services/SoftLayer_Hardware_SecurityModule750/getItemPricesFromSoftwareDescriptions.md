---
title: "getItemPricesFromSoftwareDescriptions"
description: "Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getItemPricesFromSoftwareDescriptions"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getItemPricesFromSoftwareDescriptions

Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description


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
* SoftLayer_Hardware_SecurityModule750InitParameters


### Optional Headers
* SoftLayer_Hardware_SecurityModule750ObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'Unable to locate billing item.' when the billing item cannot be determined. 



