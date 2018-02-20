---
title: "addPrivateSubnetToNetworkTunnel"
description: "Associates a private subnet to the network tunnel.  When a private subnet is associated, the network tunnel will allow t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# SoftLayer_Network_Tunnel_Module_Context::addPrivateSubnetToNetworkTunnel
## Overview 
Associates a private subnet to the network tunnel.  When a private subnet is associated, the network tunnel will allow the customer (remote) network to access the private subnet. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the association described above to take effect. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnetId| integer| The internal identifier of the private subnet to add.|


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters

### Optional Headers

### Return Values
boolean
