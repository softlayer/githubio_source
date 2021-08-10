---
title: "getAvailableBillingTermChangePrices"
description: "Retrieves a list of available term prices to this hardware. Currently, price terms are only available for increasing ter... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getAvailableBillingTermChangePrices"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getAvailableBillingTermChangePrices

Retrieves a list of available term prices available to this of hardware. 


## Overview 
Retrieves a list of available term prices to this hardware. Currently, price terms are only available for increasing term length to monthly billed servers. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters


### Optional Headers
* SoftLayer_Hardware_ServerObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>




