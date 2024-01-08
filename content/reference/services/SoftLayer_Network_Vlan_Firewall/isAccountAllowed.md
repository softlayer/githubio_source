---
title: "isAccountAllowed"
description: "Checks if the account is allowed to use some features of FSA1G and Hardware firewall (Dedicated) "
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

### [REST Example](#isAccountAllowed-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#isAccountAllowed-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan_Firewall/{SoftLayer_Network_Vlan_FirewallID}/isAccountAllowed'
```
