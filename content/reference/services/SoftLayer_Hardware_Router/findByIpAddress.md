---
title: "findByIpAddress"
description: "The '''findByIpAddress''' method finds hardware using its primary public or private IP address. IP addresses that have a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Router"
aliases:
    - "/reference/services/softlayer_hardware_router/findByIpAddress"
---
# [SoftLayer_Hardware_Router](/reference/services/SoftLayer_Hardware_Router)::findByIpAddress

Find hardware by its primary public or private IP (ipv4) address.


## Overview 
The '''findByIpAddress''' method finds hardware using its primary public or private IP address. IP addresses that have a secondary subnet tied to the hardware will not return the hardware - alternate means of locating the hardware must be used (see '''Associated Methods'''). If no hardware is found, no errors are generated and no data is returned. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| An IP (ipv4) address by which to search for hardware|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Hardware_RouterObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Hardware_Router'>SoftLayer_Hardware_Router </a>

