---
title: "getServerTemperatureGraphs"
description: "The '''getServerTemperatureGraphs''' retrieves the server's temperatures and displays the various temperatures using the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
aliases:
    - "/reference/services/softlayer_hardware_router/getServerTemperatureGraphs"
---
# [SoftLayer_Hardware_Router](/reference/services/SoftLayer_Hardware_Router)::getServerTemperatureGraphs

Retrieve server's temperature graphs


## Overview 
The '''getServerTemperatureGraphs''' retrieves the server's temperatures and displays the various temperatures using thermometer graphs. Temperatures retrieved are CPU temperature(s) and system temperatures. Data used to construct the graphs is retrieved from the server's remote management card. All graphs returned will have an associated title. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_RouterInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_Graphs_SensorTemperature'>SoftLayer_Container_RemoteManagement_Graphs_SensorTemperature[] </a>



### Error Handling

* SoftLayer_Exception 

> "Method has not been implemented for this object type." 



