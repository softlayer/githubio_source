---
title: "getUpgradeItemPrices"
description: "getUpgradeItemPrices() retrieves a list of all upgrades available to a CloudLayer Computing Instance. Upgradeable items... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getUpgradeItemPrices"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getUpgradeItemPrices

Retrieve a computing instance's upgradeable items.


## Overview 
getUpgradeItemPrices() retrieves a list of all upgrades available to a CloudLayer Computing Instance. Upgradeable items include, but are not limited to, number of cores, amount of RAM, storage configuration, and network port speed. 

This method exclude downgrade item prices by default. You can set the "includeDowngradeItemPrices" parameter to true so that it can include downgrade item prices. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|includeDowngradeItemPrices| boolean| If set to true, this method will include the downgrade item prices.|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>




