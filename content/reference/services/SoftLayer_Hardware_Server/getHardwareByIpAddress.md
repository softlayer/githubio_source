---
title: "getHardwareByIpAddress"
description: "Retrieve a server by searching for the primary IP address."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getHardwareByIpAddress"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getHardwareByIpAddress


Retrieve a SoftLayer_Hardware_Server object by IP address.


## Overview 
Retrieve a server by searching for the primary IP address. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| The IP address for the server you would like to locate.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Hardware_ServerObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Hardware_Server'>SoftLayer_Hardware_Server </a>




