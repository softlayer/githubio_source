---
title: "getCpuMetricDataByDate"
description: "Use this method when needing the metric data for a single guest's CPUs.  It will gather the correct input parameters bas... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getCpuMetricDataByDate"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getCpuMetricDataByDate

Retrieve records containing the percentage of the amount of time that a cpu was in use for the specified time frame for a computing instance. 


## Overview 
Use this method when needing the metric data for a single guest's CPUs.  It will gather the correct input parameters based on the date ranges 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| datetime of the start date of the graph|
|endDateTime| dateTime| datetime of the ending date of the graph|
|cpuIndexes| array of integers| reserved for future use. An array of cpu index numbers to specify which cpus to graph|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>




