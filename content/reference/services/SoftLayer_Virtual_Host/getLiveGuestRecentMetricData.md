---
title: "getLiveGuestRecentMetricData"
description: "Query a virtualization platform directly to retrieve recent metric data for a guest."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Host"
---
# SoftLayer_Virtual_Host::getLiveGuestRecentMetricData
## Overview 
Query a virtualization platform directly to retrieve recent metric data for a guest. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|uuid| string| The Universally Unique Identifier for the guest to fetch|
|time| integer| Start time|
|limit| integer| Number of data points to return|
|interval| integer| Data point stepping|


### Required Headers
* authenticate
* SoftLayer_Virtual_HostInitParameters

### Optional Headers
* SoftLayer_Virtual_HostObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object[] </a>
