---
title: "getValidBlockDeviceTemplateGroups"
description: "This method will return the list of block device template groups that are valid to the host. For instance, it will only... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
---
# SoftLayer_Hardware_SecurityModule::getValidBlockDeviceTemplateGroups
## Overview 
This method will return the list of block device template groups that are valid to the host. For instance, it will only retrieve FLEX images. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|visibility| string| whether to return the private, public or all image templates.  possible values are: private, public, all|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_ObjectMask
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupObjectFilter
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a>

