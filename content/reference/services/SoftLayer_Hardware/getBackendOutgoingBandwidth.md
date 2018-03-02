---
title: "getBackendOutgoingBandwidth"
description: "The '''getBackendOutgoingBandwidth''' method retrieves the amount of outgoing private network traffic used between the g... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
---
# SoftLayer_Hardware::getBackendOutgoingBandwidth
## Overview 
The '''getBackendOutgoingBandwidth''' method retrieves the amount of outgoing private network traffic used between the given start date and end date parameters. When entering start and end dates, only the month, day and year are used to calculate bandwidth totals - the time (HH:MM:SS) is ignored and defaults to midnight. The amount of bandwidth retrieved is measured in gigabytes. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| The start date for the range of bandwidth to retrieve.|
|endDate| dateTime| The end date for the range of bandwidth to retrieve.|


### Required Headers
* authenticate
* SoftLayer_HardwareInitParameters

### Optional Headers

### Return Values
float

