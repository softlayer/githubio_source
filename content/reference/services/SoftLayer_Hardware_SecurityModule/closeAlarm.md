---
title: "closeAlarm"
description: "Returns monitoring alarm detailed history"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/closeAlarm"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::closeAlarm

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
* SoftLayer_Hardware_SecurityModuleInitParameters


### Optional Headers
* resultLimit

### Return Values
* boolean



### Error Handling

* SoftLayer_Exception 

> "Monitoring service is not enabled on [domain name]." 



