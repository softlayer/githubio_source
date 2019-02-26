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
aliases:
    - "/reference/services/softlayer_network_tunnel_module_context/addPrivateSubnetToNetworkTunnel"
---
# [SoftLayer_Network_Tunnel_Module_Context](/reference/services/SoftLayer_Network_Tunnel_Module_Context)::addPrivateSubnetToNetworkTunnel

Associate a private subnet to a network tunnel.


## Overview 
Associates a private subnet to the network tunnel.  When a private subnet is associated, the network tunnel will allow the customer (remote) network to access the private subnet. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the association described above to take effect. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|subnetId| integer| The internal identifier of the private subnet to add.|


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Network_Tunnel_Module_Context::addCustomerSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addCustomerSubnetToNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::addServiceSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addServiceSubnetToNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::removePrivateSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removePrivateSubnetFromNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::removeCustomerSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeCustomerSubnetFromNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::removeServiceSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeServiceSubnetFromNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::applyConfigurationsToDevice](/reference/services/SoftLayer_Network_Tunnel_Module_Context/applyConfigurationsToDevice )




