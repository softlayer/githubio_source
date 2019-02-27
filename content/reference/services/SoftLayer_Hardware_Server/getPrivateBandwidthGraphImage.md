---
title: "getPrivateBandwidthGraphImage"
description: "Retrieve a graph of a server's private network bandwidth usage over the specified time frame. If no time frame is specif... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getPrivateBandwidthGraphImage"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getPrivateBandwidthGraphImage

Retrieve a graph of a server's private network usage.


## Overview 
Retrieve a graph of a server's private network bandwidth usage over the specified time frame. If no time frame is specified then getPublicBandwidthGraphImage retrieves the last 24 hours of public bandwidth usage. getPublicBandwidthGraphImage returns a PNG image 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startTime| string| The starting point to retrieve bandwidth data from, specified as a [[dateTime|date]].|
|endTime| string| The end point to retrieve bandwidth data to, specified as a [[dateTime|date]].|


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters


### Return Values
* binary data

### External Links


* [Portable Network Graphics at Wikipedia](http://en.wikipedia.org/wiki/Portable_Network_Graphics)




### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to retrieve the public bandwidth graph for server {id}." if the API is unable to retrieve a valid PNG bandwidth graph image. 

* SoftLayer_Exception 

> Throw the exception "The start time {startTime} is not a readable date format." if an invalid start time is passed to getPublicBandwidthGraphImage. 

* SoftLayer_Exception 

> Throw the exception "The end time {endTime} is not a readable date format." if an invalid end time is passed to getPublicBandwidthGraphImage. 



