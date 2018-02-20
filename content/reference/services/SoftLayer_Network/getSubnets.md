---
title: "getSubnets"
description: "Retrieve the Subnets within the Network. These represent the realized segments of the Network and reside within a [[Soft... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network"
---
# SoftLayer_Network::getSubnets
## Overview 
Retrieve the Subnets within the Network. These represent the realized segments of the Network and reside within a [[SoftLayer_Network_Pod|Pod]]. A Subnet must be specified when provisioning a compute resource within a Network.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_NetworkInitParameters
* authenticate

### Optional Headers
* SoftLayer_NetworkObjectMask
* SoftLayer_NetworkObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>
