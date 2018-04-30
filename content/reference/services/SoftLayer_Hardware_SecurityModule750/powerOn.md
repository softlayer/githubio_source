---
title: "powerOn"
description: "Power on server via its remote management card.  If a reboot command has been issued successfully in the past 20 minutes... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/powerOn"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::powerOn

Power on server.


## Overview 
Power on server via its remote management card.  If a reboot command has been issued successfully in the past 20 minutes, another remote management command (rebootSoft, rebootHard, powerOn, powerOff and powerCycle) will not be allowed.  This is to avoid any type of server failures. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters

### Optional Headers

### Return Values
boolean

