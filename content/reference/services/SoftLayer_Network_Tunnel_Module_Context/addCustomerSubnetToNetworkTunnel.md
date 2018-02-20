---
title: "addCustomerSubnetToNetworkTunnel"
description: "Associates a remote subnet to the network tunnel.  When a remote subnet is associated, a network tunnel will allow the c... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# SoftLayer_Network_Tunnel_Module_Context::addCustomerSubnetToNetworkTunnel
## Overview 
Associates a remote subnet to the network tunnel.  When a remote subnet is associated, a network tunnel will allow the customer (remote) network to communicate with the private and service subnets on the SoftLayer network which are on the other end of this network tunnel. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the association described above to take effect. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnetId| integer| The internal identifier of the customer (remote) subnet to add.|


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters

### Optional Headers

### Return Values
boolean
