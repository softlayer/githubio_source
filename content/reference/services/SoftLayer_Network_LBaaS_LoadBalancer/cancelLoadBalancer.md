---
title: "cancelLoadBalancer"
description: "Cancel a load balancer with the given uuid. The billing system will execute the deletion of load balancer and all objects associated with it such as load balancer appliances, listeners, pools and members in the background. "
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
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_LoadBalancer/cancelLoadBalancer'
```
