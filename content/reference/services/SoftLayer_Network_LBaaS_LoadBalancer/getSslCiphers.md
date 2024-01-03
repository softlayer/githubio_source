---
title: "getSslCiphers"
description: "list of preferred custom ciphers configured for the load balancer."
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

# [REST Example](#getSslCiphers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getSslCiphers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_LoadBalancer/{SoftLayer_Network_LBaaS_LoadBalancerID}/getSslCiphers'
```
