---
title: "updateL7Pool"
description: "Updates an existing L7 pool, L7 health monitor and L7 session affinity. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Pool"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_L7Pool"
---

# [REST Example](#updateL7Pool-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateL7Pool-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_L7Pool, SoftLayer_Network_LBaaS_L7HealthMonitor, SoftLayer_Network_LBaaS_L7SessionAffinity]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Pool/updateL7Pool'
```
