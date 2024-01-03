---
title: "getAttachedNetworkGatewayFlag"
description: "A value of '1' indicates this VLAN is associated with a gateway device for routing purposes."
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

# [REST Example](#getAttachedNetworkGatewayFlag-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getAttachedNetworkGatewayFlag-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getAttachedNetworkGatewayFlag'
```
