---
title: "findGcImagesByCurrentUser"
description: "Find block device template groups containing a GC enabled cloudinit image for the current active user. A sorted collecti... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
aliases:
    - "/reference/services/softlayer_virtual_guest_block_device_template_group/findGcImagesByCurrentUser"
---
# [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group)::findGcImagesByCurrentUser

Fetch a sorted collection of GC enabled cloudinit images for the account of the current active customer user. 


## Overview 
Find block device template groups containing a GC enabled cloudinit image for the current active user. A sorted collection of groups is returned. The Caller can optionally specify data center or region names to retrieve GC images from only those locations. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|dataCenters| array of strings| The name of the data center containing the images|
|regions| array of strings| The name of the region containing the images|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a>




