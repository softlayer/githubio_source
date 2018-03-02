---
title: "getMemoryMetricImageByDate"
description: "Use this method when needing a image displaying the amount of memory used over time for a single computing instance. It... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::getMemoryMetricImageByDate
## Overview 
Use this method when needing a image displaying the amount of memory used over time for a single computing instance. It will gather the correct input parameters for the generic graphing utility based on the date ranges 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| datetime of the start date of the graph|
|endDateTime| dateTime| datetime of the ending date of the graph|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>

