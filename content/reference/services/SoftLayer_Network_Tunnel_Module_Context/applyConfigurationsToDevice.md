---
title: "applyConfigurationsToDevice"
description: "A transaction will be created to apply the IPSec network tunnel's configuration to SoftLayer network devices.  During th... "
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
A transaction will be created to apply the IPSec network tunnel's configuration to SoftLayer network devices.  During this time, an IPSec network tunnel cannot be modified in anyway.  Only one network tunnel configuration transaction can be created.  If a transaction has been created or is running, a new transaction cannot be created until the previous transaction completes. 

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
*  [SoftLayer_Network_Tunnel_Module_Context::applyConfigurationsToDevice](/reference/services/SoftLayer_Network_Tunnel_Module_Context/applyConfigurationsToDevice )
*  [SoftLayer_Network_Tunnel_Module_Context::editObject](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editObject )




