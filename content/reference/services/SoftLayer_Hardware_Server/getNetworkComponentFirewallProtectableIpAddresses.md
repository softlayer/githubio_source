---
title: "getNetworkComponentFirewallProtectableIpAddresses"
description: "Get the IP addresses associated with this server that are protectable by a network component firewall. Note, this may not return all values for IPv6 subnets for this server. Please use getFirewallProtectableSubnets to get all protectable subnets. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Server"
---

### [REST Example](#getNetworkComponentFirewallProtectableIpAddresses-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getNetworkComponentFirewallProtectableIpAddresses-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/getNetworkComponentFirewallProtectableIpAddresses'
```
