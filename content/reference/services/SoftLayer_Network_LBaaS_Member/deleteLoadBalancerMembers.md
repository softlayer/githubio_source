---
title: "deleteLoadBalancerMembers"
description: "Delete given members from load balancer and return load balancer object with listeners, pools and members populated "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_Member/deleteLoadBalancerMembers'
```
