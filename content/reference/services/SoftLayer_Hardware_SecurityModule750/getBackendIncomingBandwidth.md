---
title: "getBackendIncomingBandwidth"
description: "The '''getBackendIncomingBandwidth''' method retrieves the amount of incoming private network traffic used between the g... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getBackendIncomingBandwidth"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getBackendIncomingBandwidth


Retrieve the amount of incoming private network bandwidth used by a server over a period of time. 


## Overview 
The '''getBackendIncomingBandwidth''' method retrieves the amount of incoming private network traffic used between the given start date and end date parameters. When entering start and end dates, only the month, day and year are used to calculate bandwidth totals - the time (HH:MM:SS) is ignored and defaults to midnight. The amount of bandwidth retrieved is measured in gigabytes. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| The start date for the range of bandwidth to retrieve.|
|endDate| dateTime| The end date for the range of bandwidth to retrieve.|


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* float



### Error Handling

* SoftLayer_Exception_Public 

> "Please provide a start date." 

* SoftLayer_Exception_Public 

> "Please provide an end date." 



