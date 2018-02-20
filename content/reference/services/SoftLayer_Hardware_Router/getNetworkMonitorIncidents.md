---
title: "getNetworkMonitorIncidents"
description: "Retrieve the status of all of a piece of hardware's network monitoring incidents."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
---
# SoftLayer_Hardware_Router::getNetworkMonitorIncidents
## Overview 
Retrieve the status of all of a piece of hardware's network monitoring incidents.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Hardware_RouterInitParameters
* authenticate

### Optional Headers
* SoftLayer_Hardware_RouterObjectMask
* SoftLayer_Hardware_RouterObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Incident'>SoftLayer_Network_Monitor_Version1_Incident[] </a>
