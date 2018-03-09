---
title: "getApplyServerRuleSubnets"
description: "Retrieve the additional subnets linked to this network component firewall, that inherit rules from the host that the con... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component_Firewall"
---
# [SoftLayer_Network_Component_Firewall](/reference/services/SoftLayer_Network_Component_Firewall)::getApplyServerRuleSubnets

Retrieve the additional subnets linked to this network component firewall, that inherit rules from the host that the context slot is attached to.


## Overview 
Retrieve the additional subnets linked to this network component firewall, that inherit rules from the host that the context slot is attached to.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Component_FirewallInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Component_FirewallObjectMask
* SoftLayer_Network_Component_FirewallObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>

