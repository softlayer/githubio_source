---
title: "getPrivateNetworkComponent"
description: "Retrieve the private network component attached with this server."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getPrivateNetworkComponent"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getPrivateNetworkComponent

Retrieve a server's private network component.


## Overview 
Retrieve the private network component attached with this server. 

-----

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
* <a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to locate this server's private networking component." if the API is unable to locate a management component for this server. 



