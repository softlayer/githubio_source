---
title: "getObject"
description: "getObject retrieves the SoftLayer_Hardware_Component_Partition_Template object whose ID number corresponds to the ID num... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_Template"
aliases:
    - "/reference/services/softlayer_hardware_component_partition_template/getObject"
---
# [SoftLayer_Hardware_Component_Partition_Template](/reference/services/SoftLayer_Hardware_Component_Partition_Template)::getObject

Retrieve a SoftLayer_Hardware_Component_Partition_Template record.


## Overview 
getObject retrieves the SoftLayer_Hardware_Component_Partition_Template object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Hardware_Component_Partition_Template service. You can only retrieve the partition templates that your account created or the templates predefined by SoftLayer. 

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
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template'>SoftLayer_Hardware_Component_Partition_Template </a>




