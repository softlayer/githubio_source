---
title: "updateRouteBypass"
description: "Enable or disable route bypass for this context. If enabled, this will bypass the firewall entirely and all traffic will... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan_Firewall"
aliases:
    - "/reference/services/softlayer_network_vlan_firewall/updateRouteBypass"
---
# [SoftLayer_Network_Vlan_Firewall](/reference/services/SoftLayer_Network_Vlan_Firewall)::updateRouteBypass


Enable or disable route bypass.


## Overview 
Enable or disable route bypass for this context. If enabled, this will bypass the firewall entirely and all traffic will be routed directly to the host(s) behind it. If disabled, traffic will flow through the firewall normally. This feature is only available for Hardware Firewall (Dedicated) and dedicated appliances. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|bypass| boolean| True to enable bypass, false to disable bypass|


### Required Headers
* authenticate
* SoftLayer_Network_Vlan_FirewallInitParameters


### Optional Headers
* SoftLayer_Network_Vlan_FirewallObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>




