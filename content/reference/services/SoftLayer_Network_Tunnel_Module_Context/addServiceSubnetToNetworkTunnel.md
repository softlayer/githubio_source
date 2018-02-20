---
title: "addServiceSubnetToNetworkTunnel"
description: "Associates a service subnet to the network tunnel.  When a service subnet is associated, a network tunnel will allow the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# SoftLayer_Network_Tunnel_Module_Context::addServiceSubnetToNetworkTunnel
## Overview 
Associates a service subnet to the network tunnel.  When a service subnet is associated, a network tunnel will allow the customer (remote) network to communicate with the private and service subnets on the SoftLayer network which are on the other end of this network tunnel.  Service subnets provide access to SoftLayer services such as the customer management portal and the SoftLayer API. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the association described above to take effect. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnetId| integer| The internal identifier of the SoftLayer service subnet to add.|


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters

### Optional Headers

### Return Values
boolean
