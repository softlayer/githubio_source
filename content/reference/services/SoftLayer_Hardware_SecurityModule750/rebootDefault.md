---
title: "rebootDefault"
description: "Attempts to reboot the server by issuing a reset (soft reboot) command to the server's remote management card. If the re... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/rebootDefault"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::rebootDefault

Reboot the server via the default method.


## Overview 
Attempts to reboot the server by issuing a reset (soft reboot) command to the server's remote management card. If the reset (soft reboot) attempt is unsuccessful, a power cycle command will be issued via the powerstrip. The power cycle command is equivalent to unplugging the server from the powerstrip and then plugging the server back into the powerstrip.  If a reboot command has been issued successfully in the past 20 minutes, another remote management command (rebootSoft, rebootHard, powerOn, powerOff and powerCycle) will not be allowed.  This is to avoid any type of server failures. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Return Values
* boolean




