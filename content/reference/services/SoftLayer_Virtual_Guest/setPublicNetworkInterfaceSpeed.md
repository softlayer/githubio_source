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
aliases:
    - "/reference/services/softlayer_virtual_guest/setPublicNetworkInterfaceSpeed"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::setPublicNetworkInterfaceSpeed

Updates the public network interface (eth1) speed.


## Overview 
Sets the public network interface speed to the new speed. Speed values can only be 0 (Disconnect), 10, 100, or 1000. The new speed must be equal to or less than the max speed of the interface. 

It will take less than a minute to update the port speed. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newSpeed| integer| New speed for public network component|


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throws the exception 'Speed cannot be null and must be 0 (Disconnect), 10, or 100.' when the parameter being passed in is null. 

* SoftLayer_Exception_Public 

> Throws the exception 'You do not have permission to this service.' when a user does not have permission to Manage Port Control. 

* SoftLayer_Exception_Public 

> Throws the exception 'There is currently an outstanding transaction for this server.' when there is a current hardware update. 

* SoftLayer_Exception_Public 

> Throws the exception 'Speed must be 0 (Disconnect), 10, 100, or 1000.' when the speed being passed in is not in the list of accepted speeds. 

* SoftLayer_Exception_Public 

> Throws the exception 'You cannot set interface speed greater than max speed.' when the new speed is greater than the current max speed of the public interface. 



