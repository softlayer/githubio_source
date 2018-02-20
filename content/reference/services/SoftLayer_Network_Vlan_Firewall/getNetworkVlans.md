---
title: "getNetworkVlans"
description: "Retrieve the VLAN objects that a firewall is associated with and protecting."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan_Firewall"
---
# SoftLayer_Network_Vlan_Firewall::getNetworkVlans
## Overview 
Retrieve the VLAN objects that a firewall is associated with and protecting.

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
<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>
