---
title: "getAvailableRouters"
description: "This method will get the available backend routers to order a dedicated host."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_DedicatedHost"
aliases:
    - "/reference/services/softlayer_virtual_dedicatedhost/getAvailableRouters"
---
# [SoftLayer_Virtual_DedicatedHost](/reference/services/SoftLayer_Virtual_DedicatedHost)::getAvailableRouters


Get available backend routers in a datacenter to order a dedicated host. 


## Overview 
This method will get the available backend routers to order a dedicated host. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|dedicatedHost| <a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost </a>| Template object used to specify datacenter and configuration sizes|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Virtual_DedicatedHostObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>




