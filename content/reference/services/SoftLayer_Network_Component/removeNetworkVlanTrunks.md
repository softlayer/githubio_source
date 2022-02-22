---
title: "removeNetworkVlanTrunks"
description: "Remove one or more VLANs currently attached to the uplinkComponent of this networkComponent. The VLANs given must be assigned to your account, and on the router the network component is connected to. If any VLANs not currently trunked are given, they will be silently ignored. 

This method should be called on a network component attached directly to customer assigned hardware, though all trunking operations will occur on the uplinkComponent. A current list of VLAN trunks for a network component on a customer server can be found at 'uplinkComponent->networkVlanTrunks'. 

Configuration of network hardware is done asynchronously, do not depend on the return of this call as an indication that the removed VLANs will be inaccessible. "
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
