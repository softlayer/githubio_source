---
title: "getDailyAverage"
description: "The '''getDailyAverage''' method calculates the average daily network traffic used by the selected server. Using the req... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
---
# SoftLayer_Hardware_SecurityModule::getDailyAverage
## Overview 
The '''getDailyAverage''' method calculates the average daily network traffic used by the selected server. Using the required parameter ''dateTime'' to enter a start and end date, the user retrieves this average, measure in gigabytes (GB) for the specified date range. When entering parameters, only the month, day and year are required - time entries are omitted as this method defaults the time to midnight in order to account for the entire day. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| The start date for the range of bandwidth a customer wishes to view.|
|endDate| dateTime| The end date for the range of bandwidth a customer wishes to view.|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers

### Return Values
float

