---
title: "removeServiceSubnetFromNetworkTunnel"
description: "Disassociate a service subnet from a network tunnel.  When a service subnet is disassociated, that customer (remote) sub... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# SoftLayer_Network_Tunnel_Module_Context::removeServiceSubnetFromNetworkTunnel
## Overview 
Disassociate a service subnet from a network tunnel.  When a service subnet is disassociated, that customer (remote) subnet on the other end of the network tunnel will not able to communicate with that service subnet on the SoftLayer network. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the disassociation described above to take effect. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnetId| integer| The internal identifier of the service subnet to remove.|


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network_Tunnel_Module_Context::addPrivateSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addPrivateSubnetToNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::addCustomerSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addCustomerSubnetToNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::addServiceSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addServiceSubnetFromNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::removePrivateSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removePrivateSubnetFromNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::removeServiceSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeServiceSubnetFromNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::applyConfigurationsToDevice](/reference/services/SoftLayer_Network_Tunnel_Module_Context/applyConfigurationsToDevice )

