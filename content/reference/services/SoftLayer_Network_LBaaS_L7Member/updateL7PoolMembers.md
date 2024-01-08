---
title: "updateL7PoolMembers"
description: "Update L7 members weight and port. "
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

### [REST Example](#updateL7PoolMembers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateL7PoolMembers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_L7Member]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Member/updateL7PoolMembers'
```
