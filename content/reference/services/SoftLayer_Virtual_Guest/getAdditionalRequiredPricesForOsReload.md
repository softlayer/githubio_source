---
title: "getAdditionalRequiredPricesForOsReload"
description: "Return a collection of SoftLayer_Item_Price objects for an OS reload"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::getAdditionalRequiredPricesForOsReload
## Overview 
Return a collection of SoftLayer_Item_Price objects for an OS reload

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|config| <a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration'>SoftLayer_Container_Hardware_Server_Configuration </a>| The new cloud configuration for the reload.|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>
