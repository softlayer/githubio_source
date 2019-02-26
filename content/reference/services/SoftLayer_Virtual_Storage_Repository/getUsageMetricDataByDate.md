---
title: "getUsageMetricDataByDate"
description: "Retrieve disk usage data on a [[SoftLayer_Virtual_Guest|Cloud Computing Instance]] image for the time range you provide.... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Storage_Repository"
aliases:
    - "/reference/services/softlayer_virtual_storage_repository/getUsageMetricDataByDate"
---
# [SoftLayer_Virtual_Storage_Repository](/reference/services/SoftLayer_Virtual_Storage_Repository)::getUsageMetricDataByDate

Retrieve the metric data for disk space usage for a storage repository. 


## Overview 
Retrieve disk usage data on a [[SoftLayer_Virtual_Guest|Cloud Computing Instance]] image for the time range you provide.  Each data entry objects contain ''dateTime'' and ''counter'' properties. ''dateTime'' property indicates the time that the disk usage data was measured and ''counter'' property holds the disk usage in bytes. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| datetime of the start date of the graph|
|endDateTime| dateTime| datetime of the ending date of the graph|


### Required Headers
* authenticate
* SoftLayer_Virtual_Storage_RepositoryInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>




