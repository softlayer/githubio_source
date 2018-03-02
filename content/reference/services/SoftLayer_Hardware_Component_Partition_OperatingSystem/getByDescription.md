---
title: "getByDescription"
description: "The '''getByDescription''' method retrieves all possible partition templates based on the description (required paramete... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_OperatingSystem"
---
# SoftLayer_Hardware_Component_Partition_OperatingSystem::getByDescription
## Overview 
The '''getByDescription''' method retrieves all possible partition templates based on the description (required parameter) entered when calling the method. The description is typically the operating system's name. Current recognized values include 'linux', 'windows', 'freebsd', and 'Debian'. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|description| string| The description of the operating system|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Hardware_Component_Partition_OperatingSystemObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_OperatingSystem'>SoftLayer_Hardware_Component_Partition_OperatingSystem </a>

