---
title: "getBandwidthImageByDate"
description: "Use this method when needing a bandwidth image for a single guest.  It will gather the correct input parameters for the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getBandwidthImageByDate

Retrieve a visual representation of the amount of network traffic that occurred for the specified time frame for a computing instance. 


## Overview 
Use this method when needing a bandwidth image for a single guest.  It will gather the correct input parameters for the generic graphing utility based on the date ranges 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| datetime of the start date of the graph|
|endDateTime| dateTime| datetime of the ending date of the graph|
|networkType| string| type of the graph, either "public" or "private"|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs'>SoftLayer_Container_Bandwidth_GraphOutputs </a>

