---
title: "getData"
description: "Retrieve an individual partition for a partition template. This is identical to 'partitionTemplatePartition' except this... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_Template"
aliases:
    - "/reference/services/softlayer_hardware_component_partition_template/getData"
---
# [SoftLayer_Hardware_Component_Partition_Template](/reference/services/SoftLayer_Hardware_Component_Partition_Template)::getData

Retrieve an individual partition for a partition template. This is identical to 'partitionTemplatePartition' except this will sort unix partitions.


## Overview 
Retrieve an individual partition for a partition template. This is identical to 'partitionTemplatePartition' except this will sort unix partitions.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Hardware_Component_Partition_TemplateInitParameters
* authenticate


### Optional Headers
* SoftLayer_Hardware_Component_Partition_TemplateObjectMask
* SoftLayer_Hardware_Component_Partition_TemplateObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template_Partition'>SoftLayer_Hardware_Component_Partition_Template_Partition[] </a>




