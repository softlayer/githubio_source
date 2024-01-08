---
title: "getFirewallGuestNetworkComponents"
description: "The VSI network interfaces connected to this VLAN and associated with a Hardware Firewall."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Vlan"
---

### [REST Example](#getFirewallGuestNetworkComponents-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFirewallGuestNetworkComponents-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getFirewallGuestNetworkComponents'
```
