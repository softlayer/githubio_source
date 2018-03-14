---
title: "getVlanForIpAddress"
description: "Retrieve the VLAN associated with an IP address via the IP's associated subnet."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/getVlanForIpAddress"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getVlanForIpAddress

Retrieve an IP addresses's associated VLAN.


## Overview 
Retrieve the VLAN associated with an IP address via the IP's associated subnet. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| The IP address to search for.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_VlanObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>


### associatedMethods

*  [SoftLayer_Network_Vlan::getPrivateVlanByIpAddress](/reference/services/SoftLayer_Network_Vlan/getPrivateVlanByIpAddress )

