---
title: "getRecentCommands"
description: "Retrieve the last five reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) commands i... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
---
# SoftLayer_Network_Component::getRecentCommands
## Overview 
Retrieve the last five reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) commands issued to the server's remote management card.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_ComponentInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_ComponentObjectMask
* SoftLayer_Network_ComponentObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request[] </a>

