---
title: "createL7Pool"
description: "Create a backend to be used for L7 load balancing. This L7 pool has backend protocol, L7 members, L7 health monitor and session affinity. L7 pool is associated with L7 policies. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_L7Pool, SoftLayer_Network_LBaaS_L7Member, SoftLayer_Network_LBaaS_L7HealthMonitor, SoftLayer_Network_LBaaS_L7SessionAffinity]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_L7Pool/createL7Pool'
```
