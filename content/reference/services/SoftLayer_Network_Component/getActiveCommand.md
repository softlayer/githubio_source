---
title: "getActiveCommand"
description: "Retrieve reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) command currently execut... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
aliases:
    - "/reference/services/softlayer_network_component/getActiveCommand"
---
# [SoftLayer_Network_Component](/reference/services/SoftLayer_Network_Component)::getActiveCommand


Retrieve reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) command currently executing by the server's remote management card.


## Overview 
Retrieve reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) command currently executing by the server's remote management card.

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_ComponentInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_ComponentObjectMask
* SoftLayer_Network_ComponentObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request </a>




