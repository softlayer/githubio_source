---
title: "getUpgradeItemPrices"
description: "Retrieve a list of upgradeable items available to this piece of hardware. Currently, getUpgradeItemPrices retrieves upgr... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getUpgradeItemPrices"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getUpgradeItemPrices

Retrieve a list of upgradable items available to a piece of hardware.


## Overview 
Retrieve a list of upgradeable items available to this piece of hardware. Currently, getUpgradeItemPrices retrieves upgrades available for a server's memory, hard drives, network port speed, bandwidth allocation and GPUs. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Optional Headers
* SoftLayer_Hardware_SecurityModule750ObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>



### Error Handling

* SoftLayer_Exception 

> "Hardware [hostname.domain] cannot be upgraded due to the incorrect billing information. Please contact SoftLayer Sales." 



