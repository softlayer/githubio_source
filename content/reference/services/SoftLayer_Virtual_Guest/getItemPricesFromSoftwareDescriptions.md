---
title: "getItemPricesFromSoftwareDescriptions"
description: "Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getItemPricesFromSoftwareDescriptions

Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description


## Overview 
Return a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|softwareDescriptions| <a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description[] </a>| The software that the item prices will be returned for.|
|includeTranslationsFlag| boolean| The flag to specify whether software translations should be considered when looking at the software descriptions.|
|returnAllPricesFlag| boolean| The flag to specify whether all item prices or just the first price for the software descriptions.|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>

