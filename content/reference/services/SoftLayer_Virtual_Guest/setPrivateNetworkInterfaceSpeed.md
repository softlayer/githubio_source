---
title: "setPrivateNetworkInterfaceSpeed"
description: "Sets the private network interface speed to the new speed. Speed values can only be 0 (Disconnect), 10, 100, or 1000. Th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::setPrivateNetworkInterfaceSpeed
## Overview 
Sets the private network interface speed to the new speed. Speed values can only be 0 (Disconnect), 10, 100, or 1000. The new speed must be equal to or less than the max speed of the interface. 

It will take less than a minute to update the port speed. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newSpeed| integer| New speed for private network component|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers

### Return Values
boolean
