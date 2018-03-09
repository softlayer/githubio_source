---
title: "getSummaryData"
description: "Returns summarized metric data for the date range, metric type and summary period provided."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object"
---
# [SoftLayer_Metric_Tracking_Object](/reference/services/SoftLayer_Metric_Tracking_Object)::getSummaryData

Returns the metric data for the date range provided


## Overview 
Returns summarized metric data for the date range, metric type and summary period provided. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| |
|endDateTime| dateTime| |
|validTypes| <a href='/reference/datatypes/SoftLayer_Container_Metric_Data_Type'>SoftLayer_Container_Metric_Data_Type[] </a>| |
|summaryPeriod| integer| 300, 600, 1800, 3600, 43200 or 86400 seconds|


### Required Headers
* authenticate
* SoftLayer_Metric_Tracking_ObjectInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>

