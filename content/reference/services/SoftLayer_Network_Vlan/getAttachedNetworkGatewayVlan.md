---
title: "getAttachedNetworkGatewayVlan"
description: "The gateway device VLAN context this VLAN is associated with for routing purposes."
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

### [REST Example](#getAttachedNetworkGatewayVlan-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAttachedNetworkGatewayVlan-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getAttachedNetworkGatewayVlan'
```
