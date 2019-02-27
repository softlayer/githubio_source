---
title: "rejectBypassRequest"
description: "Reject a request from technical support to bypass the firewall. Once rejected, IBM support will not be able to route and... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan_Firewall"
aliases:
    - "/reference/services/softlayer_network_vlan_firewall/rejectBypassRequest"
---
# [SoftLayer_Network_Vlan_Firewall](/reference/services/SoftLayer_Network_Vlan_Firewall)::rejectBypassRequest

Reject a request from technical support to bypass the firewall.


## Overview 
Reject a request from technical support to bypass the firewall. Once rejected, IBM support will not be able to route and unroute the VLAN on the firewall. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_Vlan_FirewallInitParameters


### Return Values
* void



### Error Handling

* SoftLayer_Exception_InvalidStatus 

> Throw the exception "Bypass request is already rejected" 

* SoftLayer_Exception_InvalidStatus 

> Throw the exception "Bypass request is already revoked" 

* SoftLayer_Exception_InvalidStatus 

> Throw the exception "Bypass request is already released from support" 

* SoftLayer_Exception_InvalidStatus 

> Throw the exception "There is no approved bypass request to reject" 



