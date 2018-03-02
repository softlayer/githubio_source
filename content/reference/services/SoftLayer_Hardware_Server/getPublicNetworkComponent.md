---
title: "getPublicNetworkComponent"
description: "Retrieve a SoftLayer server's public network component. Some servers are only connected to the private network and may n... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
---
# SoftLayer_Hardware_Server::getPublicNetworkComponent
## Overview 
Retrieve a SoftLayer server's public network component. Some servers are only connected to the private network and may not have a public network component. In that case getPublicNetworkComponent returns a null object. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters

### Optional Headers
* SoftLayer_Hardware_ServerObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>

