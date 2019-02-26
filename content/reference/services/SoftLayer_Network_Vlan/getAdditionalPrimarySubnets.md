---
title: "getAdditionalPrimarySubnets"
description: "Retrieve a VLAN's additional primary subnets. These are used to extend the number of servers attached to the VLAN by add... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/getAdditionalPrimarySubnets"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getAdditionalPrimarySubnets

Retrieve a VLAN's additional primary subnets. These are used to extend the number of servers attached to the VLAN by adding more ip addresses to the primary IP address pool.


## Overview 
Retrieve a VLAN's additional primary subnets. These are used to extend the number of servers attached to the VLAN by adding more ip addresses to the primary IP address pool.

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
* resultLimit
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>




