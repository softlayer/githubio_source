---
title: "updateFirewallIntraVlanCommunication"
description: "The '''getSensorData''' method updates a VLAN's firewall to allow or disallow intra-VLAN communication."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
aliases:
    - "/reference/services/softlayer_network_vlan/updateFirewallIntraVlanCommunication"
---
# [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan)::updateFirewallIntraVlanCommunication

Update a VLAN's firewall to allow or disallow intra-VLAN communication.


## Overview 
The '''getSensorData''' method updates a VLAN's firewall to allow or disallow intra-VLAN communication. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|enabled| boolean| Whether or not intra-VLAN communication should be enabled.|


### Required Headers
* authenticate
* SoftLayer_Network_VlanInitParameters


### Return Values
* void



### Error Handling

* SoftLayer_Exception 

> Throw the exception "VLAN does not have an associated firewall context." if this VLAN does not have an associated firewall. 



