---
title: "sparePool"
description: "The ability to place bare metal servers in a state where they are powered down, and ports closed yet still allocated to... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/sparePool"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::sparePool

Allows servers to be added to or removed from the spare pool.


## Overview 
The ability to place bare metal servers in a state where they are powered down, and ports closed yet still allocated to the customer as a part of the Spare Pool program. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|action| string| Action to 'add' server to spare pool or remove (use 'activate') from spare pool|
|newOrder| boolean| Set to true if a Spare Pool Server was ordered; otherwise false|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers

### Return Values
boolean

