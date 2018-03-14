---
title: "setAvailableLocations"
description: "Create transaction(s) to set the archived block device available locations"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
aliases:
    - "/reference/services/softlayer_virtual_guest_block_device_template_group/setAvailableLocations"
---
# [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group)::setAvailableLocations

[[SoftLayer_Virtual_Guest_Block_Devices|Block Devices]] can be made available in all storage locations. This method generates the necessary transaction(s) to set available locations for archived block devices. WARNING - Any existing image template location(s) not sent in as a parameter will be deleted.  If you wish to keep your existing locations and add some new location(s), you must send in all of the locations as parameters. 


## Overview 
Create transaction(s) to set the archived block device available locations

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|locations| <a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>| location(s)of the archived block devices|


### Required Headers
* authenticate
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParameters

### Optional Headers

### Return Values
boolean

