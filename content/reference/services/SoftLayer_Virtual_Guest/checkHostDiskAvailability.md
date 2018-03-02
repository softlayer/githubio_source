---
title: "checkHostDiskAvailability"
description: "Checks the associated host for available disk space to determine if guest migration is necessary. This method is only us... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::checkHostDiskAvailability
## Overview 
Checks the associated host for available disk space to determine if guest migration is necessary. This method is only used with local disks. If this method returns false, calling attachDiskImage($imageId) will automatically migrate the destination guest to a new host before attaching the portable volume. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|diskCapacity| integer| |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers

### Return Values
boolean

