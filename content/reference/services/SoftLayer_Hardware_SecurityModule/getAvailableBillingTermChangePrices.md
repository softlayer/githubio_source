---
title: "getAvailableBillingTermChangePrices"
description: "Retrieves a list of available term prices to this hardware. Currently, price terms are only available for increasing ter... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getAvailableBillingTermChangePrices"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getAvailableBillingTermChangePrices

Retrieves a list of available term prices available to this of hardware. 


## Overview 
Retrieves a list of available term prices to this hardware. Currently, price terms are only available for increasing term length to monthly billed servers. 

-----

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
* <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>




