---
title: "getDiskUsageMetricDataFromLegacyByDate"
description: "Retrieve disk usage data on a [[SoftLayer_Virtual_Guest|Cloud Computing Instance]] image for the time range you provide... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::getDiskUsageMetricDataFromLegacyByDate
## Overview 
Retrieve disk usage data on a [[SoftLayer_Virtual_Guest|Cloud Computing Instance]] image for the time range you provide from the Legacy Data Warehouse.  Each data entry objects contain ''dateTime'' and ''counter'' properties. ''dateTime'' property indicates the time that the disk usage data was measured and ''counter'' property holds the disk usage in bytes. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| datetime of the start date of the graph|
|endDateTime| dateTime| datetime of the ending date of the graph|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>

