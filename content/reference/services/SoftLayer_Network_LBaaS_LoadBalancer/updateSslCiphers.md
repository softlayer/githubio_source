---
title: "updateSslCiphers"
description: "Updates the load balancer with the new cipher list. All new connections going forward will use the new set of ciphers selected by the user. "
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
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_LoadBalancer/updateSslCiphers'
```
