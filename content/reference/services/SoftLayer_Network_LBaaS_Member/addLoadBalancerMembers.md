---
title: "addLoadBalancerMembers"
description: "Add server instances as members to load balancer and return it with listeners, pools and members populated "
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

# [REST Example](#addLoadBalancerMembers-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#addLoadBalancerMembers-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_LoadBalancerServerInstanceInfo]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_Member/addLoadBalancerMembers'
```
