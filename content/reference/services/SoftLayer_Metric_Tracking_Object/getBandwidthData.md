---
title: "getBandwidthData"
description: "Retrieve a collection of raw bandwidth data from an individual public or private network tracking object. Raw data is id... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Metric"
classes:
    - "SoftLayer_Metric_Tracking_Object"
---
# [SoftLayer_Metric_Tracking_Object](/reference/services/SoftLayer_Metric_Tracking_Object)::getBandwidthData

Retrieve raw bandwidth data from a tracking object.


## Overview 
Retrieve a collection of raw bandwidth data from an individual public or private network tracking object. Raw data is ideal if you with to employ your own traffic storage and graphing systems. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| The starting date of the range of data you wish to collect.|
|endDateTime| dateTime| The ending date of the range of data you wish to collect.|
|type| string| The type type of the bandwidth data you wish to retrieve, either "public" or "private".|
|rollupSeconds| integer| The amount of rollup seconds to segregate data in. Rollup seconds enable you to retrieve the average amount of bandwidth used per individual delta in your date range. For instance, a rollupSeconds value of 3600 will return data averaged over every hour.|


### Required Headers
* authenticate
* SoftLayer_Metric_Tracking_ObjectInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>


### associatedMethods

*  [SoftLayer_Metric_Tracking_Object::getBandwidthGraph](/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthGraph )
*  [SoftLayer_Metric_Tracking_Object::getBandwidthTotal](/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthTotal )

