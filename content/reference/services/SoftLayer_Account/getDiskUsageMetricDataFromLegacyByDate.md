---
title: "getDiskUsageMetricDataFromLegacyByDate"
description: "Retrieve disk usage data on a [SoftLayer_Virtual_Guest]({{<ref 'reference/datatypes/SoftLayer_Virtual_Guest'>}}) image f... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getDiskUsageMetricDataFromLegacyByDate"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getDiskUsageMetricDataFromLegacyByDate

Retrieve the metric data for disk space usage for a storage repository from the Legacy Data Warehouse. 


## Overview 
Retrieve disk usage data on a [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}) image for the time range you provide from the Legacy Data Warehouse.  Each data entry objects contain ''dateTime'' and ''counter'' properties. ''dateTime'' property indicates the time that the disk usage data was measured and ''counter'' property holds the disk usage in bytes. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| datetime of the start date of the graph|
|endDateTime| dateTime| datetime of the ending date of the graph|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>




