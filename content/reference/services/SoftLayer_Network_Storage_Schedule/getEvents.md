---
title: "getEvents"
description: "Retrieve events which have been created as the result of a schedule execution."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Schedule"
---
# SoftLayer_Network_Storage_Schedule::getEvents
## Overview 
Retrieve events which have been created as the result of a schedule execution.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Storage_ScheduleInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Storage_ScheduleObjectMask
* SoftLayer_Network_Storage_ScheduleObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Storage_Event'>SoftLayer_Network_Storage_Event[] </a>
