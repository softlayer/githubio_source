---
title: "getAddressTranslationConfigurations"
description: "The address translations will be returned.  All the translations will be formatted so that the configurations can be cop... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---
# [SoftLayer_Network_Tunnel_Module_Context](/reference/services/SoftLayer_Network_Tunnel_Module_Context)::getAddressTranslationConfigurations

Build and returns IPsec VPN  tunnel address translation configurations


## Overview 
The address translations will be returned.  All the translations will be formatted so that the configurations can be copied into a host file. 

Format: 

{address translation SoftLayer IP Address}        {address translation name} 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Tunnel_Module_ContextInitParameters

### Optional Headers

### Return Values
string


### associatedMethods

*  [SoftLayer_Network_Tunnel_Module_Context::downloadAddressTranslationConfigurations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/downloadAddressTranslationConfigurations )

