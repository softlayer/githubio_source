---
title: "bootToRescueLayer"
description: "The Rescue Kernel is designed to provide you with the ability to bring a server online in order to troubleshoot system p... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/bootToRescueLayer"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::bootToRescueLayer

Initiates the Rescue Kernel to bring a server online to troubleshoot system problems.


## Overview 
The Rescue Kernel is designed to provide you with the ability to bring a server online in order to troubleshoot system problems that would normally only be resolved by an OS Reload. The correct Rescue Kernel will be selected based upon the currently installed operating system. When the rescue kernel process is initiated, the server will shutdown and reboot on to the public network with the same IP's assigned to the server to allow for remote connections. It will bring your server offline for approximately 10 minutes while the rescue is in progress. The root/administrator password will be the same as what is listed in the portal for the server. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|noOsBootEnvironment| string| Optionally specify which rescue environment to boot into (currently accepts LINUX or WINDOWS). Only applies to No-OS Servers. Defaults to LINUX.|


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'You do not have permission to this service.' when a user does not have permission to Issue OS Reloads. 

* SoftLayer_Exception_Public 

> Throws the exception 'There is currently an outstanding transaction for this server.' when there is a current hardware update. 



