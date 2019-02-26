---
title: "captureImage"
description: "Captures a Flex Image of the hard disk on the physical machine, based on the capture template parameter. Returns the ima... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/captureImage"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::captureImage

Captures a Flex Image of the hard disk on the physical machine.


## Overview 
Captures a Flex Image of the hard disk on the physical machine, based on the capture template parameter. Returns the image template group containing the disk image. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|captureTemplate| <a href='/reference/datatypes/SoftLayer_Container_Disk_Image_Capture_Template'>SoftLayer_Container_Disk_Image_Capture_Template </a>| |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters


### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group </a>




