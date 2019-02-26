---
title: "removeNetworkVlanTrunks"
description: "Remove one or more VLANs currently attached to the uplinkComponent of this networkComponent. The VLANs given must be ass... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
aliases:
    - "/reference/services/softlayer_network_component/removeNetworkVlanTrunks"
---
# [SoftLayer_Network_Component](/reference/services/SoftLayer_Network_Component)::removeNetworkVlanTrunks

Remove VLAN trunks from a network component


## Overview 
Remove one or more VLANs currently attached to the uplinkComponent of this networkComponent. The VLANs given must be assigned to your account, and on the router the network component is connected to. If any VLANs not currently trunked are given, they will be silently ignored. 

This method should be called on a network component attached directly to customer assigned hardware, though all trunking operations will occur on the uplinkComponent. A current list of VLAN trunks for a network component on a customer server can be found at 'uplinkComponent->networkVlanTrunks'. 

Configuration of network hardware is done asynchronously, do not depend on the return of this call as an indication that the removed VLANs will be inaccessible. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|networkVlans| <a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>| An array of Network_Vlan|


### Required Headers
* authenticate
* SoftLayer_Network_ComponentInitParameters


### Optional Headers
* SoftLayer_Network_ComponentObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan[] </a>




