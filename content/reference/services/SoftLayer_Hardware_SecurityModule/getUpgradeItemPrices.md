---
title: "getUpgradeItemPrices"
description: "Retrieve a list of upgradeable items available to this piece of hardware. Currently, getUpgradeItemPrices retrieves upgr... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
---
# SoftLayer_Hardware_SecurityModule::getUpgradeItemPrices
## Overview 
Retrieve a list of upgradeable items available to this piece of hardware. Currently, getUpgradeItemPrices retrieves upgrades available for a server's memory, hard drives, network port speed, bandwidth allocation and GPUs. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>

