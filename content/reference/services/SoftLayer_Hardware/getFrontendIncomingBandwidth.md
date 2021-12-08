---
title: "getFrontendIncomingBandwidth"
description: "The '''getFrontendIncomingBandwidth''' method retrieves the amount of incoming public network traffic used by a server b... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
aliases:
    - "/reference/services/softlayer_hardware/getFrontendIncomingBandwidth"
---
# [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware)::getFrontendIncomingBandwidth


Retrieve the amount of incoming public network bandwidth used by a server over a period of time. 


## Overview 
The '''getFrontendIncomingBandwidth''' method retrieves the amount of incoming public network traffic used by a server between the given start and end date parameters. When entering the ''dateTime'' parameter, only the month, day and year of the start and end dates are required - the time (hour, minute and second) are set to midnight by default and cannot be changed. The amount of bandwidth retrieved is measured in gigabytes (GB). 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| The start date for the range of bandwidth to retrieve.|
|endDate| dateTime| The end date for the range of bandwidth to retrieve.|


### Required Headers
* authenticate
* SoftLayer_HardwareInitParameters


### Return Values
* float



### Error Handling

* SoftLayer_Exception_Public 

> <<< EOT 

* SoftLayer_Exception_Public 

> <<< EOT 



