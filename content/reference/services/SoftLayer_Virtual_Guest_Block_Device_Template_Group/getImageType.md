---
title: "getImageType"
description: "Retrieve the virtual disk image type of this template. Value will be populated on parent and child, but only supports ob... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
---
# SoftLayer_Virtual_Guest_Block_Device_Template_Group::getImageType
## Overview 
Retrieve the virtual disk image type of this template. Value will be populated on parent and child, but only supports object filtering on the parent.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParameters
* authenticate

### Optional Headers
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupObjectMask
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Type'>SoftLayer_Virtual_Disk_Image_Type </a>

