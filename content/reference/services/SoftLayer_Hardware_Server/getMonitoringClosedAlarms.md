---
title: "getMonitoringClosedAlarms"
description: "Returns closed monitoring alarms for a given time period"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getMonitoringClosedAlarms"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getMonitoringClosedAlarms

Returns closed monitoring alarms for a given time period


## Overview 
Returns closed monitoring alarms for a given time period 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| |
|endDate| dateTime| |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Monitoring_Alarm_History'>SoftLayer_Container_Monitoring_Alarm_History[] </a>

