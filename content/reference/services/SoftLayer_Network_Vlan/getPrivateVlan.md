---
title: "getPrivateVlan"
description: "Retrieve a VLAN's associated private network VLAN. getPrivateVlan gathers it's information by retrieving the private VLA... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getPrivateVlan

Retrieve a VLAN's associated private network VLAN.


## Overview 
Retrieve a VLAN's associated private network VLAN. getPrivateVlan gathers it's information by retrieving the private VLAN of a VLAN's primary hardware object. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_VlanInitParameters

### Optional Headers
* SoftLayer_Network_VlanObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>

