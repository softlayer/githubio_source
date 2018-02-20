---
title: "removePrivateSubnetFromNetworkTunnel"
description: "Disassociate a private subnet from a network tunnel.  When a private subnet is disassociated, the customer (remote) subn... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# SoftLayer_Network_Tunnel_Module_Context::removePrivateSubnetFromNetworkTunnel
## Overview 
Disassociate a private subnet from a network tunnel.  When a private subnet is disassociated, the customer (remote) subnet on the other end of the tunnel will not able to communicate with the private subnet that was just disassociated. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the disassociation described above to take effect. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnetId| integer| The internal identifier of the private subnet to remove.|


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters

### Optional Headers

### Return Values
boolean
