---
title: "deleteLoadBalancerProtocols"
description: "Delete load balancers front- and backend protocols and return load balancer object with listeners (frontend), pools (backend), server instances (members) and datacenter populated. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Listener"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_Listener"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_Listener/deleteLoadBalancerProtocols'
```
