---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Tunnel_Module_Context object whose ID number corresponds to the ID number of t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
aliases:
    - "/reference/services/softlayer_network_tunnel_module_context/getObject"
---
# [SoftLayer_Network_Tunnel_Module_Context](/reference/services/SoftLayer_Network_Tunnel_Module_Context)::getObject

Retrieve a SoftLayer_Network_Tunnel_Module_Context record.


## Overview 
getObject retrieves the SoftLayer_Network_Tunnel_Module_Context object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Tunnel_Module_Context service. The IPSec network tunnel will be returned if it is associated with the account and the user has proper permission to manage network tunnels. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Tunnel_Module_ContextInitParameters
* authenticate


### Optional Headers
* SoftLayer_Network_Tunnel_Module_ContextObjectMask
* SoftLayer_Network_Tunnel_Module_ContextObjectFilter
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context'>SoftLayer_Network_Tunnel_Module_Context </a>




