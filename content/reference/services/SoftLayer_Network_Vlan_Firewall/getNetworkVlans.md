---
title: "getNetworkVlans"
description: "The VLAN objects that a firewall is associated with and protecting."
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

### [REST Example](#getNetworkVlans-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNetworkVlans-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan_Firewall/{SoftLayer_Network_Vlan_FirewallID}/getNetworkVlans'
```
