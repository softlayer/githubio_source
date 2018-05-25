---
title: "findGcImagesByCurrentUser"
description: "Find block device template groups contain GC enabled image for the current active user. Caller can optionally specify da... "
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

Fetch collection of GC enabled images for the account of the current active customer user. 


## Overview 
Find block device template groups contain GC enabled image for the current active user. Caller can optionally specify data center names to retrieve GC image from those data centers only. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|dataCenters| array of strings| |


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a>

