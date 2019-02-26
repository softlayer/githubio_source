---
title: "getManagementNetworkComponent"
description: "Retrieve the remote management network component attached with this server."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getManagementNetworkComponent"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getManagementNetworkComponent

Retrieve a server's management network component.


## Overview 
Retrieve the remote management network component attached with this server. 

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

> Throw the exception "Unable to locate this server's management networking component." if the API is unable to locate a management component for this server. 



