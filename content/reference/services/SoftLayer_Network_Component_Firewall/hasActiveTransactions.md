---
title: "hasActiveTransactions"
description: "Check for active transactions for the shared Firewall. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component_Firewall"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Component_Firewall"
---

### [REST Example](#hasActiveTransactions-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#hasActiveTransactions-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Component_Firewall/{SoftLayer_Network_Component_FirewallID}/hasActiveTransactions'
```
