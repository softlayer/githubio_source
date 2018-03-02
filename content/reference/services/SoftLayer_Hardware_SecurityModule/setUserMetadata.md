---
title: "setUserMetadata"
description: "Sets the data that will be written to the configuration drive."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
---
# SoftLayer_Hardware_SecurityModule::setUserMetadata
## Overview 
Sets the data that will be written to the configuration drive. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|metadata| array of strings| base64 encoded strings that will be written to the configuration drive|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute[] </a>

