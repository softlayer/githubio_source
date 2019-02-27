---
title: "getAverageUsageMetricDataByDate"
description: "Returns the average disk space usage for a storage repository."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Storage_Repository"
aliases:
    - "/reference/services/softlayer_virtual_storage_repository/getAverageUsageMetricDataByDate"
---
# [SoftLayer_Virtual_Storage_Repository](/reference/services/SoftLayer_Virtual_Storage_Repository)::getAverageUsageMetricDataByDate

Returns the average disk usage for the timeframe based on the parameters provided. 


## Overview 
Returns the average disk space usage for a storage repository. 

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
* float




