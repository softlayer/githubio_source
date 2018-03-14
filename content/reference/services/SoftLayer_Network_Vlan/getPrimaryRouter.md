---
title: "getPrimaryRouter"
description: "Retrieve the primary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router fo... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/getPrimaryRouter"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getPrimaryRouter

Retrieve the primary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy.


## Overview 
Retrieve the primary router that a VLAN is associated with. Every SoftLayer VLAN is connected to more than one router for greater network redundancy.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_VlanInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_VlanObjectMask
* SoftLayer_Network_VlanObjectFilter
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Hardware_Router'>SoftLayer_Hardware_Router </a>

