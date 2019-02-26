---
title: "captureImage"
description: "Captures a Flex Image of the hard disk on the virtual machine, based on the capture template parameter. Returns the imag... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/captureImage"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::captureImage

Captures a Flex Image of the hard disk on the virtual machine.


## Overview 
Captures a Flex Image of the hard disk on the virtual machine, based on the capture template parameter. Returns the image template group containing the disk image. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|captureTemplate| <a href='/reference/datatypes/SoftLayer_Container_Disk_Image_Capture_Template'>SoftLayer_Container_Disk_Image_Capture_Template </a>| |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group </a>




