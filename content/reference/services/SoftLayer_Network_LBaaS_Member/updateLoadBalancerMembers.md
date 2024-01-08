---
title: "updateLoadBalancerMembers"
description: "Update members weight and return load balancer object with listeners, pools and members populated "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Member"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_Member"
---

### [REST Example](#updateLoadBalancerMembers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateLoadBalancerMembers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_Member]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_Member/updateLoadBalancerMembers'
```
