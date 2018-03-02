---
title: "powerOn"
description: "The '''powerOn''' method powers on a server via its remote management card. This boolean return value returns ''true'' u... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
---
# SoftLayer_Hardware_Router::powerOn
## Overview 
The '''powerOn''' method powers on a server via its remote management card. This boolean return value returns ''true'' upon successful execution and ''false'' if unsuccessful. Other remote management commands may not be issued in this command was successfully completed within the last 20 minutes to avoid server failure. Remote management commands include: 

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

