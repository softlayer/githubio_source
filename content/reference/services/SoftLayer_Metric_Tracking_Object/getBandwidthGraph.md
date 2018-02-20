---
title: "getBandwidthGraph"
description: "Retrieve a PNG image of a bandwidth graph representing the bandwidth usage over time recorded by SofTLayer's bandwidth p... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object"
---
# SoftLayer_Metric_Tracking_Object::getBandwidthGraph
## Overview 
Retrieve a PNG image of a bandwidth graph representing the bandwidth usage over time recorded by SofTLayer's bandwidth pollers. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| The starting date of the range of graph data you wish to retrieve.|
|endDateTime| dateTime| The ending date of the range of graph data you wish to retrieve.|
|graphType| string| $graphType The type type of the bandwidth graph you wish to retrieve, either "public" or "private".|
|fontSize| integer| $fontSize Size to draw the font on the graph labels and legend.|
|graphWidth| integer| $graphWidth Number of pixel wide you would like to draw the graph.|
|graphHeight| integer| $graphHeight Number of pixel high you would like to draw the graph.|
|doNotShowTimeZone| boolean| $doNotShowTimeZone Whether or not you'd like the timezone printed on the graph margin.|


### Required Headers
* authenticate
* SoftLayer_Metric_Tracking_ObjectInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>
