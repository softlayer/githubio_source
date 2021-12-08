---
title: "getPublicVlan"
description: "Retrieve the frontend VLAN for the primary IP address of the server"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule/getPublicVlan"
---
# [SoftLayer_Hardware_SecurityModule](/reference/services/SoftLayer_Hardware_SecurityModule)::getPublicVlan


Retrieve the frontend VLAN for the primary IP address of the server


## Overview 
Retrieve the frontend VLAN for the primary IP address of the server 

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
* <a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "No public network components found for hardware." a server does not have any network components installed. 

* SoftLayer_Exception 

> Throw the exception "No IP address found for public network component" if there is no primary IP address for the network components on a server. 

* SoftLayer_Exception 

> Throw the exception "Unable to find a public subnet." if there are no frontend subnets the network components are associated with. 



