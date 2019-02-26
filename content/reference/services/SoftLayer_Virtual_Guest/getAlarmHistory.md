---
title: "getAlarmHistory"
description: "Returns monitoring alarm detailed history"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getAlarmHistory"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getAlarmHistory

Returns monitoring alarm detailed history


## Overview 
Returns monitoring alarm detailed history 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| |
|endDate| dateTime| |
|alarmId| string| |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Monitoring_Alarm_History'>SoftLayer_Container_Monitoring_Alarm_History[] </a>




