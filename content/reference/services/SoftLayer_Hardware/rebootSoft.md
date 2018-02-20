---
title: "rebootSoft"
description: "The '''rebootSoft''' method reboots the server by issuing a reset command to the server's remote management card via sof... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
---
# SoftLayer_Hardware::rebootSoft
## Overview 
The '''rebootSoft''' method reboots the server by issuing a reset command to the server's remote management card via soft reboot. When executing a soft reboot, servers allow all processes to shut down completely before rebooting. Remote management commands are unable to be issued within 20 minutes of issuing a successful soft reboot in order to avoid server failure. Remote management commands include: 

rebootSoft rebootHard powerOn powerOff powerCycle 



### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_HardwareInitParameters

### Optional Headers

### Return Values
boolean
