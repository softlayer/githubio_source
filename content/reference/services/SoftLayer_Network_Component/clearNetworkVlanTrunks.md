---
title: "clearNetworkVlanTrunks"
description: "This method will remove all VLANs trunked to this network component. The native VLAN (networkVlanId/networkVlan) will re... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
---
# SoftLayer_Network_Component::clearNetworkVlanTrunks
## Overview 
This method will remove all VLANs trunked to this network component. The native VLAN (networkVlanId/networkVlan) will remain active, and cannot be removed via the API. Returns a list of SoftLayer_Network_Vlan objects for which the trunks were removed. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_ComponentInitParameters

### Optional Headers
* SoftLayer_Network_ComponentObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>
