---
title: "getPublicVlanByHostname"
description: "Retrieve the frontend network Vlan by searching the hostname of a server"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
---
# SoftLayer_Hardware_SecurityModule::getPublicVlanByHostname
## Overview 
Retrieve the frontend network Vlan by searching the hostname of a server 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hostname| string| The hostname for a server, example: www.server.com|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>

