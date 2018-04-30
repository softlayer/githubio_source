---
title: "getServerPowerState"
description: "The '''getPowerState''' method retrieves the power state for the selected server. The server's power status is retrieved... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
aliases:
    - "/reference/services/softlayer_hardware/getServerPowerState"
---
# [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware)::getServerPowerState

Retrieves a server's power state.


## Overview 
The '''getPowerState''' method retrieves the power state for the selected server. The server's power status is retrieved from its remote management card. This method returns "on", for a server that has been powered on, or "off" for servers powered off. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_HardwareInitParameters

### Optional Headers

### Return Values
string

