---
title: "getRoutableEndpointIpAddresses"
description: "Returns IP addresses which may be used as routing endpoints for a given subnet. IP address which are currently the netwo... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
aliases:
    - "/reference/services/softlayer_network_subnet/getRoutableEndpointIpAddresses"
---
# [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet)::getRoutableEndpointIpAddresses


Retrieve IP addresses which may be used as a routing endpoint from a subnet.


## Overview 
Returns IP addresses which may be used as routing endpoints for a given subnet. IP address which are currently the network, gateway, or broadcast address of a Secondary Portable subnet, are an address in a Secondary Static subnet, or if the address is not assigned to a resource when part of a Primary Subnet will not be available as a routing endpoint. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_SubnetInitParameters


### Optional Headers
* SoftLayer_Network_SubnetObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>




