---
title: "getAccountReferences"
description: "Retrieve the accounts which may have read-only access to an image template group. Will only be populated for parent temp... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
aliases:
    - "/reference/services/softlayer_virtual_guest_block_device_template_group/getAccountReferences"
---
# [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group)::getAccountReferences

Retrieve the accounts which may have read-only access to an image template group. Will only be populated for parent template group objects.


## Overview 
Retrieve the accounts which may have read-only access to an image template group. Will only be populated for parent template group objects.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParameters
* authenticate

### Optional Headers
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupObjectMask
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts'>SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts[] </a>

