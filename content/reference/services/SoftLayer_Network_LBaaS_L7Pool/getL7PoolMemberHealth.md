---
title: "getL7PoolMemberHealth"
description: "Returns the health of all L7 pool's members which are created under load balancer. L7 members health status is available only after a L7 pool is associated with the L7 policy and that L7 policy has at least one L7 rule. "
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

# [REST Example](#getL7PoolMemberHealth-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getL7PoolMemberHealth-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Pool/getL7PoolMemberHealth'
```
