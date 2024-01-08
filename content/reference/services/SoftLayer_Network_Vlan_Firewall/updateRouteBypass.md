---
title: "updateRouteBypass"
description: "Enable or disable route bypass for this context. If enabled, this will bypass the firewall entirely and all traffic will be routed directly to the host(s) behind it. If disabled, traffic will flow through the firewall normally. This feature is only available for Hardware Firewall (Dedicated) and dedicated appliances. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan_Firewall"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Vlan_Firewall"
---

### [REST Example](#updateRouteBypass-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateRouteBypass-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan_Firewall/{SoftLayer_Network_Vlan_FirewallID}/updateRouteBypass'
```
