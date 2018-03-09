---
title: "detachDiskImage"
description: "Creates a transaction to detach a guest's disk image. If the disk image is already detached it will be ignored. 

WARNIN... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::detachDiskImage

Detaches a disk image.


## Overview 
Creates a transaction to detach a guest's disk image. If the disk image is already detached it will be ignored. 

WARNING: The transaction created by this service will shut down the guest while the disk image is attached. The guest will be turned back on once this process is complete. 

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
<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>

