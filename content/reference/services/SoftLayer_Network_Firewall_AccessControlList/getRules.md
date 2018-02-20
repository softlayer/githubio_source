---
title: "getRules"
description: "Retrieve the currently running rule set of this context access control list firewall."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_AccessControlList"
---
# SoftLayer_Network_Firewall_AccessControlList::getRules
## Overview 
Retrieve the currently running rule set of this context access control list firewall.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Network_Firewall_AccessControlListInitParameters
* authenticate

### Optional Headers
* SoftLayer_Network_Firewall_AccessControlListObjectMask
* SoftLayer_Network_Firewall_AccessControlListObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall_Rule'>SoftLayer_Network_Vlan_Firewall_Rule[] </a>
