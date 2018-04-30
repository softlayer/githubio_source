---
title: "getPrivateVlanByIpAddress"
description: "Retrieve a backend network VLAN by searching for an IP address"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getPrivateVlanByIpAddress"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getPrivateVlanByIpAddress

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
* SoftLayer_Hardware_ServerObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>

