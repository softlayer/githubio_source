---
title: "rebootHard"
description: "The '''rebootHard''' method reboots the server by issuing a cycle command to the server's remote management card. A hard... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware"
aliases:
    - "/reference/services/softlayer_hardware/rebootHard"
---
# [SoftLayer_Hardware](/reference/services/SoftLayer_Hardware)::rebootHard


Reboot the server via "hard" reboot.


## Overview 
The '''rebootHard''' method reboots the server by issuing a cycle command to the server's remote management card. A hard reboot is equivalent to pressing the ''Reset'' button on a server - it is issued immediately and will not allow processes to shut down prior to the reboot. Completing a hard reboot may initiate system disk checks upon server reboot, causing the boot up to take longer than normally expected. 

Remote management commands are unable to be executed if a reboot has been issued successfully within the last 20 minutes to avoid server failure. Remote management commands include: 

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



