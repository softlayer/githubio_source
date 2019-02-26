---
title: "getServerTemperatureGraphs"
description: "Retrieve the server's temperature and displays them using thermometer graphs.  Temperatures retrieved are CPU(s) and sys... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getServerTemperatureGraphs"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getServerTemperatureGraphs

Retrieve server's temperature graphs


## Overview 
Retrieve the server's temperature and displays them using thermometer graphs.  Temperatures retrieved are CPU(s) and system temperatures.  Data used to construct graphs is retrieved from the server's remote management card.  All graphs returned will have a title associated with it. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_Graphs_SensorTemperature'>SoftLayer_Container_RemoteManagement_Graphs_SensorTemperature[] </a>




