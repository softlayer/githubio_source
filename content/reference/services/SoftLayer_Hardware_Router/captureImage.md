---
title: "captureImage"
description: "Captures a Flex Image of the hard disk on the physical machine, based on the capture template parameter. Returns the ima... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
aliases:
    - "/reference/services/softlayer_hardware_router/captureImage"
---
# [SoftLayer_Hardware_Router](/reference/services/SoftLayer_Hardware_Router)::captureImage

Captures a Flex Image of the hard disk on the physical machine.


## Overview 
Captures a Flex Image of the hard disk on the physical machine, based on the capture template parameter. Returns the image template group containing the disk image. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|captureTemplate| <a href='/reference/datatypes/SoftLayer_Container_Disk_Image_Capture_Template'>SoftLayer_Container_Disk_Image_Capture_Template </a>| |


### Required Headers
* authenticate
* SoftLayer_Hardware_RouterInitParameters

### Optional Headers
* SoftLayer_Hardware_RouterObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group </a>

