---
title: "createPublicArchiveTransaction"
description: "Create a transaction to copy archived block devices into public repository"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
aliases:
    - "/reference/services/softlayer_virtual_guest_block_device_template_group/createPublicArchiveTransaction"
---
# [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group)::createPublicArchiveTransaction


[SoftLayer_Virtual_Guest_Block_Device]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device">}}) can be published together in a public repository for use by everyone. This method generates a transaction to perform a public image of the provided archived block devices. 


## Overview 
Create a transaction to copy archived block devices into public repository

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|groupName| string| The group name for an existing archive|
|summary| string| A summary describing the public image|
|note| string| A long description describing the public image|
|locations| <a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>| Destination location id(s) of the public image|


### Required Headers
* authenticate
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParameters


### Return Values
* integer




