---
title: "getPrivateVlan"
description: "Retrieve the backend VLAN for the primary IP address of the server"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getPrivateVlan"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getPrivateVlan


Retrieve the backend VLAN for the primary IP address of the server.


## Overview 
Retrieve the backend VLAN for the primary IP address of the server 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModule750InitParameters


### Optional Headers
* SoftLayer_Hardware_SecurityModule750ObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "No public network components found for hardware." a server does not have any private network components installed. 

* SoftLayer_Exception 

> Throw the exception "No IP address found for public network component" if there is no backend primary IP address for the network components on a server. 

* SoftLayer_Exception 

> Throw the exception "Unable to find a public subnet." if there are no backend subnets the network components are associated with. 



