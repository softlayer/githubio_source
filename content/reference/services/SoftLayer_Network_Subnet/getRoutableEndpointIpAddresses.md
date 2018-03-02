---
title: "getRoutableEndpointIpAddresses"
description: "getRoutableEndpointAddresses retrieves valid routable endpoint addresses for a subnet. You may use any IP address in a p... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
---
# SoftLayer_Network_Subnet::getRoutableEndpointIpAddresses
## Overview 
getRoutableEndpointAddresses retrieves valid routable endpoint addresses for a subnet. You may use any IP address in a portable subnet, but may not use the network identifier, gateway, or broadcast address for primary and secondary on VLAN subnets. 

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
<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>

