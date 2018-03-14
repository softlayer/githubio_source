---
title: "getGraph"
description: "Retrieve a PNG image of a metric in graph form."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object"
aliases:
    - "/reference/services/softlayer_metric_tracking_object/getGraph"
---
# [SoftLayer_Metric_Tracking_Object](/reference/services/SoftLayer_Metric_Tracking_Object)::getGraph

Retrieve a graph of a virtual hosting platform's per instance use.


## Overview 
Retrieve a PNG image of a metric in graph form. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| timestamp of the starting date of the graph|
|endDateTime| dateTime| timestamp of the ending date of the graph|
|graphType| array of strings| type of the graph ("public" or "private" for bandwidth, "InstanceCount" or "HostMemoryUsage" or "HostReservedMemoryUsage" for virtual hosts)|


### Required Headers
* authenticate
* SoftLayer_Metric_Tracking_ObjectInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>

