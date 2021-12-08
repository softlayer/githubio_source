---
title: "getNetworkComponentsTrunkable"
description: "Retrieve the viable trunking targets of this VLAN. Viable targets include accessible components of assigned hardware in... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/getNetworkComponentsTrunkable"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getNetworkComponentsTrunkable


Retrieve the viable trunking targets of this VLAN. Viable targets include accessible components of assigned hardware in the same pod and network as this VLAN, which are not already natively attached nor trunked.


## Overview 
Retrieve the viable trunking targets of this VLAN. Viable targets include accessible components of assigned hardware in the same pod and network as this VLAN, which are not already natively attached nor trunked.

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
* <a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>




