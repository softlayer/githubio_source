---
title: "rebootHard"
description: "Reboot the server by issuing a cycle command to the server's remote management card.  This is equivalent to pressing the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/rebootHard"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::rebootHard

Reboot the server via "hard" reboot.


## Overview 
Reboot the server by issuing a cycle command to the server's remote management card.  This is equivalent to pressing the 'Reset' button on the server.  This command is issued immediately and will not wait for processes to shutdown. After this command is issued, the server may take a few moments to boot up as server may run system disks checks. If a reboot command has been issued successfully in the past 20 minutes, another remote management command (rebootSoft, rebootHard, powerOn, powerOff and powerCycle) will not be allowed.  This is to avoid any type of server failures. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters

### Optional Headers

### Return Values
boolean

