---
title: "getRules"
description: "The currently running rule set of this network component firewall."
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

# [REST Example](#getRules-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRules-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan_Firewall/{SoftLayer_Network_Vlan_FirewallID}/getRules'
```
