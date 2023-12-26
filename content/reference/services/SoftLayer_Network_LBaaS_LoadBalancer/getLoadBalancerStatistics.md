---
title: "getLoadBalancerStatistics"
description: "Return load balancers statistics such as total number of current sessions and total number of accumulated connections. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_LoadBalancer/getLoadBalancerStatistics'
```
