---
title: "findByIpAddress"
description: "Find CCI by only its primary public or private IP address. IP addresses within secondary subnets tied to the CCI will no... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
---
# SoftLayer_Virtual_Guest::findByIpAddress
## Overview 
Find CCI by only its primary public or private IP address. IP addresses within secondary subnets tied to the CCI will not return the CCI. If no CCI is found, no errors are generated and no data is returned. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|ipAddress| string| An IP (ipv4) address by which to search for CCI|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>

