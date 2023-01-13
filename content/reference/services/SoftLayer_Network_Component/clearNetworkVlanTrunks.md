---
title: "clearNetworkVlanTrunks"
description: "Remove all VLANs currently attached as trunks to this network component. 

This method should be called on a network component of assigned hardware. A current list of VLAN trunks for a network component on a customer server can be found at 'uplinkComponent->networkVlanTrunks'. 

This method returns an array of SoftLayer_Network_Vlans which will be removed as trunks. 

Affected VLANs will not yet be removed as trunks upon return of this call, but deactivation and removal will have been scheduled and should be considered imminent. The trunking records associated with the affected VLANs will maintain an 'isUpdating' value of '1' so long as this is the case. 

Note that in the event of a 'pending API request' error some VLANs may still have been affected and scheduled for deactivation. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Component"
---
