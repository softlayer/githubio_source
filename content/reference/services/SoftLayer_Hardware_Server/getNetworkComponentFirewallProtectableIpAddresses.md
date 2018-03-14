---
title: "getNetworkComponentFirewallProtectableIpAddresses"
description: "Get the IP addresses associated with this server that are protectable by a network component firewall. Note, this may no... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
aliases:
    - "/reference/services/softlayer_hardware_server/getNetworkComponentFirewallProtectableIpAddresses"
---
# [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)::getNetworkComponentFirewallProtectableIpAddresses

Get the IP addresses associated with this server that are protectable by a network component firewall.


## Overview 
Get the IP addresses associated with this server that are protectable by a network component firewall. Note, this may not return all values for IPv6 subnets for this server. Please use getFirewallProtectableSubnets to get all protectable subnets. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_ServerInitParameters

### Optional Headers
* SoftLayer_Hardware_ServerObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>

