---
title: "getPrivateVlanByIpAddress"
description: "Retrieve the private network VLAN associated with an IP address."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/getPrivateVlanByIpAddress"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getPrivateVlanByIpAddress

Retrieve the private network VLAN associated with an IP address.


## Overview 
Retrieve the private network VLAN associated with an IP address. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| The IPv4 address to search for|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_VlanObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>


### associatedMethods

*  [SoftLayer_Network_Vlan::getVlanForIpAddress](/reference/services/SoftLayer_Network_Vlan/getVlanForIpAddress )

