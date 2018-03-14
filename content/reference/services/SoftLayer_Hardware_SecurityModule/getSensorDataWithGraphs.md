---
title: "getSensorDataWithGraphs"
description: "Retrieves the raw data returned from the server's remote management card.  For more details of what is returned please r... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getSensorDataWithGraphs"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getSensorDataWithGraphs

Retrieve server's temperature and fan speed graphs as well the sensor raw data.


## Overview 
Retrieves the raw data returned from the server's remote management card.  For more details of what is returned please refer to the getSensorData method.  Along with the raw data, graphs for the cpu and system temperatures and fan speeds are also returned. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs'>SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs </a>

