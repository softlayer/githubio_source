---
title: "applyConfigurationsToDevice"
description: "An asynchronous task will be created to apply the IPSec network tunnel's configuration to network devices. During this t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
aliases:
    - "/reference/services/softlayer_network_tunnel_module_context/applyConfigurationsToDevice"
---
# [SoftLayer_Network_Tunnel_Module_Context](/reference/services/SoftLayer_Network_Tunnel_Module_Context)::applyConfigurationsToDevice

Apply current configuration settings to the network device


## Overview 
An asynchronous task will be created to apply the IPSec network tunnel's configuration to network devices. During this time, an IPSec network tunnel cannot be modified in anyway. Only one network tunnel configuration task can be created at a time. If a task has already been created and has not completed, a new task cannot be created. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Network_Tunnel_Module_Context::addPrivateSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addPrivateSubnetToNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::removePrivateSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removePrivateSubnetFromNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::addCustomerSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addCustomerSubnetToNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::removeCustomerSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeCustomerSubnetFromNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::addServiceSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addServiceSubnetFromNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::removeServiceSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeServiceSubnetFromNetworkTunnel )
*  [SoftLayer_Network_Tunnel_Module_Context::createAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslation )
*  [SoftLayer_Network_Tunnel_Module_Context::createAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslations )
*  [SoftLayer_Network_Tunnel_Module_Context::editAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslation )
*  [SoftLayer_Network_Tunnel_Module_Context::editAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslations )
*  [SoftLayer_Network_Tunnel_Module_Context::editObject](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editObject )



### Error Handling

* SoftLayer_Exception_NotReady 

> <<< EOT 

* SoftLayer_Exception_NotReady 

> <<< EOT 

* SoftLayer_Exception_NotReady 

> <<< EOT 



