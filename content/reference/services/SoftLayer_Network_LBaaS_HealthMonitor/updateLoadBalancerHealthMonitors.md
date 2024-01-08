---
title: "updateLoadBalancerHealthMonitors"
description: "Update load balancers health monitor and return load balancer object with listeners (frontend), pools (backend), health monitor server instances (members) and datacenter populated "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_HealthMonitor"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_LBaaS_HealthMonitor"
---

### [REST Example](#updateLoadBalancerHealthMonitors-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateLoadBalancerHealthMonitors-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_LBaaS_HealthMonitor/updateLoadBalancerHealthMonitors'
```
