---
title: "getPrivateVlanByIpAddress"
description: "Retrieve a backend network VLAN by searching for an IP address"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getPrivateVlanByIpAddress"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getPrivateVlanByIpAddress

Retrieve a backend network VLAN by searching for an IP address.


## Overview 
Retrieve a backend network VLAN by searching for an IP address 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| The server's IP address you are searching for.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>

