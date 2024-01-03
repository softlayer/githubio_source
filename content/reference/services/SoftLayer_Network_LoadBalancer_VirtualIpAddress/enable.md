---
title: "enable"
description: "Enable a disabled Virtual IP Address, allowing connections back to the IP address. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
---

# [REST Example](#enable-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#enable-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_LoadBalancer_VirtualIpAddressID}/enable'
```
