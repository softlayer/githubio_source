---
title: "getValidBlockDeviceTemplateGroups"
description: "This method will return the list of block device template groups that are valid to the host. For instance, it will valid... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getValidBlockDeviceTemplateGroups"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getValidBlockDeviceTemplateGroups

Return a list of valid block device template groups based on this host


## Overview 
This method will return the list of block device template groups that are valid to the host. For instance, it will validate that the template groups returned are compatible with the size and number of disks on the host. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|visibility| string| whether to return the private, shared, public or all image templates.  possible values are: private, shared, public, all|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupObjectFilter
* resultLimit

### Return Values
* <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a>




