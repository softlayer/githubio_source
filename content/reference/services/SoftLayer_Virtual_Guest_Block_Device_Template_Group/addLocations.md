---
title: "addLocations"
description: "This method will create transaction(s) to add available locations to an archive image template."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
aliases:
    - "/reference/services/softlayer_virtual_guest_block_device_template_group/addLocations"
---
# [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group)::addLocations


[SoftLayer_Virtual_Guest_Block_Device]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device">}}) can be made available in all storage locations. This method will create transaction(s) to add available locations to an archive image template. 


## Overview 
This method will create transaction(s) to add available locations to an archive image template.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|locations| <a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>| to add to the image template.|


### Required Headers
* authenticate
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParameters


### Return Values
* boolean




