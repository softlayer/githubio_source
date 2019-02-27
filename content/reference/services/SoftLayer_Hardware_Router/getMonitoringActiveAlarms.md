---
title: "getMonitoringActiveAlarms"
description: "Returns open monitoring alarms for a given time period"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
aliases:
    - "/reference/services/softlayer_hardware_router/getMonitoringActiveAlarms"
---
# [SoftLayer_Hardware_Router](/reference/services/SoftLayer_Hardware_Router)::getMonitoringActiveAlarms

Returns open monitoring alarms for a given time period


## Overview 
Returns open monitoring alarms for a given time period 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| |
|endDate| dateTime| |


### Required Headers
* authenticate
* SoftLayer_Hardware_RouterInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Monitoring_Alarm_History'>SoftLayer_Container_Monitoring_Alarm_History[] </a>



### Error Handling

* SoftLayer_Exception 

> "Monitoring service is not enabled on [domain name]. 



