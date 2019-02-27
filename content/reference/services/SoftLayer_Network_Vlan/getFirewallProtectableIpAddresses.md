---
title: "getFirewallProtectableIpAddresses"
description: "Get the IP addresses associated with this server that are protectable by a network component firewall. Note, this may no... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/getFirewallProtectableIpAddresses"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::getFirewallProtectableIpAddresses

Get the IP addresses associated with this server that are protectable by a network component firewall.


## Overview 
Get the IP addresses associated with this server that are protectable by a network component firewall. Note, this may not return all values for IPv6 subnets for this VLAN. Please use getFirewallProtectableSubnets to get all protectable subnets. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_VlanInitParameters


### Optional Headers
* SoftLayer_Network_VlanObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>




