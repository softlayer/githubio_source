---
title: "getPMInfo"
description: "Retrieve a server's hardware state via its internal sensors. Remote sensor data is transmitted to the SoftLayer API by w... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getPMInfo"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getPMInfo


Retrieve a server's hardware state via its internal sensors.


## Overview 
Retrieve a server's hardware state via its internal sensors. Remote sensor data is transmitted to the SoftLayer API by way of the server's remote management card. Sensor data measures system temperatures, voltages, and other local server settings. Sensor data is cached for 30 seconds. Calls made to getSensorData for the same server within 30 seconds of each other will return the same data. Subsequent calls will return new data once the cache expires. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_PmInfo'>SoftLayer_Container_RemoteManagement_PmInfo[] </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to locate the management component for this server." if the API is unable to locate the server's remote management component. 



