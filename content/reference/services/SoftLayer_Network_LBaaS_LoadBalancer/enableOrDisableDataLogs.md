---
title: "enableOrDisableDataLogs"
description: "When enabled, data log would be forwarded to logging service. "
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

# [REST Example](#enableOrDisableDataLogs-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#enableOrDisableDataLogs-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_LoadBalancer/enableOrDisableDataLogs'
```
