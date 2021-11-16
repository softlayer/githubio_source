---
title: "getFrontendOutgoingBandwidth"
description: "The '''getFrontendOutgoingBandwidth''' method retrieves the amount of outgoing public network traffic used by a server b... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getFrontendOutgoingBandwidth"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getFrontendOutgoingBandwidth


Retrieve the amount of outgoing public network bandwidth used by a server over a period of time. 


## Overview 
The '''getFrontendOutgoingBandwidth''' method retrieves the amount of outgoing public network traffic used by a server between the given start and end date parameters. The ''dateTime'' parameter requires only the day, month and year to be entered - the time (hour, minute and second) are set to midnight be default in order to gather the data for the entire start and end date indicated in the parameter. The amount of bandwidth retrieved is measured in gigabytes (GB). 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| The start date for the range of bandwidth to retrieve.|
|endDate| dateTime| The end date for the range of bandwidth to retrieve.|


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters


### Return Values
* float



### Error Handling

* SoftLayer_Exception_Public 

> <<< EOT 

* SoftLayer_Exception_Public 

> <<< EOT 



