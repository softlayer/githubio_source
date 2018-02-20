---
title: "addNetworkVlanTrunks"
description: "Add VLANs as trunks to a network component. The VLANs given must be assigned to your account, and on the router to which... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
---
# SoftLayer_Network_Component::addNetworkVlanTrunks
## Overview 
Add VLANs as trunks to a network component. The VLANs given must be assigned to your account, and on the router to which this network component is connected. The current native VLAN (networkVlanId/networkVlan) cannot be added as a trunk. This method should be called on a network component attached directly to customer assigned hardware, though all trunking operations will occur on the uplinkComponent. A current list of VLAN trunks for a network component on a customer server can be found at 'uplinkComponent->networkVlanTrunks'. 

This method returns an array of SoftLayer_Network_Vlans which were added as trunks. Any requested trunks which are already trunked will be silently ignored, and will not be returned. 

Configuration of network hardware is done asynchronously, do not depend on the return of this call as an indication that the newly trunked VLANs will be accessible. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|networkVlans| <a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>| An array of Network_Vlan objects with the 'id' or 'vlanNumber'|


### Required Headers
* authenticate
* SoftLayer_Network_ComponentInitParameters

### Optional Headers
* SoftLayer_Network_ComponentObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>
