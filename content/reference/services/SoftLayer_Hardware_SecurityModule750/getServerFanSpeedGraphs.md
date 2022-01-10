---
title: "getServerFanSpeedGraphs"
description: "Retrieve the server's fan speeds and displays them using tachometer graphs.  Data used to construct graphs is retrieved... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getServerFanSpeedGraphs"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getServerFanSpeedGraphs


Retrieve server's fan speed graphs.


## Overview 
Retrieve the server's fan speeds and displays them using tachometer graphs.  Data used to construct graphs is retrieved from the server's remote management card.  All graphs returned will have a title associated with it. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_Graphs_SensorSpeed'>SoftLayer_Container_RemoteManagement_Graphs_SensorSpeed[] </a>




