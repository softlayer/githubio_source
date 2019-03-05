---
title: "getSummaryData"
description: ""
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Hub_Swift_Metrics"
aliases:
    - "/reference/services/softlayer_network_storage_hub_swift_metrics/getSummaryData"
---
# [SoftLayer_Network_Storage_Hub_Swift_Metrics](/reference/services/SoftLayer_Network_Storage_Hub_Swift_Metrics)::getSummaryData




## Overview 


-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| |
|endDateTime| dateTime| |
|validTypes| <a href='/reference/datatypes/SoftLayer_Container_Metric_Data_Type'>SoftLayer_Container_Metric_Data_Type[] </a>| |
|summaryPeriod| integer| 300, 600, 1800, 3600, 43200 or 86400 seconds|


### Required Headers
* authenticate
* SoftLayer_Network_Storage_Hub_Swift_MetricsInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>




