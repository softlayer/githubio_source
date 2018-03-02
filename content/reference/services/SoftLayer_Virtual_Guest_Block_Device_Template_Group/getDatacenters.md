---
title: "getDatacenters"
description: "Retrieve a collection of locations containing a copy of this image template group. Will only be populated for parent tem... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
---
# SoftLayer_Virtual_Guest_Block_Device_Template_Group::getDatacenters
## Overview 
Retrieve a collection of locations containing a copy of this image template group. Will only be populated for parent template group objects.

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
<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>

