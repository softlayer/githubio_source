---
title: "deleteObject"
description: "Deleting a block device template group is different from the deletion of other objects.  A block device template group c... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
aliases:
    - "/reference/services/softlayer_virtual_guest_block_device_template_group/deleteObject"
---
# [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group)::deleteObject


Create a transaction that will remove all block device templates from the group and delete the disk images associated with them. 


## Overview 
Deleting a block device template group is different from the deletion of other objects.  A block device template group can contain several gigabytes of data in its disk images.  This may take some time to delete and requires a transaction to be created.  This method creates a transaction that will delete all resources associated with the block device template group. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParameters


### Optional Headers
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>




