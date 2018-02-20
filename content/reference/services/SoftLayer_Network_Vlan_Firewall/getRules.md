---
title: "getRules"
description: "Retrieve the currently running rule set of this network component firewall."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan_Firewall"
---
# SoftLayer_Network_Vlan_Firewall::getRules
## Overview 
Retrieve the currently running rule set of this network component firewall.

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
<a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall_Rule'>SoftLayer_Network_Vlan_Firewall_Rule[] </a>
