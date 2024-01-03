---
title: "deleteL7PoolMembers"
description: "Delete given members from load balancer and return load balancer object with listeners, pools and members populated "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Member"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_L7Member"
---

# [REST Example](#deleteL7PoolMembers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#deleteL7PoolMembers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Member/deleteL7PoolMembers'
```
