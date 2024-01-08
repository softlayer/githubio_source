---
title: "updateSslCiphers"
description: "Updates the load balancer with the new cipher list. All new connections going forward will use the new set of ciphers selected by the user. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancer"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_LoadBalancer"
---

### [REST Example](#updateSslCiphers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateSslCiphers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_LoadBalancer/updateSslCiphers'
```
