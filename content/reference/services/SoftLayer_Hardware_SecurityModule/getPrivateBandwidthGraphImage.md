---
title: "getPrivateBandwidthGraphImage"
description: "Retrieve a graph of a server's private network bandwidth usage over the specified time frame. If no time frame is specif... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
---
# SoftLayer_Hardware_SecurityModule::getPrivateBandwidthGraphImage
## Overview 
Retrieve a graph of a server's private network bandwidth usage over the specified time frame. If no time frame is specified then getPublicBandwidthGraphImage retrieves the last 24 hours of public bandwidth usage. getPublicBandwidthGraphImage returns a PNG image 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startTime| string| The starting point to retrieve bandwidth data from, specified as a [[dateTime|date]].|
|endTime| string| The end point to retrieve bandwidth data to, specified as a [[dateTime|date]].|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers

### Return Values
binary data
