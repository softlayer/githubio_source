---
title: "removeLocations"
description: "This method will create transaction(s) to remove available locations from an archive image template."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
aliases:
    - "/reference/services/softlayer_virtual_guest_block_device_template_group/removeLocations"
---
# [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group)::removeLocations

[[SoftLayer_Virtual_Guest_Block_Devices|Block Devices]] can be made available in all storage locations. This method will create transaction(s) to remove available locations from an archive image template. 


## Overview 
This method will create transaction(s) to remove available locations from an archive image template.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|locations| <a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>| to remove from the image template.|


### Required Headers
* authenticate
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParameters


### Return Values
* boolean




