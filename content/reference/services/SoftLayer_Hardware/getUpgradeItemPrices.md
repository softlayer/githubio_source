---
title: "getUpgradeItemPrices"
description: "Retrieve a list of upgradeable items available to this piece of hardware. Currently, getUpgradeItemPrices retrieves upgr... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
aliases:
    - "/reference/services/softlayer_hardware/getUpgradeItemPrices"
---
# [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware)::getUpgradeItemPrices

Retrieve a list of upgradable items available to a piece of hardware.


## Overview 
Retrieve a list of upgradeable items available to this piece of hardware. Currently, getUpgradeItemPrices retrieves upgrades available for a server's memory, hard drives, network port speed, bandwidth allocation and GPUs. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_HardwareInitParameters


### Optional Headers
* SoftLayer_HardwareObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>



### Error Handling

* SoftLayer_Exception 

> "Hardware [hostname.domain] cannot be upgraded due to the incorrect billing information. Please contact SoftLayer Sales." 



