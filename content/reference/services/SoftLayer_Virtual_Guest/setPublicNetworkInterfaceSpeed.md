---
title: "setPublicNetworkInterfaceSpeed"
description: "Sets the public network interface speed to the new speed. Speed values can only be 0 (Disconnect), 10, 100, or 1000. The... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::setPublicNetworkInterfaceSpeed

Updates the public network interface (eth1) speed.


## Overview 
Sets the public network interface speed to the new speed. Speed values can only be 0 (Disconnect), 10, 100, or 1000. The new speed must be equal to or less than the max speed of the interface. 

It will take less than a minute to update the port speed. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newSpeed| integer| New speed for public network component|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers

### Return Values
boolean

