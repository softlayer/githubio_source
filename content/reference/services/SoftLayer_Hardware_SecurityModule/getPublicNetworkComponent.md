---
title: "getPublicNetworkComponent"
description: "Retrieve a SoftLayer server's public network component. Some servers are only connected to the private network and may n... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getPublicNetworkComponent"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getPublicNetworkComponent


Retrieve a server's public network component.


## Overview 
Retrieve a SoftLayer server's public network component. Some servers are only connected to the private network and may not have a public network component. In that case getPublicNetworkComponent returns a null object. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters


### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Unable to locate this server's public networking component." if the API is unable to locate a management component for this server. 



