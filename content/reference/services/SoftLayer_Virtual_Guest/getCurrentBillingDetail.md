---
title: "getCurrentBillingDetail"
description: "getUpgradeItemPrices() retrieves a list of all upgrades available to a CloudLayer Computing Instance. Upgradeable items... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getCurrentBillingDetail

Retrieve a computing instance's upgradeable items.


## Overview 
getUpgradeItemPrices() retrieves a list of all upgrades available to a CloudLayer Computing Instance. Upgradeable items include, but are not limited to, number of cores, amount of RAM, storage configuration, and network port speed. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>

