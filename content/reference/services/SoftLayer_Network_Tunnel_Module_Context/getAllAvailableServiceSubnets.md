---
title: "getAllAvailableServiceSubnets"
description: "Retrieve subnets that provide access to SoftLayer services such as the management portal and the SoftLayer API."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# SoftLayer_Network_Tunnel_Module_Context::getAllAvailableServiceSubnets
## Overview 
Retrieve subnets that provide access to SoftLayer services such as the management portal and the SoftLayer API.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Tunnel_Module_ContextInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Tunnel_Module_ContextObjectMask
* SoftLayer_Network_Tunnel_Module_ContextObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>

