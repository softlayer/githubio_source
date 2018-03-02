---
title: "getNetworkComponentFirewallProtectableIpAddresses"
description: "Get the IP addresses associated with this server that are protectable by a network component firewall. Note, this may no... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
---
# SoftLayer_Hardware_SecurityModule::getNetworkComponentFirewallProtectableIpAddresses
## Overview 
Get the IP addresses associated with this server that are protectable by a network component firewall. Note, this may not return all values for IPv6 subnets for this server. Please use getFirewallProtectableSubnets to get all protectable subnets. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Hardware_SecurityModuleInitParameters

### Optional Headers
* SoftLayer_Hardware_SecurityModuleObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>

