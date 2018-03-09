---
title: "route"
description: "This function is used to create a new transaction to modify a global IP route. Routes are updated in one to two minutes... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress_Global"
---
# [SoftLayer_Network_Subnet_IpAddress_Global](/reference/services/SoftLayer_Network_Subnet_IpAddress_Global)::route

create a new transaction to reroute a global IP.


## Overview 
This function is used to create a new transaction to modify a global IP route. Routes are updated in one to two minutes depending on the number of transactions that are pending for a router. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|newEndPointIpAddress| string| The IP address to route the subnet to.|


### Required Headers
* authenticate
* SoftLayer_Network_Subnet_IpAddress_GlobalInitParameters

### Optional Headers
* SoftLayer_Network_Subnet_IpAddress_GlobalObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>

