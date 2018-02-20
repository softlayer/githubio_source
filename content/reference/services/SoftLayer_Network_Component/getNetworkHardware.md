---
title: "getNetworkHardware"
description: "Retrieve all network devices in SoftLayer's network hierarchy that this device is connected to."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
---
# SoftLayer_Network_Component::getNetworkHardware
## Overview 
Retrieve all network devices in SoftLayer's network hierarchy that this device is connected to.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_ComponentInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_ComponentObjectMask
* SoftLayer_Network_ComponentObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>
