---
title: "getPublicBandwidthTotal"
description: "Retrieve the total number of bytes used by a server over a specified time period via the data warehouse tracking objects... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getPublicBandwidthTotal"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getPublicBandwidthTotal

Retrieve total number of public bytes used by a server over time period specified.


## Overview 
Retrieve the total number of bytes used by a server over a specified time period via the data warehouse tracking objects for this hardware. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startTime| integer| The starting point to retrieve bandwidth data from, specified as a [[dateTime|date]].|
|endTime| integer| The end point to retrieve bandwidth data to, specified as a [[dateTime|date]].|


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters

### Optional Headers

### Return Values
unsigned long

