---
title: "getCpuMetricImageByDate"
description: "Use this method when needing a CPU usage image for a single guest.  It will gather the correct input parameters for the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::getCpuMetricImageByDate
## Overview 
Use this method when needing a CPU usage image for a single guest.  It will gather the correct input parameters for the generic graphing utility based on the date ranges 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| datetime of the start date of the graph|
|endDateTime| dateTime| datetime of the ending date of the graph|
|cpuIndexes| array of integers| reserved for future use. An array of cpu index numbers to specify which cpus to graph|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>

