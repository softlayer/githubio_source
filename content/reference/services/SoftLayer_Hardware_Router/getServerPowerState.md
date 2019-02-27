---
title: "getServerPowerState"
description: "The '''getPowerState''' method retrieves the power state for the selected server. The server's power status is retrieved... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
aliases:
    - "/reference/services/softlayer_hardware_router/getServerPowerState"
---
# [SoftLayer_Hardware_Router](/reference/services/SoftLayer_Hardware_Router)::getServerPowerState

Retrieves a server's power state.


## Overview 
The '''getPowerState''' method retrieves the power state for the selected server. The server's power status is retrieved from its remote management card. This method returns "on", for a server that has been powered on, or "off" for servers powered off. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_RouterInitParameters


### Return Values
* string



### Error Handling

* SoftLayer_Exception 

> "Method has not been implemented for this object type." 



