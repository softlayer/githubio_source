---
title: "getDetailsForDateRange"
description: "Retrieve a collection of detailed metric data over a date range. Ideal if you want to employ your own graphing systems.... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object"
---
# [SoftLayer_Metric_Tracking_Object](/reference/services/SoftLayer_Metric_Tracking_Object)::getDetailsForDateRange

Retrieve metric detail data over a date range.


## Overview 
Retrieve a collection of detailed metric data over a date range. Ideal if you want to employ your own graphing systems.  Note not all metrics support this method.  Those that do not return null. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| The starting date of the range of data you wish to collect.|
|endDate| dateTime| The ending date of the range of data you wish to collect.|
|graphType| array of strings| The type of metric to gather data for (InstanceCount, HostMemoryUsage, HostReservedMemoryUsage).|


### Required Headers
* authenticate
* SoftLayer_Metric_Tracking_ObjectInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Metric_Tracking_Object_Details'>SoftLayer_Container_Metric_Tracking_Object_Details[] </a>


### associatedMethods

*  [SoftLayer_Metric_Tracking_Object::getSummary](/reference/services/SoftLayer_Metric_Tracking_Object/getSummary )

