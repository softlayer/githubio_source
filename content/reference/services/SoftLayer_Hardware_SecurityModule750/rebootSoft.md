---
title: "rebootSoft"
description: "Reboot the server by issuing a reset command to the server's remote management card.  This is a graceful reboot. The ser... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/rebootSoft"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::rebootSoft


Reboot the server via gracefully (soft reboot).


## Overview 
Reboot the server by issuing a reset command to the server's remote management card.  This is a graceful reboot. The servers will allow all process to shutdown gracefully before rebooting.  If a reboot command has been issued successfully in the past 20 minutes, another remote management command (rebootSoft, rebootHard, powerOn, powerOff and powerCycle) will not be allowed.  This is to avoid any type of server failures. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* boolean




