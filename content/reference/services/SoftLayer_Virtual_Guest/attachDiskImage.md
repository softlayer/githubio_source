---
title: "attachDiskImage"
description: "Creates a transaction to attach a guest's disk image. If the disk image is already attached it will be ignored. 

WARNIN... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/attachDiskImage"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::attachDiskImage


Attaches a disk image.


## Overview 
Creates a transaction to attach a guest's disk image. If the disk image is already attached it will be ignored. 

WARNING: SoftLayer_Virtual_Guest::checkHostDiskAvailability should be called before this method. If the SoftLayer_Virtual_Guest::checkHostDiskAvailability method is not called before this method, the guest migration will happen automatically. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|imageId| integer| |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>




