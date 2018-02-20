---
title: "getGraphData"
description: "This method returns the metric data for each of the configuration values provided during the given time range."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
---
# SoftLayer_Monitoring_Agent::getGraphData
## Overview 
This method returns the metric data for each of the configuration values provided during the given time range. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|metricDataTypes| <a href='/reference/datatypes/SoftLayer_Container_Metric_Data_Type'>SoftLayer_Container_Metric_Data_Type[] </a>| Array of metric data types|
|startDate| dateTime| The start date for the range of metric data to retrieve, must be in GMT.|
|endDate| dateTime| The end date for the range of metric data to retrieve, must be in GMT.|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>
