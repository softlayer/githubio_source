---
title: "rejectBypassRequest"
description: "Reject a request from technical support to bypass the firewall. Once rejected, IBM support will not be able to route and unroute the VLAN on the firewall. "
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

### [REST Example](#rejectBypassRequest-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#rejectBypassRequest-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan_Firewall/{SoftLayer_Network_Vlan_FirewallID}/rejectBypassRequest'
```
