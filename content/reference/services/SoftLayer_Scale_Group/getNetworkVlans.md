---
title: "getNetworkVlans"
description: "Retrieve collection of VLANs for this auto scale group. VLANs are optional. This can contain a public or private VLAN or... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Group"
---
# [SoftLayer_Scale_Group](/reference/services/SoftLayer_Scale_Group)::getNetworkVlans

Retrieve collection of VLANs for this auto scale group. VLANs are optional. This can contain a public or private VLAN or both. When a single VLAN for a public/private type is given it can be a non-purchased VLAN only if the minimumMemberCount on the group is >= 1. This can also contain any number of public/private purchased VLANs and members are staggered across them when scaled up.


## Overview 
Retrieve collection of VLANs for this auto scale group. VLANs are optional. This can contain a public or private VLAN or both. When a single VLAN for a public/private type is given it can be a non-purchased VLAN only if the minimumMemberCount on the group is >= 1. This can also contain any number of public/private purchased VLANs and members are staggered across them when scaled up.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_Scale_GroupInitParameters
* authenticate

### Optional Headers
* SoftLayer_Scale_GroupObjectMask
* SoftLayer_Scale_GroupObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Scale_Network_Vlan'>SoftLayer_Scale_Network_Vlan[] </a>

