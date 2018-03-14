---
title: "getBlockDevices"
description: "Retrieve a computing instance's block devices. Block devices link [[SoftLayer_Virtual_Disk_Image|disk images]] to comput... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getBlockDevices"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getBlockDevices

Retrieve a computing instance's block devices. Block devices link [[SoftLayer_Virtual_Disk_Image|disk images]] to computing instances.


## Overview 
Retrieve a computing instance's block devices. Block devices link [[SoftLayer_Virtual_Disk_Image|disk images]] to computing instances.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Virtual_GuestInitParameters
* authenticate

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_Virtual_GuestObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device'>SoftLayer_Virtual_Guest_Block_Device[] </a>

