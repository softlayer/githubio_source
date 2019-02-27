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
aliases:
    - "/reference/services/softlayer_virtual_guest/findByIpAddress"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::findByIpAddress

Find CCI by its primary public or private IP (ipv4) address.


## Overview 
Find CCI by only its primary public or private IP address. IP addresses within secondary subnets tied to the CCI will not return the CCI. If no CCI is found, no errors are generated and no data is returned. 

-----

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
* <a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>



### Error Handling

* SoftLayer_Exception 

> Throw the exception "Invalid IP address of {ipAddress} defined." when the IP given is not a valid ipv4 IP address. 



