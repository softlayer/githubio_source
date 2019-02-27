---
title: "powerCycle"
description: "Power off then power on the server via powerstrip.  The power cycle command is equivalent to unplugging the server from... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/powerCycle"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::powerCycle

Issues power cycle to server.


## Overview 
Power off then power on the server via powerstrip.  The power cycle command is equivalent to unplugging the server from the powerstrip and then plugging the server back into the powerstrip.  This should only be used as a last resort.  If a reboot command has been issued successfully in the past 20 minutes, another remote management command (rebootSoft, rebootHard, powerOn, powerOff and powerCycle) will not be allowed. This is to avoid any type of server failures. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters


### Return Values
* boolean




