---
title: "getBoundSubnets"
description: "Retrieve subnets which are directly bound to one or more routers in a given datacenter, and currently allow routing."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Datacenter"
---
# SoftLayer_Location_Datacenter::getBoundSubnets
## Overview 
Retrieve subnets which are directly bound to one or more routers in a given datacenter, and currently allow routing.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Location_DatacenterInitParameters
* authenticate

### Optional Headers
* SoftLayer_Location_DatacenterObjectMask
* SoftLayer_Location_DatacenterObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>
