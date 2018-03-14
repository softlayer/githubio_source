---
title: "getSummary"
description: "Retrieve a metric summary. Ideal if you want to employ your own graphing systems.  Note not all metric types contain a s... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object"
aliases:
    - "/reference/services/softlayer_metric_tracking_object/getSummary"
---
# [SoftLayer_Metric_Tracking_Object](/reference/services/SoftLayer_Metric_Tracking_Object)::getSummary

Retrieve metric summary.


## Overview 
Retrieve a metric summary. Ideal if you want to employ your own graphing systems.  Note not all metric types contain a summary.  These return null. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|graphType| string| The type of metric to gather data for (InstanceCount, HostMemoryUsage, HostReservedMemoryUsage).|


### Required Headers
* authenticate
* SoftLayer_Metric_Tracking_ObjectInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Metric_Tracking_Object_Summary'>SoftLayer_Container_Metric_Tracking_Object_Summary </a>


### associatedMethods

*  [SoftLayer_Metric_Tracking_Object::getDetailsForDateRange](/reference/services/SoftLayer_Metric_Tracking_Object/getDetailsForDateRange )

