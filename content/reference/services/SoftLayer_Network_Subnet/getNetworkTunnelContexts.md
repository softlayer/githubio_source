---
title: "getNetworkTunnelContexts"
description: "Retrieve iPSec network tunnels that have access to a private subnet."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
---
# SoftLayer_Network_Subnet::getNetworkTunnelContexts
## Overview 
Retrieve iPSec network tunnels that have access to a private subnet.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_SubnetInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_SubnetObjectMask
* SoftLayer_Network_SubnetObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context'>SoftLayer_Network_Tunnel_Module_Context[] </a>

