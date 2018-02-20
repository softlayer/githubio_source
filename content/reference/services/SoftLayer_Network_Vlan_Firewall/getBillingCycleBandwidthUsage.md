---
title: "getBillingCycleBandwidthUsage"
description: "Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this f... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan_Firewall"
---
# SoftLayer_Network_Vlan_Firewall::getBillingCycleBandwidthUsage
## Overview 
Retrieve the raw bandwidth usage data for the current billing cycle. One object will be returned for each network this firewall is attached to.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Vlan_FirewallInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Vlan_FirewallObjectMask
* SoftLayer_Network_Vlan_FirewallObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Usage'>SoftLayer_Network_Bandwidth_Usage[] </a>
