---
title: "getPrivateNetworkGateways"
description: "Retrieve the gateways this VLAN is the private VLAN of."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
---
# SoftLayer_Network_Vlan::getPrivateNetworkGateways
## Overview 
Retrieve the gateways this VLAN is the private VLAN of.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_VlanInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_VlanObjectMask
* SoftLayer_Network_VlanObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway[] </a>

