---
title: "getRoutableBoundSubnets"
description: "Retrieve retrieve all subnets that are eligible to be routed; those which the account has permission to associate with a... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Datacenter"
aliases:
    - "/reference/services/softlayer_location_datacenter/getRoutableBoundSubnets"
---
# [SoftLayer_Location_Datacenter](/reference/services/SoftLayer_Location_Datacenter)::getRoutableBoundSubnets

Retrieve retrieve all subnets that are eligible to be routed; those which the account has permission to associate with a vlan.


## Overview 
Retrieve retrieve all subnets that are eligible to be routed; those which the account has permission to associate with a vlan.

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

