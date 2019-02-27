---
title: "getGraphData"
description: "This method returns the metric data for each of the configuration values provided during the given time range."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/getGraphData"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::getGraphData

This method returns the metric data for each of the configuration values provided during the given time range.


## Overview 
This method returns the metric data for each of the configuration values provided during the given time range. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|metricDataTypes| <a href='/reference/datatypes/SoftLayer_Container_Metric_Data_Type'>SoftLayer_Container_Metric_Data_Type[] </a>| Array of metric data types|
|startDate| dateTime| The start date for the range of metric data to retrieve, must be in GMT.|
|endDate| dateTime| The end date for the range of metric data to retrieve, must be in GMT.|


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>


### Associated Methods

*  [SoftLayer_Monitoring_Agent_Configuration_Value::getMetricDataType](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Value/getMetricDataType )



### Error Handling

* SoftLayer_Exception_Public 

> Throws 'Please provide metric data types.' if no metric data types were provided. 

* SoftLayer_Exception_Public 

> Throws 'Please provide a start date.' if a start date is not provided. 

* SoftLayer_Exception_Public 

> Throws 'Please provide a end date.' if a end date is not provided. 

* SoftLayer_Exception_Public 

> Throws 'Failed to obtain metric data. Please contact development.' if a end date is not provided. 



