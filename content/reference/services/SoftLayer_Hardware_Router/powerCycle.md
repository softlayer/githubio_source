---
title: "powerCycle"
description: "The '''powerCycle''' method completes a power off and power on of the server successively in one command. The power cycl... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
---
# SoftLayer_Hardware_Router::powerCycle
## Overview 
The '''powerCycle''' method completes a power off and power on of the server successively in one command. The power cycle command is equivalent to unplugging the server from the power strip and then plugging the server back in. '''This method should only be used when all other options have been exhausted'''. Additional remote management commands may not be executed if this command was successfully issued within the last 20 minutes to avoid server failure. Remote management commands include: 

rebootSoft rebootHard powerOn powerOff powerCycle 



### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_RouterInitParameters

### Optional Headers

### Return Values
boolean

