---
title: "getServices"
description: "the services on this load balancer."
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LoadBalancer_VirtualIpAddress"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_LoadBalancer_VirtualIpAddressID}/getServices'
```
