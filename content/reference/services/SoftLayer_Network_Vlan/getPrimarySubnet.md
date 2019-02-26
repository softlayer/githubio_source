---
title: "getPrimarySubnet"
description: "Retrieve a VLAN's primary subnet. Each VLAN has at least one subnet, usually the subnet that is assigned to a server or... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/getPrimarySubnet"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getPrimarySubnet

Retrieve a VLAN's primary subnet. Each VLAN has at least one subnet, usually the subnet that is assigned to a server or new IP address block when it's purchased.


## Overview 
Retrieve a VLAN's primary subnet. Each VLAN has at least one subnet, usually the subnet that is assigned to a server or new IP address block when it's purchased.

-----

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
* <a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>




