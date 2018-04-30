---
title: "getPMInfo"
description: "Retrieve a server's hardware state via its internal sensors. Remote sensor data is transmitted to the SoftLayer API by w... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getPMInfo"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getPMInfo

Retrieve a server's hardware state via its internal sensors.


## Overview 
Retrieve a server's hardware state via its internal sensors. Remote sensor data is transmitted to the SoftLayer API by way of the server's remote management card. Sensor data measures system temperatures, voltages, and other local server settings. Sensor data is cached for 30 seconds. Calls made to getSensorData for the same server within 30 seconds of each other will return the same data. Subsequent calls will return new data once the cache expires. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_PmInfo'>SoftLayer_Container_RemoteManagement_PmInfo[] </a>

