---
title: "getBandwidthTotal"
description: "Returns the total amount of bandwidth used during the time specified for a computing instance."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::getBandwidthTotal
## Overview 
Returns the total amount of bandwidth used during the time specified for a computing instance. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDateTime| dateTime| timestamp of the starting date|
|endDateTime| dateTime| timestamp of the ending date|
|direction| string| either "IN", "OUT", or "BOTH" with BOTH being default|
|side| string| either "PUBLIC", "PRIVATE", or "BOTH" with PUBLIC being default|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers

### Return Values
unsigned long
