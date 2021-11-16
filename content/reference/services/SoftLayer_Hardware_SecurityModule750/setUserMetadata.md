---
title: "setUserMetadata"
description: "Sets the data that will be written to the configuration drive."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/setUserMetadata"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::setUserMetadata


Sets the server's user metadata value.


## Overview 
Sets the data that will be written to the configuration drive. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|metadata| array of strings| base64 encoded strings that will be written to the configuration drive|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Optional Headers
* SoftLayer_Hardware_SecurityModule750ObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Hardware_Attribute'>SoftLayer_Hardware_Attribute[] </a>




