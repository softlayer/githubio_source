---
title: "closeAlarm"
description: "Returns monitoring alarm detailed history"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
aliases:
    - "/reference/services/softlayer_hardware/closeAlarm"
---
# [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware)::closeAlarm

Returns monitoring alarm detailed history


## Overview 
Returns monitoring alarm detailed history 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|alarmId| string| |


### Required Headers
* authenticate
* SoftLayer_HardwareInitParameters


### Optional Headers
* resultLimit

### Return Values
* boolean



### Error Handling

* SoftLayer_Exception 

> "Monitoring service is not enabled on [domain name]." 



