---
title: "rebootDefault"
description: "The '''rebootDefault''' method attempts to reboot the server by issuing a soft reboot, or reset, command to the server's... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
aliases:
    - "/reference/services/softlayer_hardware/rebootDefault"
---
# [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware)::rebootDefault


Reboot the server via the default method.


## Overview 
The '''rebootDefault''' method attempts to reboot the server by issuing a soft reboot, or reset, command to the server's remote management card. if the reset attempt is unsuccessful, a power cycle command will be issued via the power strip. The power cycle command is equivalent to unplugging the server from the power strip and then plugging the server back in. If the reset was successful within the last 20 minutes, another remote management command cannot be completed to avoid server failure. Remote management commands include: 

rebootSoft rebootHard powerOn powerOff powerCycle 



-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_HardwareInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception 

> "Method has not been implemented for this object type." 



