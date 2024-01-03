---
title: "getFirewallProtectableIpAddresses"
description: "
*** DEPRECATED ***
Retrieves the IP addresses routed on this VLAN that are protectable by a Hardware Firewall. "
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

# [REST Example](#getFirewallProtectableIpAddresses-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFirewallProtectableIpAddresses-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/{SoftLayer_Network_VlanID}/getFirewallProtectableIpAddresses'
```
