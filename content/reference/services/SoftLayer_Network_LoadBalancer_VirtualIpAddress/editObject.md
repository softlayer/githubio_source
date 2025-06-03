---
title: "editObject"
description: "Deprecated "
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

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_LoadBalancer_VirtualIpAddress]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_LoadBalancer_VirtualIpAddressID}/editObject'
```
