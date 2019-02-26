---
title: "getNetworkComponentFirewallProtectableIpAddresses"
description: "Get the IP addresses associated with this CloudLayer computing instance that are protectable by a network component fire... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
aliases:
    - "/reference/services/softlayer_virtual_guest/getNetworkComponentFirewallProtectableIpAddresses"
---
# [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest)::getNetworkComponentFirewallProtectableIpAddresses

Get the IP addresses associated with this CloudLayer computing instance that are protectable by a network component firewall.


## Overview 
Get the IP addresses associated with this CloudLayer computing instance that are protectable by a network component firewall. Note, this may not return all values for IPv6 subnets for this CloudLayer computing instance. Please use getFirewallProtectableSubnets to get all protectable subnets. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Virtual_GuestInitParameters


### Optional Headers
* SoftLayer_Virtual_GuestObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>




