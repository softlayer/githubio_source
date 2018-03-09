---
title: "getObject"
description: "getObject retrieves the SoftLayer_Software_Component object whose ID corresponds to the ID number of the init parameter... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component"
---
# [SoftLayer_Software_Component](/reference/services/SoftLayer_Software_Component)::getObject

Retrieve a SoftLayer_Software_Component record.


## Overview 
getObject retrieves the SoftLayer_Software_Component object whose ID corresponds to the ID number of the init parameter passed to the SoftLayer_Software_Component service. 

The best way to get software components is through getSoftwareComponents from the Hardware service. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Software_ComponentInitParameters
* authenticate

### Optional Headers
* SoftLayer_Software_ComponentObjectMask
* SoftLayer_Software_ComponentObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>

