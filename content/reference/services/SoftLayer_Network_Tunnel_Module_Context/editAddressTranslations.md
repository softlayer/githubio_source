---
title: "editAddressTranslations"
description: "Edit name, source (SoftLayer IP) ip address and/or destination (Customer IP) ip address for existing address translation... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
aliases:
    - "/reference/services/softlayer_network_tunnel_module_context/editAddressTranslations"
---
# [SoftLayer_Network_Tunnel_Module_Context](/reference/services/SoftLayer_Network_Tunnel_Module_Context)::editAddressTranslations


Edit address translations for a network tunnel


## Overview 
Edit name, source (SoftLayer IP) ip address and/or destination (Customer IP) ip address for existing address translations for a network tunnel. 

Address translations deliver packets to a destination ip address that is on a customer (remote) subnet. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for an address translation to be modified. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|translations| <a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation[] </a>| The address translations to edit for an IPSec network tunnel.|


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters


### Optional Headers
* SoftLayer_Network_Tunnel_Module_ContextObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation[] </a>


### Associated Methods

*  [SoftLayer_Network_Tunnel_Module_Context::createAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslation )
*  [SoftLayer_Network_Tunnel_Module_Context::createAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslations )
*  [SoftLayer_Network_Tunnel_Module_Context::editAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslation )
*  [SoftLayer_Network_Tunnel_Module_Context::deleteAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/deleteAddressTranslation )
*  [SoftLayer_Network_Tunnel_Module_Context::applyConfigurationsToDevice](/reference/services/SoftLayer_Network_Tunnel_Module_Context/applyConfigurationsToDevice )




