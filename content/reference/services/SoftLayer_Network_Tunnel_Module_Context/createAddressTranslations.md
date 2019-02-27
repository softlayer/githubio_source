---
title: "createAddressTranslations"
description: "This has the same functionality as the SoftLayer_Network_Tunnel_Module_Context::createAddressTranslation.  However, it a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
aliases:
    - "/reference/services/softlayer_network_tunnel_module_context/createAddressTranslations"
---
# [SoftLayer_Network_Tunnel_Module_Context](/reference/services/SoftLayer_Network_Tunnel_Module_Context)::createAddressTranslations

Create address translations for a network tunnel


## Overview 
This has the same functionality as the SoftLayer_Network_Tunnel_Module_Context::createAddressTranslation.  However, it allows multiple translations to be passed in for creation. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the address translations to be created. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|translations| <a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation[] </a>| The address translations to create for an IPSec network tunnel.|


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
*  [SoftLayer_Network_Tunnel_Module_Context::editAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslation )
*  [SoftLayer_Network_Tunnel_Module_Context::editAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslations )
*  [SoftLayer_Network_Tunnel_Module_Context::deleteAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/deleteAddressTranslation )
*  [SoftLayer_Network_Tunnel_Module_Context::applyConfigurationsToDevice](/reference/services/SoftLayer_Network_Tunnel_Module_Context/applyConfigurationsToDevice )




