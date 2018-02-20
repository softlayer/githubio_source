---
title: "getFirewallProtectableSubnets"
description: "Get the subnets associated with this CloudLayer computing instance that are protectable by a network component firewall."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::getFirewallProtectableSubnets
## Overview 
Get the subnets associated with this CloudLayer computing instance that are protectable by a network component firewall. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>
