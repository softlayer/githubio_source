---
title: "editAddressTranslation"
description: "Edit name, source (SoftLayer IP) ip address and/or destination (Customer IP) ip address for an existing address translat... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# SoftLayer_Network_Tunnel_Module_Context::editAddressTranslation
## Overview 
Edit name, source (SoftLayer IP) ip address and/or destination (Customer IP) ip address for an existing address translation for a network tunnel. 

Address translations deliver packets to a destination ip address that is on a customer (remote) subnet. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for an address translation to be created. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|translation| <a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation </a>| The address translation to edit for an IPSec network tunnel.|


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters

### Optional Headers
* SoftLayer_Network_Tunnel_Module_ContextObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation </a>


### associatedMethods

*  [SoftLayer_Network_Tunnel_Module_Context::createAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslation )
*  [SoftLayer_Network_Tunnel_Module_Context::createAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslations )
*  [SoftLayer_Network_Tunnel_Module_Context::editAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslations )
*  [SoftLayer_Network_Tunnel_Module_Context::deleteAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/deleteAddressTranslation )
*  [SoftLayer_Network_Tunnel_Module_Context::applyConfigurationsToDevice](/reference/services/SoftLayer_Network_Tunnel_Module_Context/applyConfigurationsToDevice )

