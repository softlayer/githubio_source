---
title: "getSensorDataWithGraphs"
description: "The '''getSensorDataWithGraphs''' method retrieves the raw data returned from the server's remote management card. Along... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
---
# SoftLayer_Hardware::getSensorDataWithGraphs
## Overview 
The '''getSensorDataWithGraphs''' method retrieves the raw data returned from the server's remote management card. Along with raw data, graphs for the CPU and system temperatures and fan speeds are also returned. For more details on what information is returned, refer to the ''getSensorData'' method. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_HardwareInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs'>SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs </a>

