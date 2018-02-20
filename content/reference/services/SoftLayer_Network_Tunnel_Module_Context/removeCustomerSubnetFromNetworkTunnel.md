---
title: "removeCustomerSubnetFromNetworkTunnel"
description: "Disassociate a customer subnet (remote) from a network tunnel.  When a remote subnet is disassociated, that subnet will... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# SoftLayer_Network_Tunnel_Module_Context::removeCustomerSubnetFromNetworkTunnel
## Overview 
Disassociate a customer subnet (remote) from a network tunnel.  When a remote subnet is disassociated, that subnet will not able to communicate with private and service subnets on the SoftLayer network. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the disassociation described above to take effect. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnetId| integer| The internal identifier of the customer subnet (remote) to remove.|


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters

### Optional Headers

### Return Values
boolean
