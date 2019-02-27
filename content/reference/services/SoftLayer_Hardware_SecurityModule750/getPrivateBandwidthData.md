---
title: "getPrivateBandwidthData"
description: "Retrieve a graph of a server's private network bandwidth usage over the specified timeframe. If no timeframe is specifie... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getPrivateBandwidthData"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getPrivateBandwidthData

Retrieve a graph of a server's private network usage.


## Overview 
Retrieve a graph of a server's private network bandwidth usage over the specified timeframe. If no timeframe is specified then getPublicBandwidthGraphImage retrieves the last 24 hours of public bandwidth usage. getPrivateBandwidthGraphImage returns a PNG image measuring 827 pixels by 293 pixels. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startTime| integer| The starting point to retrieve bandwidth data from, specified as a [[dateTime|date]].|
|endTime| integer| The end point to retrieve bandwidth data to, specified as a [[dateTime|date]].|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Data'>SoftLayer_Metric_Tracking_Object_Data[] </a>

### External Links


* [Portable Network Graphics at Wikipedia](http://en.wikipedia.org/wiki/Portable_Network_Graphics)




### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to retrieve the private bandwidth graph for server {id}." if the API is unable to retrieve a valid PNG bandwidth graph image. 

* SoftLayer_Exception 

> Throw the exception "The start time {startTime} is not a readable date format." if an invalid start time is passed to getPublicBandwidthGraphImage. 

* SoftLayer_Exception 

> Throw the exception "The end time {endTime} is not a readable date format." if an invalid end time is passed to getPublicBandwidthGraphImage. 



