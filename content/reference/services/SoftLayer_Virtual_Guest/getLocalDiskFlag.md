---
title: "getLocalDiskFlag"
description: "Retrieve a flag indicating that the virtual guest has at least one disk which is local to the host it runs on. This does... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::getLocalDiskFlag
## Overview 
Retrieve a flag indicating that the virtual guest has at least one disk which is local to the host it runs on. This does not include a SWAP device.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Virtual_GuestInitParameters
* authenticate

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_Virtual_GuestObjectFilter
* SoftLayer_ObjectMask

### Return Values
boolean

