---
title: "addNetworkVlanTrunks"
description: "Add VLANs as trunks to a network component. The VLANs given must be assigned to your account and belong to the same pod in which this network component and its hardware reside. The current native VLAN cannot be added as a trunk. 

This method should be called on a network component of assigned hardware. A current list of VLAN trunks for a network component on a customer server can be found at 'uplinkComponent->networkVlanTrunks'. 

This method returns an array of SoftLayer_Network_Vlans which were added as trunks. Any requested VLANs which are already trunked will be ignored and will not be returned. 

Affected VLANs will not yet be operational as trunks on the network upon return of this call, but activation will have been scheduled and should be considered imminent. The trunking records associated with the affected VLANs will maintain an 'isUpdating' value of '1' so long as this is the case. 

Note that in the event of an 'internal system error' some VLANs may still have been affected and scheduled for activation. "
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

### [REST Example](#addNetworkVlanTrunks-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addNetworkVlanTrunks-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Vlan]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Component/{SoftLayer_Network_ComponentID}/addNetworkVlanTrunks'
```
