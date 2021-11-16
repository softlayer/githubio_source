---
title: "getHardwareByIpAddress"
description: "Retrieve a server by searching for the primary IP address."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/getHardwareByIpAddress"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::getHardwareByIpAddress


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
* SoftLayer_Hardware_SecurityModule750ObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Hardware_SecurityModule750'>SoftLayer_Hardware_SecurityModule750 </a>




