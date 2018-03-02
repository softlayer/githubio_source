---
title: "getRecentMetricData"
description: "Recent metric data for a guest"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::getRecentMetricData
## Overview 
Recent metric data for a guest 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|time| unsigned integer| The amount of time (in seconds) in the past to retrieve data for. This parameter is not supported by some virtualization platforms at this time.|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object[] </a>

