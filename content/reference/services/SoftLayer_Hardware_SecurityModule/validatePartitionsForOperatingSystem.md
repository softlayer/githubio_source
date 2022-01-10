---
title: "validatePartitionsForOperatingSystem"
description: "Validates a collection of partitions for an operating system"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/validatePartitionsForOperatingSystem"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::validatePartitionsForOperatingSystem


Validates a collection of partitions for an operating system


## Overview 
Validates a collection of partitions for an operating system

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|operatingSystem| <a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>| The operating system that is to be verified against.|
|partitions| <a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition'>SoftLayer_Hardware_Component_Partition[] </a>| The partitions that are to be used with the operating system.|


### Required Headers
* authenticate


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'Invalid operating system provided.' when the operating system description that was provided does not exist. 

* SoftLayer_Exception_Public 

> Throws the exception '<partition> partition is too small...' when the partition that was provided does not meet the minimum requirements 

* SoftLayer_Exception_Public 

> Throws the exception 'Missing required partitions:...' when partitions that are required for the operating system indicated are not provided. 



