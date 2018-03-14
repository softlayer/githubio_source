---
title: "unroute"
description: "This function is used to create a new transaction to unroute a global IP address. Routes are updated in one to two minut... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress_Global"
aliases:
    - "/reference/services/softlayer_network_subnet_ipaddress_global/unroute"
---
# [SoftLayer_Network_Subnet_IpAddress_Global](/reference/services/SoftLayer_Network_Subnet_IpAddress_Global)::unroute

create a new transaction to unroute a global IP.


## Overview 
This function is used to create a new transaction to unroute a global IP address. Routes are updated in one to two minutes depending on the number of transactions that are pending for a router. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Subnet_IpAddress_GlobalInitParameters

### Optional Headers
* SoftLayer_Network_Subnet_IpAddress_GlobalObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>

