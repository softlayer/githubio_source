---
title: "updateLoadBalancer"
description: "Update load balancer's description, and return the load balancer object containing all listeners, pools, members and datacenter. "
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

# [REST Example](#updateLoadBalancer-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateLoadBalancer-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_LoadBalancer/updateLoadBalancer'
```
